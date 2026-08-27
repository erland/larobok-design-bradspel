#!/usr/bin/env python3
"""Snabb deterministisk validering för läroboksprojektet."""
from __future__ import annotations
import argparse, re, sys
from pathlib import Path
from urllib.parse import unquote

MARKERS = ("TODO", "FIXME", "[PLACEHOLDER]")
CHAPTER_FILE_RE = re.compile(r"^(\d{2})-.+\.md$")
CHAPTER_H1_RE = re.compile(r"^#\s+Kapitel\s+(\d+)\s*:\s*(.+?)\s*$", re.I)
REQUIRED_PATHS = (
    "README.md", "docs/export-metadata.yaml", "chapters", "assets/cover/cover.png",
    "publishing/epub.css", "publishing/fix-epub-after-pandoc.py",
    "publishing/pdf-template.tex", "publishing/pdf-filter.lua",
)
REQUIRED_METADATA = ("title", "author", "language", "cover_image", "project_slug")

def fail(errors, msg):
    errors.append(msg); print(f"ERROR: {msg}", file=sys.stderr)

def top_yaml(path: Path):
    out = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw or raw[0].isspace() or raw.lstrip().startswith(("#", "-")) or ":" not in raw:
            continue
        k,v=raw.split(":",1); v=v.strip()
        if len(v)>=2 and v[0]==v[-1] and v[0] in "\"'": v=v[1:-1]
        out[k.strip()]=v
    return out

def metadata_chapters(path: Path):
    result=[]; active=False
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("chapters:"):
            active=True; continue
        if active:
            if raw.startswith("- "):
                result.append(raw[2:].strip().strip("\"'")); continue
            if raw and not raw[0].isspace(): break
    return result

def validate_links(root: Path, errors):
    rx=re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        if ".git" in md.parts: continue
        for target in rx.findall(md.read_text(encoding="utf-8")):
            target=target.strip().strip("<>")
            if not target or target.startswith(("#","http://","https://","mailto:")): continue
            target=unquote(target.split("#",1)[0].split("?",1)[0])
            candidate=(md.parent/target).resolve()
            try: candidate.relative_to(root.resolve())
            except ValueError: continue
            if not candidate.exists(): fail(errors, f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("root", nargs="?", default="."); args=ap.parse_args()
    root=Path(args.root).resolve(); errors=[]
    for rel in REQUIRED_PATHS:
        if not (root/rel).exists(): fail(errors, f"Obligatorisk projektsökväg saknas: {rel}")
    if errors: return 1
    meta=top_yaml(root/"docs/export-metadata.yaml")
    for key in REQUIRED_METADATA:
        if not meta.get(key): fail(errors, f"docs/export-metadata.yaml saknar värde för '{key}'.")
    listed=metadata_chapters(root/"docs/export-metadata.yaml")
    if not listed: fail(errors, "Metadata innehåller ingen chapters-lista.")
    for rel in listed:
        p=root/rel
        if not p.is_file(): fail(errors, f"Kapitel i metadata saknas: {rel}")
    actual=[p.relative_to(root).as_posix() for p in sorted((root/"chapters").glob("*.md"))]
    if listed and actual != listed:
        fail(errors, "Kapitelordningen/listan i metadata matchar inte chapters-katalogen.")
    nums=[]
    for rel in listed:
        p=root/rel; text=p.read_text(encoding="utf-8"); stripped=text.strip()
        if not stripped: fail(errors, f"{rel} är tom."); continue
        first=next((line.strip() for line in text.splitlines() if line.strip()), "")
        fm=CHAPTER_FILE_RE.match(p.name)
        if p.name.startswith("00-"):
            if not first.lower().startswith("# inledning"): fail(errors, f"{rel} ska börja med '# Inledning'.")
        elif fm:
            n=int(fm.group(1)); hm=CHAPTER_H1_RE.fullmatch(first)
            if not hm or int(hm.group(1)) != n: fail(errors, f"{rel} ska börja med '# Kapitel {n}: ...'.")
            nums.append(n)
        for marker in MARKERS:
            if marker in text: fail(errors, f"{rel} innehåller arbetsmarkören {marker}.")
    if nums and nums != list(range(1, max(nums)+1)): fail(errors, "Kapitelnumreringen har luckor eller fel ordning.")
    cover=root/meta.get("cover_image","")
    if not cover.is_file(): fail(errors, f"Omslagsfilen från metadata saknas: {meta.get('cover_image')}")
    validate_links(root, errors)
    if errors:
        print(f"\nValidation failed: {len(errors)} error(s).", file=sys.stderr); return 1
    print(f"OK: projektvalidering godkänd. {len(listed)} manusfiler ({len(nums)} numrerade kapitel + inledning).")
    return 0
if __name__ == "__main__": raise SystemExit(main())
