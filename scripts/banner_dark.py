"""Sinh assets/banner-dark.svg tu assets/banner-light.svg (doi bang mau, giu nguyen hinh).

    python scripts/banner_dark.py
"""
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"

KEEP: list[str] = []  # chuoi giu nguyen mau (neu can)
SWAP = [
    ('fill="#F5F6F8"', 'fill="#1B2129"'),
    (".num { fill: #FFFFFF;", ".num { fill: #0E1A2B;"),
    ("#FFFFFF", "#232A34"),
    ("#1D3F73", "#DCE6F5"),
    ("#60656B", "#A9B0BA"),
    ("#CDD0D5", "#3A4250"),
    ("#2469C9", "#5B9BF0"),
    ("#2F80ED", "#5B9BF0"),
    ("#7F7F7F", "#6B7480"),
    ("#DFE1E5", "#3A4250"),
]


def main() -> None:
    svg = (ASSETS / "banner-light.svg").read_text(encoding="utf-8")
    for i, k in enumerate(KEEP):
        assert svg.count(k) == 1, k
        svg = svg.replace(k, f"@@KEEP{i}@@")
    for a, b in SWAP:
        svg = svg.replace(a, b)
    for i, k in enumerate(KEEP):
        svg = svg.replace(f"@@KEEP{i}@@", k)
    (ASSETS / "banner-dark.svg").write_text(svg, encoding="utf-8", newline="\n")
    print("assets/banner-dark.svg")


if __name__ == "__main__":
    main()
