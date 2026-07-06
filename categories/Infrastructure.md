# Infrastructure

[Previous: AI](../categories/AI.md) · [Next: Misc](../categories/Misc.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Authorized exposure mapping and web-service reconnaissance.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Nuclei](#nuclei)
  - [httpx](#httpx)
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

<a id="nuclei"></a>
<details>
<summary><strong>Nuclei</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Nuclei |
| **Description** | Template-based scanner for authorized, reproducible checks against known infrastructure conditions. |
| **Category** | Infrastructure |
| **Platform** | Linux, macOS, Windows; Go; Docker |
| **Repository** | [https://github.com/projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) |
| **Official website** | [https://docs.projectdiscovery.io/tools/nuclei/overview](https://docs.projectdiscovery.io/tools/nuclei/overview) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
```

**Quick example**

```text
nuclei -u https://example.com -severity info -rl 1
```

**Supported sources**

Direct responses from explicitly authorized web and network targets, interpreted through selected templates.

**Pros**

Versioned templates; structured output; rate and scope controls.

**Limitations**

Active scanning can affect systems and trigger alerts; templates can produce false positives or unsafe requests; obtain permission first.

</details>

<a id="httpx"></a>
<details>
<summary><strong>httpx</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | httpx |
| **Description** | Probes authorized HTTP services and records status, titles, technologies, TLS, and response metadata. |
| **Category** | Infrastructure |
| **Platform** | Linux, macOS, Windows; Go; Docker |
| **Repository** | [https://github.com/projectdiscovery/httpx](https://github.com/projectdiscovery/httpx) |
| **Official website** | [https://docs.projectdiscovery.io/tools/httpx/overview](https://docs.projectdiscovery.io/tools/httpx/overview) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

**Quick example**

```text
printf 'https://example.com\n' | httpx -json -title -status-code
```

**Supported sources**

Direct HTTP and TLS responses from analyst-supplied, authorized targets.

**Pros**

Pipeline-friendly; rich JSON output; configurable retries and rates.

**Limitations**

It sends network traffic; technology detection is heuristic; redirects and virtual hosting can create attribution mistakes.

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

[Previous: AI](../categories/AI.md) · [Next: Misc](../categories/Misc.md) · [Back to README](../README.md)
