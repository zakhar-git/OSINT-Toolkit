# Documents

[Previous: Images](../categories/Images.md) · [Next: Domains](../categories/Domains.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Document metadata, embedded-object, and sanitization analysis.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [oletools](#oletools)
  - [MAT2](#mat2)
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

<a id="oletools"></a>
<details>
<summary><strong>oletools</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | oletools |
| **Description** | Analyzes Microsoft Office and OLE files for metadata, macros, embedded objects, and suspicious structures. |
| **Category** | Documents |
| **Platform** | Linux, macOS, Windows; Python |
| **Repository** | [https://github.com/decalage2/oletools](https://github.com/decalage2/oletools) |
| **Official website** | [https://github.com/decalage2/oletools/wiki](https://github.com/decalage2/oletools/wiki) |
| **License** | BSD-2-Clause |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
pipx install oletools
```

**Quick example**

```text
oleid evidence.docx
olevba evidence.docm
```

**Supported sources**

OLE, OOXML, RTF, macro, property, and embedded-object structures.

**Pros**

Purpose-built analyzers; readable reports; strong triage value.

**Limitations**

Potentially malicious documents need isolated handling; findings require interpretation; does not safely render document content.

</details>

<a id="mat2"></a>
<details>
<summary><strong>MAT2</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | MAT2 |
| **Description** | Inspects and removes metadata from common file formats while exposing what was found. |
| **Category** | Documents |
| **Platform** | Linux; Python |
| **Repository** | [https://0xacab.org/jvoisin/mat2](https://0xacab.org/jvoisin/mat2) |
| **Official website** | [https://0xacab.org/jvoisin/mat2](https://0xacab.org/jvoisin/mat2) |
| **License** | LGPL-3.0-or-later |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Debian/Ubuntu
sudo apt install mat2
```

**Quick example**

```text
mat2 --show evidence.pdf
```

**Supported sources**

Metadata in supported documents, images, audio, archives, and office formats.

**Pros**

Clear inspection mode; supports sanitized copies; integrates with desktop workflows.

**Limitations**

Sanitization can change files and signatures; preserve an original first; not every proprietary metadata field is supported.

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

[Previous: Images](../categories/Images.md) · [Next: Domains](../categories/Domains.md) · [Back to README](../README.md)
