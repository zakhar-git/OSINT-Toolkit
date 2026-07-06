#!/usr/bin/env python3
"""Generate Markdown TOCs between explicit marker comments."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- toc:start -->"
END = "<!-- toc:end -->"


def github_slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def build_toc(text: str) -> str:
    visible = re.sub(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        "",
        text,
        flags=re.DOTALL,
    )
    items: list[tuple[int, str, str]] = []
    current_h2 = ""
    for line in visible.splitlines():
        heading = re.match(r"^(#{2,3})\s+(.+?)\s*$", line)
        if heading:
            level = len(heading.group(1))
            title = re.sub(r"\s+#+$", "", heading.group(2)).strip()
            if title.lower() == "table of contents":
                continue
            anchor = github_slug(title)
            items.append((level, title, anchor))
            if level == 2:
                current_h2 = title

    # Tool cards use explicit anchors and summaries instead of headings to keep
    # the rendered document compact. Include them beneath the Tools section.
    cards = re.findall(
        r'<a id="([^"]+)"></a>\s*<details>\s*<summary><strong>([^<]+)</strong></summary>',
        visible,
    )
    if cards:
        expanded: list[tuple[int, str, str]] = []
        inserted = False
        for item in items:
            expanded.append(item)
            if item[0] == 2 and item[1] == "Tools":
                expanded.extend((3, title, anchor) for anchor, title in cards)
                inserted = True
        if inserted:
            items = expanded

    return "\n".join(
        f"{'  ' * (level - 2)}- [{title}](#{anchor})" for level, title, anchor in items
    )


def process(path: Path, check: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    start_matches = list(re.finditer(rf"(?m)^{re.escape(START)}$", original))
    end_matches = list(re.finditer(rf"(?m)^{re.escape(END)}$", original))
    if not start_matches and not end_matches:
        return False
    if len(start_matches) != 1 or len(end_matches) != 1:
        raise ValueError(f"{path}: expected exactly one TOC marker pair")
    start = start_matches[0]
    end = end_matches[0]
    if start.end() > end.start():
        raise ValueError(f"{path}: TOC start marker must appear before end marker")
    before = original[: start.start()]
    after = original[end.end() :]
    toc = build_toc(original)
    updated = f"{before}{START}\n{toc}\n{END}{after}"
    changed = updated != original
    if changed and not check:
        path.write_text(updated, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if a TOC is stale.")
    args = parser.parse_args()
    changed: list[Path] = []
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        if process(path, args.check):
            changed.append(path.relative_to(ROOT))
    if args.check and changed:
        print("Stale table of contents:")
        for path in changed:
            print(f"- {path}")
        return 1
    action = "Would update" if args.check else "Updated"
    print(f"{action} {len(changed)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
