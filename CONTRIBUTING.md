# Contributing

[Previous: README](README.md) · [Next: Security](SECURITY.md) · [Back to README](README.md)

Contributions are reviewed for accuracy, investigative value, safety, and maintainability. A popular tool is not automatically a suitable tool. Read the [curation policy](docs/CURATION.md) before proposing a new entry.

## Table of contents

<!-- toc:start -->
- [Before you contribute](#before-you-contribute)
- [How to add a tool](#how-to-add-a-tool)
- [Evidence and safety standard](#evidence-and-safety-standard)
- [Category rules](#category-rules)
- [Naming rules](#naming-rules)
- [Markdown conventions](#markdown-conventions)
- [Review process](#review-process)
- [Local validation](#local-validation)
- [Commit and pull request rules](#commit-and-pull-request-rules)
<!-- toc:end -->

## Before you contribute

Search open issues and pull requests. Use the relevant issue form for changes that need discussion. Never include personal data, credentials, private source material, or live unauthorized targets in examples.

By contributing, you agree that your contribution is licensed under the repository's [MIT License](LICENSE) and that you will follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## How to add a tool

1. Open a [tool submission](.github/ISSUE_TEMPLATE/tool_submission.yml) or explain the addition in the pull request.
2. Verify the official repository and website directly.
3. Confirm the license from the upstream license file. Use `TODO` when it cannot be established.
4. Assess maintenance from releases, commits, issues, and an upstream statement; do not infer `Maintained` from popularity.
5. Review documentation, supported sources, installation paths, issue activity, and recent releases.
6. Test the tool with synthetic or standards-reserved input when practical.
7. Explain why the tool is better than existing entries for the category.
8. Add the data to `TOOLS` in `scripts/build_docs.py` under one primary category.
9. Use a reserved domain, IP address, phone number, or synthetic identifier in examples.
10. Run the documentation builder and validation commands.
11. Update README statistics and `CHANGELOG.md` when the catalog count changes.

Do not edit a generated category or workflow page directly. The next build will overwrite it.

## Evidence and safety standard

Every entry must:

- describe only capabilities supported by upstream documentation or direct testing;
- identify the actual source types queried;
- include meaningful limitations, not generic disclaimers;
- show current maintenance evidence from public upstream signals;
- avoid instructions for bypassing access controls, evading detection, or collecting private data;
- distinguish local processing, passive third-party lookup, authenticated access, and active probing;
- use `TODO` for unknown repository, license, installation, or maintenance facts;
- carry the date on which links and claims were last checked.

Do not include a tool when its repository is archived, core functionality is broken by platform changes, or current maintenance cannot be verified. A smaller category is acceptable when only a few entries meet the standard.

## Category rules

- Select the category by the analyst's starting artifact or principal discipline.
- Do not duplicate a card merely because a tool has secondary capabilities; cross-link instead.
- Put intelligence platforms without a clear primary artifact in `Misc`.
- Put active network tools in `Infrastructure` or `IP` and state the authorization requirement prominently.
- Put researcher-protection tools in `OPSEC`, not in target-discovery categories.
- A web service is acceptable when it provides distinct value, but proprietary status and repository unknowns must be explicit.
- Do not add filler to balance categories.

## Naming rules

- Use the upstream project's official capitalization.
- Category files use title case and the exact published category name.
- Workflow files end with `Investigation.md`.
- Heading text uses sentence case except proper names.
- Use descriptive link text; never use “click here.”
- Use UTC dates in `YYYY-MM-DD` format.

## Markdown conventions

- One H1 per file; use H2 and H3 in order.
- Wrap at natural sentence boundaries; the linter does not enforce a hard line length.
- Use fenced code blocks with a language or `text`.
- Use GitHub callouts sparingly for legal, safety, or destructive-action warnings.
- Keep tables compact and do not hide essential warnings inside collapsible sections.
- Preserve `<!-- toc:start -->` and `<!-- toc:end -->` markers.
- Use relative links for repository files and HTTPS for external sources.

See the complete [style guide](docs/STYLE_GUIDE.md) and copy the [tool-card template](.github/TOOL_CARD_TEMPLATE.md).

## Review process

1. **Triage:** scope, duplication, and safety are checked.
2. **Curation review:** the entry is checked against the selection and rejection criteria.
3. **Source review:** repository, website, license, maintenance, and capability claims are verified.
4. **Technical review:** installation and example are tested when practical.
5. **Editorial review:** category fit, limitations, navigation, and tone are checked.
6. **Automation:** Markdown, links, TOCs, and generated pages must pass.
7. **Merge:** a maintainer records the change in the changelog when release-relevant.

Reviewers may request removal when a project is malicious, deceptive, unlawfully invasive, unmaintainable, or materially duplicates a stronger entry.

## Local validation

```bash
python scripts/build_docs.py
python scripts/update_toc.py
python scripts/validate_repo.py
npx --yes markdownlint-cli2@0.18.1 "**/*.md" "#node_modules"
```

Use `lychee --config lychee.toml .` when the link checker is installed. Network checks can be rate-limited; document persistent false positives instead of disabling broad classes of links.

## Commit and pull request rules

Keep changes focused. Explain what was verified, how it was verified, and what remains uncertain. Do not mix unrelated formatting churn with catalog changes. Use present-tense commit subjects and complete the pull request checklist.

---

[Previous: README](README.md) · [Next: Security](SECURITY.md) · [Back to README](README.md)
