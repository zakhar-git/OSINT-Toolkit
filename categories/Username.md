# Username

[Previous: Misc](../categories/Misc.md) · [Next: Email](../categories/Email.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Username discovery and identity correlation across public services.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Sherlock](#sherlock)
  - [Maigret](#maigret)
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

<a id="sherlock"></a>
<details>
<summary><strong>Sherlock</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Sherlock |
| **Description** | Checks a username across a large catalog of social networks and public services. |
| **Category** | Username |
| **Platform** | Linux, macOS, Windows; Python; Docker |
| **Repository** | [https://github.com/sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) |
| **Official website** | [https://sherlockproject.xyz/](https://sherlockproject.xyz/) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
pipx install sherlock-project
```

**Quick example**

```text
sherlock --print-found --csv analyst_handle
```

**Supported sources**

Public profile URLs on supported websites.

**Pros**

Broad site coverage; machine-readable output; active test ecosystem.

**Limitations**

False positives remain possible; rate limits and site changes affect results; existence does not establish ownership.

</details>

<a id="maigret"></a>
<details>
<summary><strong>Maigret</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Maigret |
| **Description** | Searches usernames across sites and produces structured reports with profile-derived identifiers. |
| **Category** | Username |
| **Platform** | Linux, macOS, Windows; Python; Docker |
| **Repository** | [https://github.com/soxoj/maigret](https://github.com/soxoj/maigret) |
| **Official website** | [https://maigret.readthedocs.io/](https://maigret.readthedocs.io/) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
pipx install maigret
```

**Quick example**

```text
maigret analyst_handle --json simple
```

**Supported sources**

Public profiles, username pages, and identifiers exposed by supported sites.

**Pros**

Multiple report formats; recursive identifier extraction; configurable site database.

**Limitations**

Large scans create noise; some targets require cookies or regional access; matches need manual validation.

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

[Previous: Misc](../categories/Misc.md) · [Next: Email](../categories/Email.md) · [Back to README](../README.md)
