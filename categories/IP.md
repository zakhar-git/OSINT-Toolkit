# IP

[Previous: Domains](../categories/Domains.md) · [Next: GEOINT](../categories/GEOINT.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

IP geolocation, ASN context, routing, and authorized service discovery.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Nmap](#nmap)
  - [IPinfo CLI](#ipinfo-cli)
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

<a id="ipinfo-cli"></a>
<details>
<summary><strong>IPinfo CLI</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | IPinfo CLI |
| **Description** | Official command-line client for IPinfo's IP, ASN, geolocation, hosting, privacy, and bulk enrichment API data. |
| **Category** | IP |
| **Platform** | Linux, macOS, Windows, BSD, Solaris; Go; Docker |
| **Repository** | [https://github.com/ipinfo/cli](https://github.com/ipinfo/cli) |
| **Official website** | [https://ipinfo.io/](https://ipinfo.io/) |
| **License** | Apache-2.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
go install github.com/ipinfo/cli/ipinfo@latest
```

**Quick example**

```text
ipinfo 8.8.8.8
```

**Supported sources**

IPinfo API datasets, analyst-supplied IPs, CIDR ranges, ASN lookups, and local IP lists.

**Pros**

Official vendor CLI; supports single and bulk lookup workflows; recent release observed in 2026.

**Limitations**

Data depth depends on the API plan and token; geolocation is approximate; IP ownership, hosting, and user attribution are separate questions.

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
