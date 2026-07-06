# Domain Investigation

[Previous: Image Investigation](../workflows/Image%20Investigation.md) · [Next: Infrastructure Investigation](../workflows/Infrastructure%20Investigation.md) · [Back to README](../README.md)

> [!IMPORTANT]
> Use this workflow only for a legitimate, documented purpose. Public availability does not remove privacy, contractual, or data-protection obligations.

## Table of contents

<!-- toc:start -->
- [Outcome](#outcome)
- [Before collection](#before-collection)
- [1. Canonicalize scope](#1-canonicalize-scope)
- [2. Collect passive DNS context](#2-collect-passive-dns-context)
- [3. Enumerate names](#3-enumerate-names)
- [4. Inspect web history](#4-inspect-web-history)
- [5. Map dependencies](#5-map-dependencies)
- [6. Validate ownership claims](#6-validate-ownership-claims)
- [7. Package evidence](#7-package-evidence)
- [Evidence package](#evidence-package)
- [Stop conditions](#stop-conditions)
<!-- toc:end -->

## Outcome

Produce a reproducible, source-grounded case record that separates observations from inferences and contains only information necessary to answer the stated question.

## Before collection

| Control | Required record |
| --- | --- |
| Purpose | One-sentence research question and intended user of the result |
| Authority | Consent, policy, contract, or legal basis |
| Scope | Included identifiers, sources, dates, and explicit exclusions |
| Safety | Account, device, network, and sensitive-data handling plan |
| Retention | Storage location, access list, review date, and deletion rule |

## 1. Canonicalize scope

Record the registrable domain, IDNA form, wildcard behavior, authorized boundaries, and investigation time window.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 2. Collect passive DNS context

Query current DNS, certificate transparency, passive sources, and web archives before any active probing.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 3. Enumerate names

Use at least two passive subdomain sources, deduplicate, resolve, and flag wildcard-derived results.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 4. Inspect web history

Review archived pages, redirects, favicons, analytics identifiers, and public documents. Preserve dates because ownership and content change.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 5. Map dependencies

Identify mail, CDN, hosting, nameserver, certificate, and third-party service relationships without assuming common ownership.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 6. Validate ownership claims

Corroborate with official sites, public filings, DNS control evidence, or signed statements; shared infrastructure is weak evidence.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 7. Package evidence

Export DNS answers with TTL and timestamp, certificate records, screenshots, raw tool output, and a scope statement.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## Evidence package

Create a case directory with a read-only original, working copies, exports, screenshots, and a research log. Hash acquired files with SHA-256. Record tool name, version, configuration, time zone, errors, and any transformations. Cite the primary source for each factual claim and label analytical confidence.

## Stop conditions

Stop collection when authorization is unclear, a source signals access restrictions, the subject could be notified or harmed unexpectedly, the tool leaves scope, or the question is answered. Escalate sensitive findings through the approved reporting channel; do not publish credentials, private communications, precise home locations, or unrelated personal data.

---

[Previous: Image Investigation](../workflows/Image%20Investigation.md) · [Next: Infrastructure Investigation](../workflows/Infrastructure%20Investigation.md) · [Back to README](../README.md)
