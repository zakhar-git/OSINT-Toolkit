# HUMINT

[Previous: SOCMINT](../categories/SOCMINT.md) · [Next: OPSEC](../categories/OPSEC.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Source management, interview notes, citations, and corroboration records.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Zotero](#zotero)
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

<a id="zotero"></a>
<details>
<summary><strong>Zotero</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Zotero |
| **Description** | Reference manager for preserving citations, source snapshots, annotations, and bibliographies for investigative records. |
| **Category** | HUMINT |
| **Platform** | Linux, macOS, Windows; browser connectors; web library |
| **Repository** | [https://github.com/zotero/zotero](https://github.com/zotero/zotero) |
| **Official website** | [https://www.zotero.org/](https://www.zotero.org/) |
| **License** | AGPL-3.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Install the signed desktop app and browser connector from the official website.
```

**Quick example**

```text
# Save first-party source pages, attach PDFs, and export a case bibliography.
```

**Supported sources**

Analyst-supplied web pages, documents, metadata records, annotations, and citation exports.

**Pros**

Research-focused citation model; browser capture; active repository activity observed in 2026.

**Limitations**

It preserves references, not truth; cloud sync and group libraries require access controls; private-source notes need separate consent and retention rules.

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
