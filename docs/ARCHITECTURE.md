# Repository architecture

[Previous: Roadmap](../ROADMAP.md) · [Next: Curation policy](CURATION.md) · [Back to README](../README.md)

## Table of contents

<!-- toc:start -->
- [Design goals](#design-goals)
- [Source of truth](#source-of-truth)
- [Content layers](#content-layers)
- [Change boundaries](#change-boundaries)
- [Automation](#automation)
- [Release model](#release-model)
<!-- toc:end -->

## Design goals

The repository is optimized for fast navigation, reviewable claims, deterministic layout, and low maintenance cost. It remains usable as plain Markdown without a documentation server.

## Source of truth

| Content | Source of truth | Generated output |
| --- | --- | --- |
| Tool metadata | `TOOLS` in `scripts/build_docs.py` | `categories/*.md` |
| Category scope and order | `CATEGORIES` in `scripts/build_docs.py` | Category pages and navigation |
| Workflow steps and order | `WORKFLOWS` in `scripts/build_docs.py` | `workflows/*.md` |
| Root policies | Individual root Markdown files | None |
| Table of contents | Headings and tool anchors in each page | Text between TOC markers |

Generated files are committed so GitHub renders a complete repository without a build step. Pull requests edit the source data, run the builder, and commit both source and output.

## Content layers

1. **README:** orientation, quick navigation, philosophy, and project status.
2. **Categories:** safe starting points organized by input artifact or discipline.
3. **Workflows:** ordered investigative methods, decision gates, preservation, and stop conditions.
4. **Maintainer documentation:** architecture, curation, conventions, contribution, review, conduct, and security.
5. **Automation:** deterministic generation and checks for structure, Markdown, TOCs, and links.

## Change boundaries

- Root policy files are edited directly.
- Category and workflow pages are never edited directly.
- The builder may create or replace only files declared in its category and workflow collections.
- The TOC updater may change only text between explicit marker comments.
- Validation is read-only and must never repair content silently.

## Automation

`quality.yml` rebuilds generated files, rejects uncommitted differences, checks TOCs, validates structural invariants, and runs Markdown lint. `links.yml` performs external and local link checks on pull requests and a weekly schedule. `toc.yml` regenerates TOCs on the default branch and can be run manually.

All workflows use minimal token permissions. External actions are tracked by Dependabot. Maintainers should pin actions to immutable commit SHAs when the repository's final ownership and update policy are established.

## Release model

Documentation releases use semantic versions. Major versions may change taxonomy or evidence standards; minor versions add workflows or curated tools; patch versions correct facts, links, or wording without changing method. Every public release updates `CHANGELOG.md` and verification statistics.

---

[Previous: Roadmap](../ROADMAP.md) · [Next: Curation policy](CURATION.md) · [Back to README](../README.md)
