# IP

[Previous: Domains](../categories/Domains.md) · [Next: GEOINT](../categories/GEOINT.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Network attribution context and authorized service discovery.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Nmap](#nmap)
  - [ZMap](#zmap)
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

<a id="nmap"></a>
<details>
<summary><strong>Nmap</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Nmap |
| **Description** | Network mapper for authorized host discovery, service identification, and carefully scoped enumeration. |
| **Category** | IP |
| **Platform** | Linux, macOS, Windows |
| **Repository** | [https://github.com/nmap/nmap](https://github.com/nmap/nmap) |
| **Official website** | [https://nmap.org/](https://nmap.org/) |
| **License** | Nmap Public Source License |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Debian/Ubuntu
sudo apt install nmap
```

**Quick example**

```text
nmap -sV --version-light 192.0.2.10
```

**Supported sources**

Direct network responses from explicitly authorized hosts and services.

**Pros**

Mature service detection; XML output; extensive documentation.

**Limitations**

Active scanning is observable and may be unlawful without permission; detection is probabilistic; use documentation-reserved addresses in examples.

</details>

<a id="zmap"></a>
<details>
<summary><strong>ZMap</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | ZMap |
| **Description** | High-speed internet scanner designed for controlled research with explicit scope and rate governance. |
| **Category** | IP |
| **Platform** | Linux, macOS, BSD |
| **Repository** | [https://github.com/zmap/zmap](https://github.com/zmap/zmap) |
| **Official website** | [https://zmap.io/](https://zmap.io/) |
| **License** | Apache-2.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Debian/Ubuntu
sudo apt install zmap
```

**Quick example**

```text
zmap --dryrun -p 443 192.0.2.0/24
```

**Supported sources**

Direct responses to researcher-defined network probes.

**Pros**

Reproducible high-volume methodology; denylist support; structured output.

**Limitations**

Internet-scale use has substantial legal, ethical, and operational risk; never run without authorization, exclusions, rate controls, and abuse handling.

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

[Previous: Domains](../categories/Domains.md) · [Next: GEOINT](../categories/GEOINT.md) · [Back to README](../README.md)
