# Email

[Previous: Username](../categories/Username.md) · [Next: Phone](../categories/Phone.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Email account discovery, reputation checks, and breach-aware triage.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Holehe](#holehe)
  - [h8mail](#h8mail)
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

<a id="holehe"></a>
<details>
<summary><strong>Holehe</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Holehe |
| **Description** | Tests whether an email address is associated with supported services through public account-recovery behavior. |
| **Category** | Email |
| **Platform** | Linux, macOS, Windows; Python |
| **Repository** | [https://github.com/megadose/holehe](https://github.com/megadose/holehe) |
| **Official website** | [https://github.com/megadose/holehe](https://github.com/megadose/holehe) |
| **License** | GPL-3.0 |
| **Status** | Community |
| **Last verified** | 2026-07-07 |

**Installation**

```text
pipx install holehe
```

**Quick example**

```text
holehe subject@example.com --only-used
```

**Supported sources**

Public registration and account-recovery responses from supported services.

**Pros**

Focused account-discovery signal; simple CLI; service modules are inspectable.

**Limitations**

May trigger rate limits or notifications; service behavior changes frequently; a hit is not proof of control.

</details>

<a id="h8mail"></a>
<details>
<summary><strong>h8mail</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | h8mail |
| **Description** | Correlates email addresses with locally supplied or authorized breach and intelligence sources. |
| **Category** | Email |
| **Platform** | Linux, macOS, Windows; Python |
| **Repository** | [https://github.com/khast3x/h8mail](https://github.com/khast3x/h8mail) |
| **Official website** | [https://github.com/khast3x/h8mail](https://github.com/khast3x/h8mail) |
| **License** | MIT |
| **Status** | Community |
| **Last verified** | 2026-07-07 |

**Installation**

```text
pipx install h8mail
```

**Quick example**

```text
h8mail -t subject@example.com -q case-001.csv
```

**Supported sources**

Local breach files and configured third-party APIs for which the analyst has lawful access.

**Pros**

Supports local datasets; CSV output; useful for controlled enrichment pipelines.

**Limitations**

Data provenance and legality vary; stale breach data can mislead; API sources require separate credentials and terms review.

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

[Previous: Username](../categories/Username.md) · [Next: Phone](../categories/Phone.md) · [Back to README](../README.md)
