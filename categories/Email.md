# Email

[Previous: Username](../categories/Username.md) · [Next: Phone](../categories/Phone.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Email account context, breach exposure, and account-linked public artifacts.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [GHunt](#ghunt)
  - [Have I Been Pwned API](#have-i-been-pwned-api)
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

<a id="ghunt"></a>
<details>
<summary><strong>GHunt</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | GHunt |
| **Description** | Collects public Google account artifacts and Google-service signals for a known identifier when the analyst has a lawful reason to test that pivot. |
| **Category** | Email |
| **Platform** | Linux, macOS, Windows; Python; Docker |
| **Repository** | [https://github.com/mxrch/GHunt](https://github.com/mxrch/GHunt) |
| **Official website** | [https://github.com/mxrch/GHunt](https://github.com/mxrch/GHunt) |
| **License** | AGPL-3.0 |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
pipx install ghunt
```

**Quick example**

```text
ghunt email subject@example.com
```

**Supported sources**

Public Google account surfaces, Google Maps contribution signals, and metadata visible through supported Google services.

**Pros**

Focused Google ecosystem pivoting; structured modules; active repository activity observed in 2026.

**Limitations**

Requires authenticated setup; Google changes can break modules; a visible Google artifact is not proof that the subject still controls the account.

</details>

<a id="have-i-been-pwned-api"></a>
<details>
<summary><strong>Have I Been Pwned API</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Have I Been Pwned API |
| **Description** | Official breach-exposure API for checking whether an email address or verified domain appears in indexed breach data. |
| **Category** | Email |
| **Platform** | REST API; MCP server; any HTTP client |
| **Repository** | Not publicly published by vendor. |
| **Official website** | [https://haveibeenpwned.com/API/v3](https://haveibeenpwned.com/API/v3) |
| **License** | Proprietary API terms |
| **Status** | Active |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Obtain an API key from the official HIBP dashboard when authorized.
```

**Quick example**

```text
HIBP_API_URL="[official API base URL]"
curl -H "hibp-api-key: $HIBP_API_KEY" -H "user-agent: osint-toolkit-research" "$HIBP_API_URL/breachedaccount/account-exists%40hibp-integration-tests.com"
```

**Supported sources**

HIBP breach, paste, stealer-log, domain, and Pwned Passwords endpoints available under the selected plan.

**Pros**

Official documented API; supports privacy-preserving hash-range email searches; domain search requires control verification.

**Limitations**

Direct email queries disclose the address to HIBP; most email/domain endpoints require subscription and strict acceptable-use compliance; breach presence is exposure evidence, not attribution.

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

[Previous: Username](../categories/Username.md) · [Next: Phone](../categories/Phone.md) · [Back to README](../README.md)
