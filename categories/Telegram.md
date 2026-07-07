# Telegram

[Previous: Phone](../categories/Phone.md) · [Next: Discord](../categories/Discord.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Telegram client research and public-channel collection.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [TDLib](#tdlib)
  - [Telegram Phone Number Checker](#telegram-phone-number-checker)
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

<a id="tdlib"></a>
<details>
<summary><strong>TDLib</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | TDLib |
| **Description** | Telegram's cross-platform client library for building controlled collectors and research clients against Telegram data visible to an authenticated account. |
| **Category** | Telegram |
| **Platform** | Linux, macOS, Windows, Android, iOS; C++; JSON interface for other languages |
| **Repository** | [https://github.com/tdlib/td](https://github.com/tdlib/td) |
| **Official website** | [https://core.telegram.org/tdlib](https://core.telegram.org/tdlib) |
| **License** | BSL-1.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Build TDLib from the official repository or use the official build instructions generator.
```

**Quick example**

```text
# Use the td_json interface to collect a bounded public-channel message range.
```

**Supported sources**

Telegram chats, channels, users, messages, media references, and updates visible to the authenticated account through Telegram APIs.

**Pros**

Official Telegram library; documented JSON interface; commit activity observed in 2026.

**Limitations**

Requires custom engineering and Telegram credentials; authenticated collection must respect law and platform rules; access visibility is account-dependent.

</details>

<a id="telegram-phone-number-checker"></a>
<details>
<summary><strong>Telegram Phone Number Checker</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Telegram Phone Number Checker |
| **Description** | Bellingcat utility that checks whether phone numbers are connected to visible Telegram accounts under the operator's contact-discovery settings. |
| **Category** | Telegram |
| **Platform** | Linux, macOS, Windows; Python |
| **Repository** | [https://github.com/bellingcat/telegram-phone-number-checker](https://github.com/bellingcat/telegram-phone-number-checker) |
| **Official website** | [https://github.com/bellingcat/telegram-phone-number-checker](https://github.com/bellingcat/telegram-phone-number-checker) |
| **License** | MIT |
| **Status** | Experimental |
| **Last verified** | 2026-07-07 |

**Installation**

```text
git clone https://github.com/bellingcat/telegram-phone-number-checker.git
cd telegram-phone-number-checker
python -m pip install -r requirements.txt
```

**Quick example**

```text
python telegram-phone-number-checker.py --help
```

**Supported sources**

Telegram contact-discovery results visible to the authenticated research account.

**Pros**

Open implementation; batch-oriented research workflow; produced by an established investigations team.

**Limitations**

Results depend on privacy settings and contacts; bulk use can expose subjects or the research account; review current upstream instructions before use.

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

[Previous: Phone](../categories/Phone.md) · [Next: Discord](../categories/Discord.md) · [Back to README](../README.md)
