#!/usr/bin/env python3
"""Bygg EPUB och PDF från lärobokens kanoniska Markdown-filer."""
from __future__ import annotations
import argparse, re, shutil, subprocess, sys, tempfile, unicodedata
from pathlib import Path
PANDOC_VERSION="3.1.11.1"

def top_yaml(path: Path):
    out={}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw or raw[0].isspace() or raw.lstrip().startswith(("#","-")) or ":" not in raw: continue
        k,v=raw.split(":",1); v=v.strip()
        if len(v)>=2 and v[0]==v[-1] and v[0] in "\"'": v=v[1:-1]
        out[k.strip()]=v
    return out

def chapter_list(path: Path):
    out=[]; active=False
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("chapters:"): active=True; continue
        if active:
            if raw.startswith("- "): out.append(raw[2:].strip().strip("\"'")); continue
            if raw and not raw[0].isspace(): break
    return out

def slugify(s):
    s=unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+","-",s).strip("-")

def pandoc_version():
    p=subprocess.run(["pandoc","--version"], text=True, capture_output=True)
    if p.returncode: raise RuntimeError("Pandoc finns inte i PATH.")
    m=re.search(r"pandoc\s+([0-9][^\s]*)",p.stdout.splitlines()[0]); return m.group(1) if m else "unknown"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root",default="."); ap.add_argument("--output-dir",required=True); ap.add_argument("--name",default=""); ap.add_argument("--formats",default="epub,pdf"); ap.add_argument("--allow-pandoc-version-mismatch",action="store_true"); args=ap.parse_args()
    root=Path(args.root).resolve(); out=Path(args.output_dir).resolve()
    if subprocess.run([sys.executable,"scripts/validate_project.py","."],cwd=root).returncode: return 1
    ver=pandoc_version()
    if ver!=PANDOC_VERSION and not args.allow_pandoc_version_mismatch:
        print(f"ERROR: Pandoc {PANDOC_VERSION} krävs; hittade {ver}.",file=sys.stderr); return 2
    meta_path=root/"docs/export-metadata.yaml"; meta=top_yaml(meta_path)
    chapters=[root/p for p in chapter_list(meta_path)]
    title=meta["title"]; subtitle=meta.get("subtitle",""); author=meta["author"]; base=args.name or meta.get("project_slug") or slugify(title)
    formats=[x.strip().lower() for x in args.formats.split(",") if x.strip()]
    if not formats or set(formats)-{"epub","pdf"}: print("ERROR: --formats måste vara epub och/eller pdf.",file=sys.stderr); return 2
    out.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="book-build-") as td:
        t=Path(td); pandoc_meta=t/"metadata.yaml"
        cover_rel=meta["cover_image"]; pandoc_meta.write_text("\n".join([f'title: "{title}"',f'subtitle: "{subtitle}"',f'author: "{author}"',f'lang: "{meta.get("language","sv")}"',f'cover-path: "{cover_rel}"'])+"\n",encoding="utf-8")
        if "epub" in formats:
            target=out/f"{base}.epub"
            cmd=["pandoc",*[str(p) for p in chapters],"--from=markdown","--to=epub3","--output",str(target),"--metadata-file",str(pandoc_meta),"--css",str(root/"publishing/epub.css"),"--epub-cover-image",str(root/meta["cover_image"]),"--toc","--toc-depth=1","--split-level=1","--resource-path",f"{root / 'chapters'}:{root}"]
            subprocess.run(cmd,cwd=root,check=True)
            subprocess.run([sys.executable,str(root/"publishing/fix-epub-after-pandoc.py"),str(target)],cwd=root,check=True)
            print(f"OK: EPUB skapad: {target}")
        if "pdf" in formats:
            if not shutil.which("xelatex"): print("ERROR: xelatex krävs för PDF-bygget.",file=sys.stderr); return 2
            target=out/f"{base}.pdf"
            font_args=[]
            required=("texgyrepagella-regular.otf","texgyrepagella-bold.otf","texgyrepagella-italic.otf","texgyrepagella-bolditalic.otf")
            font_dir=None
            for base_dir in (Path("/usr/share/texmf"),Path("/usr/share/fonts")):
                if not base_dir.exists(): continue
                for regular in base_dir.rglob(required[0]):
                    candidate=regular.parent
                    if all((candidate/name).is_file() for name in required): font_dir=candidate; break
                if font_dir: break
            if font_dir: font_args=["--variable",f"pdf-font-dir={font_dir.as_posix()}"]
            cmd=["pandoc",*[str(p) for p in chapters],"--from=markdown","--to=pdf","--pdf-engine=xelatex","--output",str(target),"--metadata-file",str(pandoc_meta),"--template",str(root/"publishing/pdf-template.tex"),"--lua-filter",str(root/"publishing/pdf-filter.lua"),*font_args,"--toc","--toc-depth=1","--top-level-division=chapter","--resource-path",f"{root / 'chapters'}:{root}"]
            subprocess.run(cmd,cwd=root,check=True)
            if not target.exists() or target.stat().st_size<10000: print("ERROR: PDF-bygget gav ingen giltig PDF.",file=sys.stderr); return 2
            print(f"OK: PDF skapad: {target}")
    return 0
if __name__=="__main__": raise SystemExit(main())
