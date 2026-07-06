# Steam

[Previous: Discord](../categories/Discord.md) · [Next: Gaming](../categories/Gaming.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Steam identifiers, public profiles, and ecosystem metadata.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [SteamKit](#steamkit)
  - [SteamDB Browser Extension](#steamdb-browser-extension)
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

<a id="steamkit"></a>
<details>
<summary><strong>SteamKit</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | SteamKit |
| **Description** | A .NET library for interacting with the Steam network and public Steam services. |
| **Category** | Steam |
| **Platform** | .NET on Linux, macOS, and Windows |
| **Repository** | [https://github.com/SteamRE/SteamKit](https://github.com/SteamRE/SteamKit) |
| **Official website** | [https://github.com/SteamRE/SteamKit/wiki](https://github.com/SteamRE/SteamKit/wiki) |
| **License** | LGPL-2.1 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
dotnet add package SteamKit2
```

**Quick example**

```text
dotnet new console -n SteamResearch
cd SteamResearch
dotnet add package SteamKit2
```

**Supported sources**

Steam network data exposed to the authenticated client and public Steam endpoints.

**Pros**

Mature protocol implementation; typed .NET API; suitable for repeatable research tooling.

**Limitations**

Requires custom development; authenticated collection must respect Steam rules; public profiles may be incomplete or private.

</details>

<a id="steamdb-browser-extension"></a>
<details>
<summary><strong>SteamDB Browser Extension</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | SteamDB Browser Extension |
| **Description** | Adds SteamDB context and public metadata directly to Steam store and community pages. |
| **Category** | Steam |
| **Platform** | Chromium- and Firefox-based browsers |
| **Repository** | [https://github.com/SteamDatabase/BrowserExtension](https://github.com/SteamDatabase/BrowserExtension) |
| **Official website** | [https://steamdb.info/extension/](https://steamdb.info/extension/) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Install only from the official browser-store links on the project website.
```

**Quick example**

```text
# Open a public Steam store or community page after installation.
```

**Supported sources**

Public Steam pages and SteamDB metadata.

**Pros**

Low-friction context; open-source extension; useful for manual verification.

**Limitations**

Not a bulk collector; SteamDB is an independent service; displayed data can change after capture.

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

[Previous: Discord](../categories/Discord.md) · [Next: Gaming](../categories/Gaming.md) · [Back to README](../README.md)
