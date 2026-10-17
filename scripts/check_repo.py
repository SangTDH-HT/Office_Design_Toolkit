"""Soat repo truoc khi commit: frontmatter skill, lien ket tuong doi, bi mat, ban quyen.

    python scripts/check_repo.py
Thoat 1 neu co LOI; CANH BAO chi in ra.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TEXT = {".md", ".py", ".ps1", ".json", ".tsv", ".txt", ".jsx", ".csv", ".svg", ".yml", ".yaml", ".js", ".ts", ".html"}
SECRET = [
    (re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"), "token GitHub"),
    (re.compile(r"sk-ant-[A-Za-z0-9_-]{20,}"), "khoa API Anthropic"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "khoa AWS"),
    (re.compile(r"(?i)(password|matkhau|mat_khau)\s*[:=]\s*['\"][^'\"\s]{4,}['\"]"), "mat khau ghi thang"),
    (re.compile(r"(?i)trello_(api_key|token)\"?\s*[:=]\s*\"?[0-9a-f]{32,}"), "khoa Trello"),
]
FORBIDDEN = [
    ("Anthropic, PBC. All rights reserved", "tai lieu Anthropic khong duoc chep (docx/pptx/xlsx/pdf)"),
]
DOTFILES = {".gitignore", ".gitattributes"}
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

errors: list[str] = []
TU_CAM_FILE = REPO / "scripts" / "tu-cam.local.txt"  # khong dua len git
TU_CAM = [re.compile(x.strip(), re.I) for x in (TU_CAM_FILE.read_text(encoding="utf-8").splitlines() if TU_CAM_FILE.exists() else [])
          if x.strip() and not x.startswith("#")]
warns: list[str] = []


def front(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    meta = {}
    for raw in text[3:end].splitlines():
        m = re.match(r"(name|description):\s*(.*)$", raw)
        if m:
            meta[m.group(1)] = m.group(2).strip()
    return meta


def check_skills() -> int:
    n = 0
    for skill in sorted(REPO.glob("skills/*/SKILL.md")) + sorted(REPO.glob("vendor/**/skills/*/SKILL.md")):
        n += 1
        meta = front(skill)
        folder = skill.parent.name
        if meta.get("name") != folder:
            errors.append(f"{skill.relative_to(REPO)}: name '{meta.get('name')}' khac ten thu muc '{folder}'")
        if not meta.get("description"):
            errors.append(f"{skill.relative_to(REPO)}: thieu description")
    return n


def check_files() -> None:
    for f in REPO.rglob("*"):
        if not f.is_file() or ".git" in f.parts or (f.suffix.lower() not in TEXT and f.name not in DOTFILES):
            continue
        rel = f.relative_to(REPO)
        try:
            text = f.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            warns.append(f"{rel}: khong phai UTF-8")
            continue
        if rel.as_posix() != "scripts/check_repo.py":
            for rx, what in SECRET:
                if rx.search(text):
                    errors.append(f"{rel}: nghi {what}")
            for needle, what in FORBIDDEN:
                if needle in text:
                    errors.append(f"{rel}: {what}")
        if rel.name != TU_CAM_FILE.name:
            for rx in TU_CAM:
                m = rx.search(text)
                if m:
                    line = text.count("\n", 0, m.start()) + 1
                    errors.append(f"{rel}:{line}: dinh tu cam ({m.group(0)!r})")
        if f.suffix == ".md" and "vendor" not in rel.parts:
            for target in LINK.findall(text):
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                path = target.split("#")[0]
                if path and not (f.parent / path).exists():
                    errors.append(f"{rel}: lien ket hong -> {target}")


def check_sources() -> None:
    for line in (REPO / "scripts" / "sources.tsv").read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            dest = line.split("\t")[1].strip()
            if not (REPO / dest).exists():
                errors.append(f"sources.tsv: chua co {dest} (chay scripts/sync.py)")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if not TU_CAM:
        warns.append("thieu scripts/tu-cam.local.txt - khong soat tu cam")
    n = check_skills()
    check_files()
    check_sources()
    for w in warns:
        print("CANH BAO", w)
    for e in errors:
        print("LOI", e)
    print(f"{n} skill, {len(errors)} loi, {len(warns)} canh bao")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
