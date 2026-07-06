# Images

[Previous: Social Media](../categories/Social%20Media.md) · [Next: Documents](../categories/Documents.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Metadata inspection, hashing, and visual-evidence triage.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [ExifTool](#exiftool)
  - [ImageHash](#imagehash)
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

<a id="exiftool"></a>
<details>
<summary><strong>ExifTool</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | ExifTool |
| **Description** | Reads, writes, and compares metadata across a wide range of image and media formats. |
| **Category** | Images |
| **Platform** | Linux, macOS, Windows; Perl; standalone packages |
| **Repository** | [https://github.com/exiftool/exiftool](https://github.com/exiftool/exiftool) |
| **Official website** | [https://exiftool.org/](https://exiftool.org/) |
| **License** | Artistic-1.0 or GPL-1.0-or-later |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Debian/Ubuntu
sudo apt install libimage-exiftool-perl
```

**Quick example**

```text
exiftool -G1 -a -s evidence.jpg
```

**Supported sources**

Embedded EXIF, IPTC, XMP, maker-note, filesystem, and container metadata.

**Pros**

Exceptional format coverage; preserves duplicate tags; stable machine-readable output.

**Limitations**

Metadata may be stripped, spoofed, or inherited; never treat a single tag as conclusive location or authorship evidence.

</details>

<a id="imagehash"></a>
<details>
<summary><strong>ImageHash</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | ImageHash |
| **Description** | Python library for perceptual image hashes used to find near-duplicates and transformed variants. |
| **Category** | Images |
| **Platform** | Linux, macOS, Windows; Python |
| **Repository** | [https://github.com/JohannesBuchner/imagehash](https://github.com/JohannesBuchner/imagehash) |
| **Official website** | [https://pypi.org/project/ImageHash/](https://pypi.org/project/ImageHash/) |
| **License** | BSD-2-Clause |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
python -m pip install ImageHash
```

**Quick example**

```text
python -c "from PIL import Image; import imagehash; print(imagehash.phash(Image.open('evidence.jpg')))"
```

**Supported sources**

Local raster images and frames extracted from media.

**Pros**

Fast similarity screening; several hash algorithms; simple integration.

**Limitations**

Hash distance is not semantic proof; crops and heavy edits can evade matching; thresholds require dataset-specific testing.

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

[Previous: Social Media](../categories/Social%20Media.md) · [Next: Documents](../categories/Documents.md) · [Back to README](../README.md)
