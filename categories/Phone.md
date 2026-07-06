# Phone

[Previous: Email](../categories/Email.md) · [Next: Telegram](../categories/Telegram.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Number parsing, carrier context, and public footprint discovery.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [PhoneInfoga](#phoneinfoga)
  - [libphonenumber](#libphonenumber)
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

<a id="phoneinfoga"></a>
<details>
<summary><strong>PhoneInfoga</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | PhoneInfoga |
| **Description** | Performs phone-number parsing and open-web reconnaissance without claiming subscriber identification. |
| **Category** | Phone |
| **Platform** | Linux, macOS, Windows; Go binary; Docker |
| **Repository** | [https://github.com/sundowndev/phoneinfoga](https://github.com/sundowndev/phoneinfoga) |
| **Official website** | [https://sundowndev.github.io/phoneinfoga/](https://sundowndev.github.io/phoneinfoga/) |
| **License** | GPL-3.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
docker pull sundowndev/phoneinfoga:latest
```

**Quick example**

```text
docker run --rm sundowndev/phoneinfoga scan -n '+12025550123'
```

**Supported sources**

Numbering-plan metadata and generated public-web search pivots.

**Pros**

Normalizes international numbers; reproducible CLI; does not depend on a private subscriber database.

**Limitations**

Cannot prove a person's ownership; search results can be stale; use a reserved example number in demonstrations.

</details>

<a id="libphonenumber"></a>
<details>
<summary><strong>libphonenumber</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | libphonenumber |
| **Description** | Google's library for parsing, formatting, and validating international phone-number structures. |
| **Category** | Phone |
| **Platform** | Java, C++, JavaScript; community ports for other languages |
| **Repository** | [https://github.com/google/libphonenumber](https://github.com/google/libphonenumber) |
| **Official website** | [https://github.com/google/libphonenumber](https://github.com/google/libphonenumber) |
| **License** | Apache-2.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# JavaScript port
npm install google-libphonenumber
```

**Quick example**

```text
node -e "const p=require('google-libphonenumber').PhoneNumberUtil.getInstance(); console.log(p.parse('+12025550123'))"
```

**Supported sources**

International numbering plans and metadata distributed with the library.

**Pros**

Mature normalization logic; multi-language support; useful before querying other sources.

**Limitations**

Validity means structurally possible, not assigned or owned; metadata may lag numbering-plan changes.

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

[Previous: Email](../categories/Email.md) · [Next: Telegram](../categories/Telegram.md) · [Back to README](../README.md)
