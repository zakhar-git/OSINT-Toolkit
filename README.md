<div align="center">

![OSINT Toolkit](assets/header.svg)

# OSINT Toolkit

**Modern OSINT, HUMINT, SOCMINT, GEOINT, OPSEC and Digital Investigation Resources**

[![License: MIT](https://img.shields.io/badge/license-MIT-1f6feb.svg)](LICENSE)
[![Categories](https://img.shields.io/badge/categories-19-334155.svg)](#categories)
[![Workflows](https://img.shields.io/badge/workflows-9-334155.svg)](#workflows)
[![Curated tools](https://img.shields.io/badge/curated_tools-38-334155.svg)](#statistics)
[![Last verified](https://img.shields.io/badge/verified-2026--07--07-0f766e.svg)](#statistics)

[Previous: Roadmap](ROADMAP.md) · [Next: Username](categories/Username.md) · [Back to README](README.md)

</div>

OSINT Toolkit is a curated documentation project for responsible open-source research. It combines verified tools, repeatable investigation workflows, evidence-handling guidance, and maintenance controls in one navigable repository.

> [!IMPORTANT]
> Use these resources only for lawful, authorized purposes. Publicly accessible information can still be sensitive. Minimize collection, respect platform rules, protect sources, and document uncertainty.

## Table of contents

<!-- toc:start -->
- [Why this repository exists](#why-this-repository-exists)
- [Features](#features)
- [Quick navigation](#quick-navigation)
- [Repository architecture](#repository-architecture)
- [Categories](#categories)
- [Workflows](#workflows)
- [Tool-card standard](#tool-card-standard)
- [Repository philosophy](#repository-philosophy)
- [Statistics](#statistics)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)
<!-- toc:end -->

## Why this repository exists

Most resource collections optimize for volume. This project optimizes for investigative usefulness: what a tool does, where it fits, how to start, what it can observe, where it fails, and how to preserve results. Every listed project is real; unknown facts are marked `TODO` instead of being inferred.

## Features

- Consistent, reviewable tool cards with operational limits.
- Investigation workflows that begin with authority and end with preservation.
- Category guides organized by the analyst's starting artifact.
- Explicit status and verification dates for maintenance triage.
- Automated Markdown linting, link checking, and table-of-contents validation.
- Structured issue forms for bugs, features, and tool submissions.
- Minimal dependencies and fast, plain-Markdown navigation.

## Quick navigation

| Start with | Go to | Use when |
| --- | --- | --- |
| A known identifier | [Categories](#categories) | You have a username, email, number, image, document, domain, or address. |
| A research objective | [Workflows](#workflows) | You need a safe, repeatable investigation sequence. |
| A new tool | [Tool submission](.github/ISSUE_TEMPLATE/tool_submission.yml) | You want to propose a real, verifiable project. |
| A documentation change | [Contribution guide](CONTRIBUTING.md) | You are preparing a focused pull request. |
| A sensitive defect | [Security policy](SECURITY.md) | Reporting publicly could put users or sources at risk. |

## Repository architecture

```text
OSINT-Toolkit/
├── assets/                 # Repository-owned visual assets
├── categories/             # Artifact- and discipline-oriented guides
├── workflows/              # End-to-end investigation procedures
├── docs/                   # Architecture, style, and review standards
├── scripts/                # Deterministic documentation maintenance
└── .github/
    ├── ISSUE_TEMPLATE/     # Structured reports and submissions
    ├── workflows/          # Lint, link, and TOC automation
    └── PULL_REQUEST_TEMPLATE.md
```

Category and workflow pages are generated from reviewed data in [`scripts/build_docs.py`](scripts/build_docs.py). This keeps cards, safety language, and navigation consistent. See the [architecture guide](docs/ARCHITECTURE.md) for ownership and update boundaries.

## Categories

| Identity | Platforms | Media and files | Network and analysis |
| --- | --- | --- | --- |
| [Username](categories/Username.md) | [Telegram](categories/Telegram.md) | [Images](categories/Images.md) | [Domains](categories/Domains.md) |
| [Email](categories/Email.md) | [Discord](categories/Discord.md) | [Documents](categories/Documents.md) | [IP](categories/IP.md) |
| [Phone](categories/Phone.md) | [Steam](categories/Steam.md) | [GEOINT](categories/GEOINT.md) | [Infrastructure](categories/Infrastructure.md) |
| [HUMINT](categories/HUMINT.md) | [Gaming](categories/Gaming.md) | [SOCMINT](categories/SOCMINT.md) | [AI](categories/AI.md) |
| [OPSEC](categories/OPSEC.md) | [Social Media](<categories/Social Media.md>) |  | [Misc](categories/Misc.md) |

## Workflows

| Identity and person | Media and platform | Organization and infrastructure |
| --- | --- | --- |
| [Username Investigation](<workflows/Username Investigation.md>) | [Telegram Investigation](<workflows/Telegram Investigation.md>) | [Domain Investigation](<workflows/Domain Investigation.md>) |
| [Email Investigation](<workflows/Email Investigation.md>) | [Image Investigation](<workflows/Image Investigation.md>) | [Infrastructure Investigation](<workflows/Infrastructure Investigation.md>) |
| [Phone Investigation](<workflows/Phone Investigation.md>) |  | [Company Investigation](<workflows/Company Investigation.md>) |
| [Person Investigation](<workflows/Person Investigation.md>) |  |  |

## Tool-card standard

Every tool uses the same fields: name, description, category, platform, repository, official website, license, status, installation, quick example, supported sources, pros, limitations, and last verified date. Copy the [tool-card template](.github/TOOL_CARD_TEMPLATE.md); do not improvise a new layout.

<details>
<summary><strong>Status model</strong></summary>

| Status | Meaning |
| --- | --- |
| Active | Operational service or project with current availability. |
| Maintained | Upstream shows ongoing maintenance and supported installation paths. |
| Experimental | Useful but unstable, narrow, or explicitly experimental upstream. |
| Archived | Upstream is read-only or explicitly discontinued. |
| Deprecated | Upstream advises users to migrate or stop using it. |
| Community | Useful community project with variable or limited maintenance guarantees. |

</details>

## Repository philosophy

1. **Method before tool.** A tool result is a lead, not a conclusion.
2. **Primary sources first.** Prefer official repositories, documentation, registries, and original publications.
3. **Evidence over volume.** Preserve provenance, time, version, query, and uncertainty.
4. **Safety by design.** Use the least invasive source that can answer the question.
5. **Honest maintenance.** Remove or reclassify stale entries; mark unknowns as `TODO`.
6. **Reproducibility.** Another qualified analyst should be able to understand and repeat the work.

## Statistics

| Metric | Current value |
| --- | ---: |
| Category guides | 19 |
| Investigation workflows | 9 |
| Curated tool cards | 38 |
| Tool-card fields | 14 |
| Last catalog verification | 2026-07-07 |

Statistics describe this release and are updated with catalog changes. They are not a quality target; a smaller verified catalog is preferable to a larger unreliable one.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. New tools require an official source, license review, a safe example, concrete limitations, and manual link verification. The review process prioritizes accuracy, legality, maintenance, and category fit.

## Security

Do not disclose credentials, private datasets, live targets, bypass instructions, or personal data in issues. Follow [SECURITY.md](SECURITY.md) for private reporting and the repository's supported-version policy.

## License

Repository content and maintenance scripts are available under the [MIT License](LICENSE). Listed tools and services retain their own licenses and terms.

---

[Previous: Roadmap](ROADMAP.md) · [Next: Username](categories/Username.md) · [Back to README](README.md)
