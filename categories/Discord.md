# Discord

[Previous: Telegram](../categories/Telegram.md) · [Next: Steam](../categories/Steam.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Authorized export and preservation of accessible Discord content.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [DiscordChatExporter](#discordchatexporter)
  - [Discord History Tracker](#discord-history-tracker)
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

<a id="discordchatexporter"></a>
<details>
<summary><strong>DiscordChatExporter</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | DiscordChatExporter |
| **Description** | Exports channels and direct-message histories that the authenticated account is authorized to access. |
| **Category** | Discord |
| **Platform** | Windows GUI; cross-platform CLI via .NET or Docker |
| **Repository** | [https://github.com/Tyrrrz/DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) |
| **Official website** | [https://github.com/Tyrrrz/DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
docker pull tyrrrz/discordchatexporter:stable
```

**Quick example**

```text
docker run --rm tyrrrz/discordchatexporter:stable --help
```

**Supported sources**

Discord messages, attachments, threads, and channel metadata visible to the authorized account.

**Pros**

Multiple export formats; attachment support; useful for evidence preservation.

**Limitations**

Authentication handling is sensitive; collection may conflict with platform terms; exports contain personal data and require strict access controls.

</details>

<a id="discord-history-tracker"></a>
<details>
<summary><strong>Discord History Tracker</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Discord History Tracker |
| **Description** | Browser-based viewer and tracking utility for preserving accessible Discord message history. |
| **Category** | Discord |
| **Platform** | Modern web browser; desktop viewer |
| **Repository** | [https://github.com/chylex/Discord-History-Tracker](https://github.com/chylex/Discord-History-Tracker) |
| **Official website** | [https://dht.chylex.com/](https://dht.chylex.com/) |
| **License** | MIT |
| **Status** | Community |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Download a release from the repository; verify its checksum before use.
```

**Quick example**

```text
# Follow the upstream browser or desktop instructions for an authorized test server.
```

**Supported sources**

Messages and metadata visible in Discord to the operator.

**Pros**

Local history viewer; searchable archives; transparent source code.

**Limitations**

Browser injection and account-token handling carry risk; platform changes may break capture; use only where collection is authorized.

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

[Previous: Telegram](../categories/Telegram.md) · [Next: Steam](../categories/Steam.md) · [Back to README](../README.md)
