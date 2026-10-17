"""Dong bo repo Office_Design_Toolkit tu may cua Sang.

Chep vao repo:
  - ghi chu memory theo scripts/sources.tsv -> skills/*/references/*.md (bo metadata phien);
    ghi chu nao dinh tu cam (scripts/tu-cam.local.txt, khong dua len git) thi bo qua va bao;
  - vendor: frontend-design (plugin cache) va bo ui-ux-pro-max-skill (clone/pull repo goc).
Khong dung toi SKILL.md va cac ghi chu da luoc tay.

    python scripts/sync.py              # chep, in bao cao
    python scripts/sync.py --dry-run    # chi in viec se lam
    python scripts/sync.py --commit "ghi chu"   # chep + check_repo + commit + push

Bien moi truong (tuy chon): CLAUDE_MEMORY_DIR, UUPM_DIR.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HOME = Path.home()
PLUGINS = HOME / ".claude" / "plugins" / "installed_plugins.json"
UUPM_URL = "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git"
UUPM_DIR = Path(os.environ.get("UUPM_DIR") or Path(os.environ.get("LOCALAPPDATA", HOME)) / "Office_Design_Toolkit" / "ui-ux-pro-max-skill")
UUPM_SKILLS = ["ui-ux-pro-max", "banner-design", "brand", "design", "design-system", "slides", "ui-styling"]
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", "*.bak*", ".in_use", ".orphaned_at")


def forbidden() -> list[re.Pattern]:
    f = REPO / "scripts" / "tu-cam.local.txt"
    if not f.exists():
        print("CANH BAO: thieu scripts/tu-cam.local.txt - khong loc duoc tu cam")
        return []
    return [re.compile(x.strip(), re.I) for x in f.read_text(encoding="utf-8").splitlines() if x.strip() and not x.startswith("#")]


def memory_dir(names: list[str]) -> Path:
    env = os.environ.get("CLAUDE_MEMORY_DIR")
    if env:
        return Path(env)
    best, score = None, -1
    for d in (HOME / ".claude" / "projects").glob("*/memory"):
        n = sum((d / f"{x}.md").exists() for x in names)
        if n > score:
            best, score = d, n
    if best is None:
        sys.exit("Khong tim thay thu muc memory - dat CLAUDE_MEMORY_DIR")
    return best


def copy_tree(src: Path, dst: Path, dry: bool) -> None:
    if not src.is_dir():
        print(f"  [thieu] {src}")
        return
    print(f"  -> {dst.relative_to(REPO)}")
    if dry:
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=IGNORE)


def load_sources(link_only: bool = False) -> dict[str, str]:
    """Dong thuong: ghi chu chep tu dong. Dong bat dau '=': ghi chu da luoc tay, chi dung de noi lien ket."""
    out = {}
    for line in (REPO / "scripts" / "sources.tsv").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        name, dest = line.split("\t")
        if name.startswith("=") and not link_only:
            continue
        out[name.strip().lstrip("=")] = dest.strip()
    return out


def split_front(text: str) -> tuple[dict[str, str], str]:
    """Tach frontmatter don gian (name/description/modified) ra khoi than ghi chu."""
    meta: dict[str, str] = {}
    if not text.startswith("---"):
        return meta, text
    end = text.find("\n---", 3)
    if end < 0:
        return meta, text
    head, body = text[3:end], text[end + 4:]
    for raw in head.splitlines():
        m = re.match(r"\s*(name|description|modified):\s*(.*)$", raw)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip('"')
    return meta, body.lstrip("\n")


def convert_note(name: str, text: str, sources: dict[str, str], dest: str) -> str:
    meta, body = split_front(text)

    def link(m: re.Match) -> str:
        target = m.group(1)
        if target in sources:
            rel = os.path.relpath(sources[target], os.path.dirname(dest))
            return f"[{target}]({Path(rel).as_posix()})"
        return f"*{target}*"

    body = re.sub(r"\[\[([^\]]+)\]\]", link, body)
    title = meta.get("description", name).replace("\\\"", "\"").replace("\\\\", "\\")
    date = meta.get("modified", "")[:10]
    src = f"ghi nhớ `{name}`" + (f", cập nhật {date}" if date else "")
    return (f"---\nname: {name}\ndescription: {json.dumps(title, ensure_ascii=False)}\n---\n\n"
            f"> Nguồn: {src}. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.\n\n{body.rstrip()}\n")


def sync_notes(dry: bool, bad: list[re.Pattern]) -> None:
    sources = load_sources()
    links = load_sources(link_only=True)
    mem = memory_dir(list(sources))
    print(f"Ghi chu ({len(sources)}):")
    for name, dest in sources.items():
        src = mem / f"{name}.md"
        if not src.exists():
            print(f"  [thieu] {name}")
            continue
        out = convert_note(name, src.read_text(encoding="utf-8"), links, dest)
        hit = next((p.pattern for p in bad if p.search(out)), None)
        if hit:
            print(f"  [bo qua - dinh tu cam] {name}: luoc tay roi bo dong nay khoi sources.tsv")
            continue
        target = REPO / dest
        if dry:
            print(f"  {name} -> {dest}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        old = target.read_text(encoding="utf-8") if target.exists() else None
        if old != out:
            target.write_text(out, encoding="utf-8", newline="\n")
            print(f"  {'moi' if old is None else 'sua'}: {dest}")


def plugin_path(key: str) -> Path | None:
    data = json.loads(PLUGINS.read_text(encoding="utf-8"))
    entries = data.get("plugins", {}).get(key) or []
    return Path(entries[-1]["installPath"]) if entries else None


def update_uupm(dry: bool) -> None:
    if dry:
        return
    if (UUPM_DIR / ".git").exists():
        subprocess.check_call(["git", "-C", str(UUPM_DIR), "pull", "--ff-only", "-q"])
    else:
        UUPM_DIR.parent.mkdir(parents=True, exist_ok=True)
        subprocess.check_call(["git", "clone", "-q", UUPM_URL, str(UUPM_DIR)])


def sync_vendor(dry: bool) -> None:
    print("Vendor:")
    fd = plugin_path("frontend-design@claude-plugins-official")
    if fd:
        copy_tree(fd, REPO / "vendor" / "frontend-design", dry)
    update_uupm(dry)
    root = REPO / "vendor" / "ui-ux-pro-max-skill"
    for name in UUPM_SKILLS:
        copy_tree(UUPM_DIR / ".claude" / "skills" / name, root / "skills" / name, dry)
    if dry:
        return
    for f in ("LICENSE", "skill.json"):
        shutil.copy2(UUPM_DIR / f, root / f)
    rev = subprocess.check_output(["git", "-C", str(UUPM_DIR), "rev-parse", "--short", "HEAD"], text=True).strip()
    ver = json.loads((UUPM_DIR / "skill.json").read_text(encoding="utf-8"))["version"]
    (root / "UPSTREAM.txt").write_text(
        f"{UUPM_URL.removesuffix('.git')}\nversion {ver}\ncommit {rev}\n"
        "Chep nguyen ban tu .claude/skills/* cua repo goc (MIT). scripts/install.ps1 doi duong dan khi cai.\n",
        encoding="utf-8", newline="\n")
    print(f"  ui-ux-pro-max-skill v{ver} ({rev})")


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--commit", metavar="MSG")
    a = ap.parse_args()
    sync_notes(a.dry_run, forbidden())
    sync_vendor(a.dry_run)
    if a.dry_run:
        return 0
    rc = subprocess.call([sys.executable, str(REPO / "scripts" / "check_repo.py")])
    if rc:
        print("check_repo.py bao loi - khong commit.")
        return rc
    if a.commit:
        git = ["git", "-C", str(REPO)]
        subprocess.check_call(git + ["add", "-A"])
        if subprocess.call(git + ["diff", "--cached", "--quiet"]) == 0:
            print("Khong co thay doi.")
            return 0
        subprocess.check_call(git + ["commit", "-m", a.commit])
        subprocess.check_call(git + ["push"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
