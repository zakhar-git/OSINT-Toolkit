# HUMINT

[Previous: SOCMINT](../categories/SOCMINT.md) · [Next: OPSEC](../categories/OPSEC.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Ethical interview support, research notes, and source corroboration.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [SpiderFoot](#spiderfoot)
  - [Joplin](#joplin)
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

<a id="spiderfoot"></a>
<details>
<summary><strong>SpiderFoot</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | SpiderFoot |
| **Description** | Automates open-source collection and entity correlation to prepare and corroborate lawful research leads. |
| **Category** | HUMINT |
| **Platform** | Linux, macOS, Windows; Python; Docker |
| **Repository** | [https://github.com/smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) |
| **Official website** | [https://www.spiderfoot.net/](https://www.spiderfoot.net/) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
docker pull spiderfoot/spiderfoot
```

**Quick example**

```text
docker run -p 5001:5001 spiderfoot/spiderfoot
```

**Supported sources**

Configured public APIs, DNS, web pages, threat-intelligence feeds, and search sources.

**Pros**

Entity graph; modular sources; useful for pre-interview fact checking.

**Limitations**

Automation can amplify incorrect associations; API terms differ; it is not a substitute for consent, source evaluation, or human judgment.

</details>

<a id="joplin"></a>
<details>
<summary><strong>Joplin</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Joplin |
| **Description** | End-to-end encrypted note application suitable for structured interview notes and source logs. |
| **Category** | HUMINT |
| **Platform** | Linux, macOS, Windows, Android, iOS; terminal |
| **Repository** | [https://github.com/laurent22/joplin](https://github.com/laurent22/joplin) |
| **Official website** | [https://joplinapp.org/](https://joplinapp.org/) |
| **License** | AGPL-3.0-or-later |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Install a signed release from the official website or platform store.
```

**Quick example**

```text
# Create a case notebook with separate source, claim, and verification notes.
```

**Supported sources**

Analyst-authored notes, attachments, web clips, and imported Markdown.

**Pros**

Local-first; encryption support; Markdown export helps case portability.

**Limitations**

Encryption does not replace endpoint security; interview records may be highly sensitive; access, retention, and consent rules must be defined first.

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

[Previous: SOCMINT](../categories/SOCMINT.md) · [Next: OPSEC](../categories/OPSEC.md) · [Back to README](../README.md)
