# GEOINT

[Previous: IP](../categories/IP.md) · [Next: SOCMINT](../categories/SOCMINT.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Geospatial analysis, map data, and location corroboration.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [QGIS](#qgis)
  - [Overpass Turbo](#overpass-turbo)
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

<a id="qgis"></a>
<details>
<summary><strong>QGIS</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | QGIS |
| **Description** | Desktop geographic information system for layering, transforming, and analyzing geospatial evidence. |
| **Category** | GEOINT |
| **Platform** | Linux, macOS, Windows |
| **Repository** | [https://github.com/qgis/QGIS](https://github.com/qgis/QGIS) |
| **Official website** | [https://qgis.org/](https://qgis.org/) |
| **License** | GPL-2.0-or-later |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Debian/Ubuntu
sudo apt install qgis
```

**Quick example**

```text
qgis evidence-locations.geojson
```

**Supported sources**

GeoJSON, KML, raster imagery, vector layers, databases, and web map services.

**Pros**

Powerful spatial analysis; broad format support; reproducible projects and styles.

**Limitations**

Source accuracy and licensing vary; projections can distort results; project files should preserve source and transformation notes.

</details>

<a id="overpass-turbo"></a>
<details>
<summary><strong>Overpass Turbo</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Overpass Turbo |
| **Description** | Interactive web interface for querying and visualizing OpenStreetMap data through the Overpass API. |
| **Category** | GEOINT |
| **Platform** | Web; JavaScript |
| **Repository** | [https://github.com/tyrasd/overpass-turbo](https://github.com/tyrasd/overpass-turbo) |
| **Official website** | [https://overpass-turbo.eu/](https://overpass-turbo.eu/) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# No installation is required for the hosted interface.
```

**Quick example**

```text
[out:json];node[amenity=pharmacy](around:500,51.5074,-0.1278);out;
```

**Supported sources**

OpenStreetMap nodes, ways, relations, tags, and geometry available through Overpass.

**Pros**

Fast query prototyping; map visualization; export to common geospatial formats.

**Limitations**

OpenStreetMap is community-maintained and uneven; public instances enforce limits; timestamps reflect map edits, not necessarily real-world events.

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

[Previous: IP](../categories/IP.md) · [Next: SOCMINT](../categories/SOCMINT.md) · [Back to README](../README.md)
