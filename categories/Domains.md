# Domains

[Previous: Documents](../categories/Documents.md) · [Next: IP](../categories/IP.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

DNS, subdomain, certificate, and external-asset discovery.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [OWASP Amass](#owasp-amass)
  - [Subfinder](#subfinder)
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

<a id="owasp-amass"></a>
<details>
<summary><strong>OWASP Amass</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | OWASP Amass |
| **Description** | Performs external asset discovery using DNS, certificates, APIs, and graph-based correlation. |
| **Category** | Domains |
| **Platform** | Linux, macOS, Windows; Go; Docker |
| **Repository** | [https://github.com/owasp-amass/amass](https://github.com/owasp-amass/amass) |
| **Official website** | [https://owasp.org/www-project-amass/](https://owasp.org/www-project-amass/) |
| **License** | Apache-2.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
go install github.com/owasp-amass/amass/v4/...@master
```

**Quick example**

```text
amass enum -passive -d example.com
```

**Supported sources**

DNS, certificate transparency, search APIs, public datasets, and configured data sources.

**Pros**

Strong source fusion; graph model; passive mode supports low-impact discovery.

**Limitations**

Active modes can touch target infrastructure; API keys change coverage; discovered names require DNS and ownership validation.

</details>

<a id="subfinder"></a>
<details>
<summary><strong>Subfinder</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Subfinder |
| **Description** | Discovers valid subdomains from passive online sources with a pipeline-friendly CLI. |
| **Category** | Domains |
| **Platform** | Linux, macOS, Windows; Go; Docker |
| **Repository** | [https://github.com/projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) |
| **Official website** | [https://docs.projectdiscovery.io/tools/subfinder/overview](https://docs.projectdiscovery.io/tools/subfinder/overview) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

**Quick example**

```text
subfinder -silent -d example.com -o subdomains.txt
```

**Supported sources**

Passive APIs, certificate transparency, public datasets, and search services.

**Pros**

Fast; configurable providers; clean text and JSON output.

**Limitations**

Completeness depends on API credentials; wildcard DNS and stale records create noise; authorization is still required for follow-on probing.

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

[Previous: Documents](../categories/Documents.md) · [Next: IP](../categories/IP.md) · [Back to README](../README.md)
