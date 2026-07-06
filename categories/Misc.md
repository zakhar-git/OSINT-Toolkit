# Misc

[Previous: Infrastructure](../categories/Infrastructure.md) · [Next: Username](../categories/Username.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

General-purpose OSINT frameworks and extensible research consoles.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Recon-ng](#recon-ng)
  - [OSINT Framework](#osint-framework)
- [Quality controls](#quality-controls)
- [Related workflows](#related-workflows)
<!-- toc:end -->

## Scope

Use this category to generate and test leads, not to declare identity or attribution from a single match. Define the research question, collection boundary, and retention rule before opening a tool.

## Investigation approach

1. Preserve the input exactly as received and record its source.
2. Normalize only in a separate working copy and document every transformation.
3. Start with passive or locally processed sources.
4. Validate important results manually against the primary source.
5. Record UTC timestamps, URLs, tool versions, queries, and uncertainty.
6. Minimize personal data and stop when the research question is answered.

## Tools

The entries below are curated starting points, not endorsements. Verify current upstream documentation and release signatures before installation.

<a id="recon-ng"></a>
<details>
<summary><strong>Recon-ng</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Recon-ng |
| **Description** | Modular reconnaissance framework with workspaces, structured records, and exportable results. |
| **Category** | Misc |
| **Platform** | Linux, macOS, Windows; Python |
| **Repository** | [https://github.com/lanmaster53/recon-ng](https://github.com/lanmaster53/recon-ng) |
| **Official website** | [https://github.com/lanmaster53/recon-ng/wiki](https://github.com/lanmaster53/recon-ng/wiki) |
| **License** | GPL-3.0 |
| **Status** | Community |
| **Last verified** | 2026-07-07 |

**Installation**

```text
git clone https://github.com/lanmaster53/recon-ng.git
cd recon-ng
python -m pip install -r REQUIREMENTS
```

**Quick example**

```text
./recon-ng -w case-001
```

**Supported sources**

Public and credentialed APIs selected through separately installed modules.

**Pros**

Case workspaces; modular design; repeatable exports.

**Limitations**

Modules vary in maintenance and legal terms; API keys are sensitive; framework output needs source-level validation.

</details>

<a id="osint-framework"></a>
<details>
<summary><strong>OSINT Framework</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | OSINT Framework |
| **Description** | A navigable taxonomy of OSINT resources organized by starting data type and investigative objective. |
| **Category** | Misc |
| **Platform** | Web |
| **Repository** | [https://github.com/lockfale/OSINT-Framework](https://github.com/lockfale/OSINT-Framework) |
| **Official website** | [https://osintframework.com/](https://osintframework.com/) |
| **License** | MIT |
| **Status** | Community |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# No installation is required for the hosted website.
```

**Quick example**

```text
https://osintframework.com/
```

**Supported sources**

Curated links to third-party services and research resources.

**Pros**

Fast discovery by pivot type; broad coverage; source tree is public.

**Limitations**

A catalog is not validation; third-party links and business models change; evaluate every resource before submitting data.

</details>

## Quality controls

- Corroborate identity or ownership with at least two independent signals.
- Distinguish a tool result, an observed fact, and an analytical inference.
- Preserve raw output before filtering or transforming it.
- Re-run time-sensitive checks before publication.
- Document negative results; they describe coverage, not absence.

## Related workflows

Use the closest procedural guide in the [workflow index](../README.md#workflows). When no exact workflow exists, combine the relevant collection steps with the evidence-preservation requirements in [CONTRIBUTING](../CONTRIBUTING.md#evidence-and-safety-standard).

---

[Previous: Infrastructure](../categories/Infrastructure.md) · [Next: Username](../categories/Username.md) · [Back to README](../README.md)
