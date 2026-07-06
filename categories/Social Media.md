# Social Media

[Previous: Gaming](../categories/Gaming.md) · [Next: Images](../categories/Images.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Collection and analysis of public social-platform content.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Instaloader](#instaloader)
  - [twscrape](#twscrape)
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

<a id="instaloader"></a>
<details>
<summary><strong>Instaloader</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Instaloader |
| **Description** | Downloads accessible Instagram posts, profiles, metadata, and comments for reproducible research. |
| **Category** | Social Media |
| **Platform** | Linux, macOS, Windows; Python |
| **Repository** | [https://github.com/instaloader/instaloader](https://github.com/instaloader/instaloader) |
| **Official website** | [https://instaloader.github.io/](https://instaloader.github.io/) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
pipx install instaloader
```

**Quick example**

```text
instaloader --no-videos --no-compress-json public_profile
```

**Supported sources**

Public Instagram profiles and content accessible to the operator's session.

**Pros**

Metadata-rich output; resumable downloads; filename controls aid evidence handling.

**Limitations**

Instagram changes and rate limits cause breakage; authentication raises account risk; private content requires legitimate access.

</details>

<a id="twscrape"></a>
<details>
<summary><strong>twscrape</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | twscrape |
| **Description** | Python library and CLI for collecting publicly accessible X/Twitter search, user, and timeline results. |
| **Category** | Social Media |
| **Platform** | Linux, macOS, Windows; Python |
| **Repository** | [https://github.com/vladkens/twscrape](https://github.com/vladkens/twscrape) |
| **Official website** | [https://github.com/vladkens/twscrape](https://github.com/vladkens/twscrape) |
| **License** | MIT |
| **Status** | Community |
| **Last verified** | 2026-07-07 |

**Installation**

```text
python -m pip install twscrape
```

**Quick example**

```text
twscrape search 'from:example since:2026-01-01' --limit 20
```

**Supported sources**

Publicly accessible X/Twitter web and API responses available to configured accounts.

**Pros**

Structured output; asynchronous collection; useful search primitives.

**Limitations**

Requires account configuration; platform enforcement and schema changes are frequent; comply with terms and minimize collection.

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

[Previous: Gaming](../categories/Gaming.md) · [Next: Images](../categories/Images.md) · [Back to README](../README.md)
