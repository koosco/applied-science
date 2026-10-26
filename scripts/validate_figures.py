"""Check the published Markdown ↔ SVG figure contract (stdlib only).

Run from any directory: python scripts/validate_figures.py
The checker validates structure and links, not mathematical correctness.
"""

from __future__ import annotations

import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = Path("docs/assets/figures")
SVG_NAMESPACE = "{http://www.w3.org/2000/svg}"
IMAGE_LINE = re.compile(r"!\[([^\[\]\n]*)\]\(([^()\s]+)\)")
KEBAB_CASE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
INVALID_NUMBERS = re.compile(r"\b(?:nan|infinity|undefined)\b", flags=re.IGNORECASE)


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def validate_svg(path: Path, root: Path) -> list[str]:
    """Check XML, accessibility, security and basic diagram geometry."""
    name = _relative(path, root)
    errors: list[str] = []
    content = path.read_text(encoding="utf-8")
    if "<!DOCTYPE" in content.upper() or "<!ENTITY" in content.upper():
        errors.append(f"{name}: DTD/entity declarations are not allowed")
        return errors

    try:
        svg = ET.fromstring(content)
    except ET.ParseError as exc:
        return [f"{name}: invalid SVG XML: {exc}"]

    if svg.tag != SVG_NAMESPACE + "svg":
        errors.append(f"{name}: SVG root must use the official namespace")
        return errors
    if svg.get("role") != "img":
        errors.append(f"{name}: SVG must have role=img")

    view_box = svg.get("viewBox", "").split()
    try:
        values = [float(part) for part in view_box]
        if len(values) != 4 or not all(math.isfinite(v) for v in values) or any(v <= 0 for v in values[2:]):
            raise ValueError
    except ValueError:
        errors.append(f"{name}: viewBox must contain four finite values with positive width and height")

    titles = svg.findall(SVG_NAMESPACE + "title")
    descriptions = svg.findall(SVG_NAMESPACE + "desc")
    if len(titles) != 1 or not "".join(titles[0].itertext()).strip():
        errors.append(f"{name}: SVG needs exactly one nonempty <title>")
    if len(descriptions) != 1 or not "".join(descriptions[0].itertext()).strip():
        errors.append(f"{name}: SVG needs exactly one nonempty <desc>")

    ids: set[str] = set()
    for node in svg.iter():
        local_tag = node.tag.rsplit("}", 1)[-1] if isinstance(node.tag, str) else ""
        if local_tag in {"script", "foreignObject"}:
            errors.append(f"{name}: <{local_tag}> is not allowed in a static figure")
        item_id = node.get("id")
        if item_id:
            if item_id in ids:
                errors.append(f"{name}: duplicate SVG ID {item_id!r}")
            ids.add(item_id)
        for key, value in node.attrib.items():
            attr = key.rsplit("}", 1)[-1]
            if attr.lower().startswith("on"):
                errors.append(f"{name}: inline event handler {attr!r} is not allowed")
            if attr.lower() in {"href", "src"} and not value.startswith("#"):
                errors.append(f"{name}: external asset reference {value!r} is not allowed")

    labeled = svg.get("aria-labelledby", "").split()
    required_ids = [node.get("id") for node in titles + descriptions]
    if any(not value or value not in labeled for value in required_ids) or len(labeled) != 2 or len(set(labeled)) != 2:
        errors.append(f"{name}: aria-labelledby must reference the title and desc IDs")

    if INVALID_NUMBERS.search(content):
        errors.append(f"{name}: unexpected NaN/Infinity/undefined; check plotted coordinates")

    return errors


def validate_repo(repo_root: Path) -> list[str]:
    """Check every local documentation image and every committed figure SVG."""
    repo_root = repo_root.resolve()
    docs_root = (repo_root / "docs").resolve()
    figure_root = (repo_root / FIGURE_DIR).resolve()
    errors: list[str] = []
    if not docs_root.is_dir() or not figure_root.is_dir():
        return ["docs/ and docs/assets/figures/ must exist"]

    referenced: set[Path] = set()
    for document in sorted(docs_root.rglob("*.md")):
        if any(part in {"convention", "simulations"} for part in document.relative_to(docs_root).parts):
            continue  # Guide code samples and generated simulator output are not published figures.
        lines = document.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, 1):
            if not line.lstrip().startswith("!["):
                continue
            match = IMAGE_LINE.fullmatch(line.strip())
            where = f"{_relative(document, repo_root)}:{lineno}"
            if not match:
                errors.append(f"{where}: image must be on its own line as ![alt](relative/path.svg)")
                continue
            alt, reference = match.groups()
            if not alt.strip():
                errors.append(f"{where}: image alt text must be descriptive and nonempty")
            if reference.startswith(("http:", "https:", "data:", "/")) or "?" in reference or "#" in reference:
                errors.append(f"{where}: use a plain, relative local image path without query or fragment")
                continue
            target = (document.parent / reference).resolve()
            if not target.is_relative_to(docs_root):
                errors.append(f"{where}: image escapes docs/: {reference}")
                continue
            if not target.is_file():
                errors.append(f"{where}: image not found: {reference}")
                continue
            if target.suffix.lower() == ".svg":
                if not target.is_relative_to(figure_root):
                    errors.append(f"{where}: SVG figures belong under docs/assets/figures/")
                else:
                    referenced.add(target)
                    next_line = next((text.strip() for text in lines[lineno:] if text.strip()), "")
                    if not (next_line.startswith("*") and next_line.endswith("*") and len(next_line) > 2):
                        errors.append(f"{where}: add an italic explanatory caption below the SVG")

    figures = sorted(figure_root.rglob("*.svg"))
    for figure in figures:
        parts = figure.relative_to(figure_root).parts
        if not all(KEBAB_CASE.fullmatch(p.removesuffix(".svg")) for p in parts):
            errors.append(f"{_relative(figure, repo_root)}: use descriptive kebab-case paths")
        errors.extend(validate_svg(figure, repo_root))
        if figure not in referenced:
            errors.append(f"{_relative(figure, repo_root)}: SVG is not referenced by a published Markdown image")
    return errors


def main() -> int:
    errors = validate_repo(REPO_ROOT)
    if errors:
        print(f"Figure convention validation FAILED ({len(errors)} issue(s)):")
        for issue in errors:
            print(f"  - {issue}")
        return 1
    count = len(list((REPO_ROOT / FIGURE_DIR).rglob("*.svg")))
    print(f"Figure convention validation OK ({count} SVG figure(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
