# Misc

[Previous: Infrastructure](../categories/Infrastructure.md) · [Next: Username](../categories/Username.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Intelligence knowledge platforms and structured relationship management.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [OpenCTI](#opencti)
  - [MISP](#misp)
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

<a id="opencti"></a>
<details>
<summary><strong>OpenCTI</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | OpenCTI |
| **Description** | Open-source platform for structuring, storing, visualizing, and sharing cyber threat intelligence knowledge and observables. |
| **Category** | Misc |
| **Platform** | Docker; Linux server; web application; GraphQL API |
| **Repository** | [https://github.com/OpenCTI-Platform/opencti](https://github.com/OpenCTI-Platform/opencti) |
| **Official website** | [https://opencti.io/](https://opencti.io/) |
| **License** | Apache-2.0 community edition |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Deploy from the official Docker Compose instructions for the selected version.
```

**Quick example**

```text
# Import a STIX bundle and map relationships between observables, reports, intrusion sets, and incidents.
```

**Supported sources**

Analyst-created intelligence objects, STIX data, connectors, reports, observables, and enrichment sources.

**Pros**

Structured relationship model; visual analysis; frequent 2026 releases observed.

**Limitations**

Requires operational security, access control, and data-quality governance; connectors can import unverified data; not a collection shortcut.

</details>

<a id="misp"></a>
<details>
<summary><strong>MISP</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | MISP |
| **Description** | Open-source threat-intelligence sharing platform for storing, correlating, and distributing structured indicators, events, and reports. |
| **Category** | Misc |
| **Platform** | Linux server; Docker; web application; REST API |
| **Repository** | [https://github.com/MISP/MISP](https://github.com/MISP/MISP) |
| **Official website** | [https://www.misp-project.org/](https://www.misp-project.org/) |
| **License** | AGPL-3.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Deploy from the official MISP installation or Docker documentation.
```

**Quick example**

```text
# Create an event, add attributes and objects, then export selected indicators under the appropriate sharing policy.
```

**Supported sources**

Analyst-created events, indicators, objects, sightings, feeds, reports, and synchronized MISP communities.

**Pros**

Mature correlation engine; granular sharing controls; 2026 release activity observed.

**Limitations**

Indicator correlation is not attribution; feeds vary in quality and legal terms; sharing policies must match source restrictions.

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

[Previous: Infrastructure](../categories/Infrastructure.md) · [Next: Username](../categories/Username.md) · [Back to README](../README.md)
