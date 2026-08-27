#!/usr/bin/env python3
"""Efterbearbeta Pandoc-EPUB för kompakt tvådelad kapitelrubrik."""
from __future__ import annotations
import re, sys, tempfile, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
NS={"opf":"http://www.idpf.org/2007/opf","xhtml":"http://www.w3.org/1999/xhtml"}
ET.register_namespace("",NS["opf"])

def find_root(container_xml: Path) -> Path:
    root=ET.parse(container_xml).getroot()
    item=root.find(".//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile")
    if item is None: raise RuntimeError("EPUB container saknar rootfile.")
    return Path(item.attrib["full-path"])

def split_headings(epub_dir: Path):
    changed=0
    pattern=re.compile(r"^\s*Kapitel\s+(\d+)\s*:\s*(.+?)\s*$",re.I)
    for xhtml in epub_dir.rglob("*.xhtml"):
        tree=ET.parse(xhtml); root=tree.getroot(); local=False
        for h1 in root.findall(".//xhtml:h1",NS):
            text="".join(h1.itertext()).strip(); m=pattern.match(text)
            if not m: continue
            attrs=dict(h1.attrib); h1.clear(); h1.attrib.update(attrs)
            n=ET.SubElement(h1,f"{{{NS['xhtml']}}}span",{"class":"chapter-number"}); n.text=f"Kapitel {m.group(1)}"
            t=ET.SubElement(h1,f"{{{NS['xhtml']}}}span",{"class":"chapter-title"}); t.text=m.group(2)
            local=True
        if local: tree.write(xhtml,encoding="utf-8",xml_declaration=True); changed+=1
    return changed

def nav_non_linear(epub_dir: Path, opf_rel: Path):
    opf=epub_dir/opf_rel; tree=ET.parse(opf); root=tree.getroot(); manifest=root.find("opf:manifest",NS); spine=root.find("opf:spine",NS)
    if manifest is None or spine is None: raise RuntimeError("EPUB OPF saknar manifest eller spine.")
    nav_ids={x.attrib["id"] for x in manifest.findall("opf:item",NS) if "nav" in x.attrib.get("properties","").split()}
    changed=False
    for ref in spine.findall("opf:itemref",NS):
        if ref.attrib.get("idref") in nav_ids and ref.attrib.get("linear")!="no": ref.set("linear","no"); changed=True
    if changed: tree.write(opf,encoding="utf-8",xml_declaration=True)
    return changed

def repack(src: Path,out: Path):
    if out.exists(): out.unlink()
    with zipfile.ZipFile(out,"w") as z:
        mime=src/"mimetype"; z.write(mime,"mimetype",compress_type=zipfile.ZIP_STORED)
        for p in sorted(src.rglob("*")):
            if p.is_file() and p!=mime: z.write(p,p.relative_to(src).as_posix(),compress_type=zipfile.ZIP_DEFLATED)

def main():
    if len(sys.argv)!=2: print("Användning: fix-epub-after-pandoc.py <fil.epub>",file=sys.stderr); return 2
    epub=Path(sys.argv[1]).resolve()
    with tempfile.TemporaryDirectory(prefix="fix-epub-") as td:
        d=Path(td)
        with zipfile.ZipFile(epub) as z: z.extractall(d)
        headings=split_headings(d); nav=nav_non_linear(d,find_root(d/"META-INF/container.xml")); repack(d,epub)
    print(f"Efterbearbetad EPUB: {headings} kapitelrubriker; nav linear=no: {nav}")
    return 0
if __name__=="__main__": raise SystemExit(main())
