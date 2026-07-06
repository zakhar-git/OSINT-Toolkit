#!/usr/bin/env python3
"""Validate repository structure and documentation invariants."""

from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
CATEGORY_NAMES = [
    "Username", "Email", "Phone", "Telegram", "Discord", "Steam", "Gaming",
    "Social Media", "Images", "Documents", "Domains", "IP", "GEOINT",
    "SOCMINT", "HUMINT", "OPSEC", "AI", "Infrastructure", "Misc",
]
WORKFLOW_NAMES = [
    "Username Investigation", "Telegram Investigation", "Email Investigation",
    "Phone Investigation", "Image Investigation", "Domain Investigation",
    "Infrastructure Investigation", "Company Investigation", "Person Investigation",
]
FIELDS = [
    "Name", "Description", "Category", "Platform", "Repository",
    "Official website", "License", "Status", "Last verified",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_structure(errors: list[str]) -> None:
    required = [
        "README.md", "LICENSE", "CONTRIBUTING.md", "SECURITY.md",
        "CODE_OF_CONDUCT.md", "CHANGELOG.md", "ROADMAP.md", ".gitignore",
        ".github/PULL_REQUEST_TEMPLATE.md", ".github/TOOL_CARD_TEMPLATE.md",
        ".github/workflows/quality.yml", ".github/workflows/links.yml",
        ".github/workflows/toc.yml",
    ]
    required += [f"categories/{name}.md" for name in CATEGORY_NAMES]
    required += [f"workflows/{name}.md" for name in WORKFLOW_NAMES]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(errors, f"Missing required file: {relative}")


def validate_pages(errors: list[str]) -> None:
    card_count = 0
    for name in CATEGORY_NAMES:
        path = ROOT / "categories" / f"{name}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        cards = text.split("<details>")[1:]
        card_count += len(cards)
        if len(cards) < 1:
            fail(errors, f"{path.relative_to(ROOT)}: no tool cards")
        for number, card in enumerate(cards, 1):
            for field in FIELDS:
                if f"| **{field}** |" not in card:
                    fail(errors, f"{path.relative_to(ROOT)} card {number}: missing {field}")
            for section in ["Installation", "Quick example", "Supported sources", "Pros", "Limitations"]:
                if f"**{section}**" not in card:
                    fail(errors, f"{path.relative_to(ROOT)} card {number}: missing {section}")
        for token in ["Previous:", "Next:", "Back to README", "<!-- toc:start -->", "<!-- toc:end -->"]:
            if token not in text:
                fail(errors, f"{path.relative_to(ROOT)}: missing {token}")
    if card_count != 38:
        fail(errors, f"Expected 38 tool cards, found {card_count}")

    for name in WORKFLOW_NAMES:
        path = ROOT / "workflows" / f"{name}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for token in ["Previous:", "Next:", "Back to README", "## Evidence package", "## Stop conditions", "<!-- toc:start -->"]:
            if token not in text:
                fail(errors, f"{path.relative_to(ROOT)}: missing {token}")


def validate_internal_links(errors: list[str]) -> None:
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\((?:<([^>]+)>|([^\s)]+))\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        for match in pattern.finditer(text):
            target = unquote(match.group(1) or match.group(2))
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            resolved = (path.parent / file_part).resolve()
            if not resolved.exists():
                fail(errors, f"{path.relative_to(ROOT)}: broken local link {target}")


def validate_content(errors: list[str]) -> None:
    all_text = "\n".join(path.read_text(encoding="utf-8") for path in ROOT.rglob("*.md"))
    for placeholder in ["OWNER/REPO", "your-email@example.com", "@maintainers"]:
        if placeholder in all_text:
            fail(errors, f"Forbidden deployment placeholder: {placeholder}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for value in ["| Category guides | 19 |", "| Investigation workflows | 9 |", "| Curated tool cards | 38 |"]:
        if value not in readme:
            fail(errors, f"README statistic missing or stale: {value}")


def main() -> int:
    errors: list[str] = []
    validate_structure(errors)
    validate_pages(errors)
    validate_internal_links(errors)
    validate_content(errors)
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Repository validation passed: 19 categories, 9 workflows, 38 tool cards.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
