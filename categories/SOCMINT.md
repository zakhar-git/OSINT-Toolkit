# SOCMINT

[Previous: GEOINT](../categories/GEOINT.md) · [Next: HUMINT](../categories/HUMINT.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Social media capture, platform datasets, and public interaction analysis.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [4CAT](#4cat)
  - [Zeeschuimer](#zeeschuimer)
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

<a id="4cat"></a>
<details>
<summary><strong>4CAT</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | 4CAT |
| **Description** | Research platform for capturing and analyzing social-media datasets through modular data-source and analysis processors. |
| **Category** | SOCMINT |
| **Platform** | Linux server; Docker; Python |
| **Repository** | [https://github.com/digitalmethodsinitiative/4cat](https://github.com/digitalmethodsinitiative/4cat) |
| **Official website** | [https://4cat.nl/](https://4cat.nl/) |
| **License** | MPL-2.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
git clone https://github.com/digitalmethodsinitiative/4cat.git
cd 4cat
./helper-scripts/docker-dev/build.sh
```

**Quick example**

```text
# Create a bounded dataset in 4CAT and export analysis artifacts with source metadata.
```

**Supported sources**

Platform datasets supported by installed 4CAT modules and user-supplied datasets.

**Pros**

Designed for social-media research; modular analysis pipeline; 2026 release activity observed.

**Limitations**

Source support varies by platform policy and module health; server operation requires data-governance controls; outputs need sampling and bias notes.

</details>

<a id="zeeschuimer"></a>
<details>
<summary><strong>Zeeschuimer</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Zeeschuimer |
| **Description** | Browser extension for capturing social-media data observed during ordinary browsing and preparing datasets for 4CAT-style analysis. |
| **Category** | SOCMINT |
| **Platform** | Chromium- and Firefox-based browsers |
| **Repository** | [https://github.com/digitalmethodsinitiative/zeeschuimer](https://github.com/digitalmethodsinitiative/zeeschuimer) |
| **Official website** | [https://github.com/digitalmethodsinitiative/zeeschuimer](https://github.com/digitalmethodsinitiative/zeeschuimer) |
| **License** | MPL-2.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Install from the official browser-store release or build from the repository.
```

**Quick example**

```text
# Start a new collection, browse the scoped public view, then export or upload the captured dataset.
```

**Supported sources**

Public social-media content rendered in the browser on supported platforms.

**Pros**

Captures what the analyst actually observed; integrates with research datasets; 2026 release activity observed.

**Limitations**

Scrolling depth shapes the dataset; platform UI changes can break capture; collection must respect platform terms and subject-safety constraints.

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

[Previous: GEOINT](../categories/GEOINT.md) · [Next: HUMINT](../categories/HUMINT.md) · [Back to README](../README.md)
