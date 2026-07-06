# Username Investigation

[Previous: Person Investigation](../workflows/Person%20Investigation.md) · [Next: Telegram Investigation](../workflows/Telegram%20Investigation.md) · [Back to README](../README.md)

> [!IMPORTANT]
> Use this workflow only for a legitimate, documented purpose. Public availability does not remove privacy, contractual, or data-protection obligations.

## Table of contents

<!-- toc:start -->
- [Outcome](#outcome)
- [Before collection](#before-collection)
- [1. Define the identifier](#1-define-the-identifier)
- [2. Search across services](#2-search-across-services)
- [3. Check historical presence](#3-check-historical-presence)
- [4. Compare visual signals](#4-compare-visual-signals)
- [5. Cross-reference attributes](#5-cross-reference-attributes)
- [6. Map relationships](#6-map-relationships)
- [7. Document and preserve](#7-document-and-preserve)
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

## 1. Define the identifier

Record exact spelling, capitalization, separators, observed URL, collection time, and the source that exposed the handle.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 2. Search across services

Run two independent username tools, then manually validate high-value results. Treat display-name matches separately from exact handles.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 3. Check historical presence

Review lawful web archives and cached search results. Record capture dates; do not imply that an archived profile is still controlled by the same person.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 4. Compare visual signals

Compare avatars with perceptual hashes and manual inspection. Note reused crops, backgrounds, and upload timing without treating similarity as identity proof.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 5. Cross-reference attributes

Compare self-disclosed names, locations, links, writing patterns, and activity windows. Require at least two independent signals for an identity hypothesis.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 6. Map relationships

Record public interactions only when they materially support the question. Avoid bulk collection of unrelated contacts.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 7. Document and preserve

Save URLs, timestamps, screenshots, raw exports, tool versions, and hashes. Separate observations from analytical judgments.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## Evidence package

Create a case directory with a read-only original, working copies, exports, screenshots, and a research log. Hash acquired files with SHA-256. Record tool name, version, configuration, time zone, errors, and any transformations. Cite the primary source for each factual claim and label analytical confidence.

## Stop conditions

Stop collection when authorization is unclear, a source signals access restrictions, the subject could be notified or harmed unexpectedly, the tool leaves scope, or the question is answered. Escalate sensitive findings through the approved reporting channel; do not publish credentials, private communications, precise home locations, or unrelated personal data.

---

[Previous: Person Investigation](../workflows/Person%20Investigation.md) · [Next: Telegram Investigation](../workflows/Telegram%20Investigation.md) · [Back to README](../README.md)
