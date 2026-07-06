# SOCMINT

[Previous: GEOINT](../categories/GEOINT.md) · [Next: HUMINT](../categories/HUMINT.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Structured research into public social interactions and identities.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Social Analyzer](#social-analyzer)
  - [snscrape](#snscrape)
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

<a id="social-analyzer"></a>
<details>
<summary><strong>Social Analyzer</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Social Analyzer |
| **Description** | Correlates a username or name across supported social and public-web sources with multiple analysis modes. |
| **Category** | SOCMINT |
| **Platform** | Linux, macOS, Windows; Python; Node.js; Docker |
| **Repository** | [https://github.com/qeeqbox/social-analyzer](https://github.com/qeeqbox/social-analyzer) |
| **Official website** | [https://github.com/qeeqbox/social-analyzer](https://github.com/qeeqbox/social-analyzer) |
| **License** | MIT |
| **Status** | Community |
| **Last verified** | 2026-07-07 |

**Installation**

```text
python -m pip install social-analyzer
```

**Quick example**

```text
social-analyzer --username analyst_handle --metadata --top 100
```

**Supported sources**

Public profile endpoints and search results across supported websites.

**Pros**

Broad query modes; JSON output; useful for initial lead generation.

**Limitations**

Coverage breadth increases false positives; automated requests can be blocked; all identity links require corroboration.

</details>

<a id="snscrape"></a>
<details>
<summary><strong>snscrape</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | snscrape |
| **Description** | Collectors for public social-network content that produce structured items for downstream analysis. |
| **Category** | SOCMINT |
| **Platform** | Linux, macOS, Windows; Python |
| **Repository** | [https://github.com/JustAnotherArchivist/snscrape](https://github.com/JustAnotherArchivist/snscrape) |
| **Official website** | [https://github.com/JustAnotherArchivist/snscrape](https://github.com/JustAnotherArchivist/snscrape) |
| **License** | GPL-3.0 |
| **Status** | Community |
| **Last verified** | 2026-07-07 |

**Installation**

```text
pipx install snscrape
```

**Quick example**

```text
snscrape --jsonl reddit-search 'example query' > results.jsonl
```

**Supported sources**

Public content from the collectors currently supported by the installed version.

**Pros**

Streaming JSON Lines; composable CLI; no private-data claim.

**Limitations**

Individual collectors frequently break after platform changes; verify current upstream support; collection may be restricted by terms or law.

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
