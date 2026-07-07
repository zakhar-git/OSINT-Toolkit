# OPSEC

[Previous: HUMINT](../categories/HUMINT.md) · [Next: AI](../categories/AI.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Researcher compartmentation, transport privacy, and data protection.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Tor](#tor)
  - [VeraCrypt](#veracrypt)
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

<a id="tor"></a>
<details>
<summary><strong>Tor</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Tor |
| **Description** | An anonymity network and client for separating research traffic from ordinary network identity. |
| **Category** | OPSEC |
| **Platform** | Linux, macOS, Windows, Android |
| **Repository** | [https://gitlab.torproject.org/tpo/core/tor](https://gitlab.torproject.org/tpo/core/tor) |
| **Official website** | [https://support.torproject.org/](https://support.torproject.org/) |
| **License** | BSD-3-Clause |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Prefer Tor Browser from the official website and verify its signature.
```

**Quick example**

```text
# Confirm the connection only through the Tor Project check page.
```

**Supported sources**

Network transport; Tor does not itself provide OSINT data sources.

**Pros**

Separates destination traffic from the origin IP; mature threat documentation; open source.

**Limitations**

Does not provide complete anonymity; browser behavior, logins, downloads, and endpoint compromise can deanonymize a researcher.

</details>

<a id="veracrypt"></a>
<details>
<summary><strong>VeraCrypt</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | VeraCrypt |
| **Description** | Creates encrypted volumes for protecting case material at rest. |
| **Category** | OPSEC |
| **Platform** | Linux, macOS, Windows |
| **Repository** | [https://github.com/veracrypt/VeraCrypt](https://github.com/veracrypt/VeraCrypt) |
| **Official website** | [https://www.veracrypt.fr/](https://www.veracrypt.fr/) |
| **License** | Apache-2.0 and TrueCrypt License 3.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Download a signed release from the official website and verify it.
```

**Quick example**

```text
veracrypt --text --create case-container.hc
```

**Supported sources**

Local files and block devices selected by the investigator.

**Pros**

Strong at-rest encryption; cross-platform volumes; supports keyfiles and hidden volumes.

**Limitations**

Mounted data is exposed to the endpoint; forgotten credentials are unrecoverable; local law and organizational key-management rules apply.

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

[Previous: HUMINT](../categories/HUMINT.md) · [Next: AI](../categories/AI.md) · [Back to README](../README.md)
