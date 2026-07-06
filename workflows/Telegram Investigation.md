# Telegram Investigation

[Previous: Username Investigation](../workflows/Username%20Investigation.md) · [Next: Email Investigation](../workflows/Email%20Investigation.md) · [Back to README](../README.md)

> [!IMPORTANT]
> Use this workflow only for a legitimate, documented purpose. Public availability does not remove privacy, contractual, or data-protection obligations.

## Table of contents

<!-- toc:start -->
- [Outcome](#outcome)
- [Before collection](#before-collection)
- [1. Set scope and account safety](#1-set-scope-and-account-safety)
- [2. Resolve entities](#2-resolve-entities)
- [3. Collect public content](#3-collect-public-content)
- [4. Trace provenance](#4-trace-provenance)
- [5. Analyze media and location](#5-analyze-media-and-location)
- [6. Assess networks](#6-assess-networks)
- [7. Preserve evidence](#7-preserve-evidence)
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

## 1. Set scope and account safety

Define whether the target is a public channel, group, message, or visible account. Use a dedicated research account and document platform and legal constraints.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 2. Resolve entities

Record canonical usernames, numeric IDs when lawfully available, invite links, display names, and entity type. Expect usernames and titles to change.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 3. Collect public content

Use an authorized API client for bounded date ranges. Preserve message IDs, timestamps, forwards, edits, media references, and reply relationships.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 4. Trace provenance

Follow forward headers and cited links to the earliest accessible source. Distinguish original publication from redistribution.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 5. Analyze media and location

Hash media, inspect metadata safely, compare frames, and test geographic claims against independent map or imagery evidence.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 6. Assess networks

Map channels, administrators only when public, mentions, forwards, and shared links. Do not infer coordination from a single overlap.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 7. Preserve evidence

Export raw API records, media hashes, collection code, account context, and UTC timestamps. Note deletions or inaccessible items without attempting unauthorized recovery.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## Evidence package

Create a case directory with a read-only original, working copies, exports, screenshots, and a research log. Hash acquired files with SHA-256. Record tool name, version, configuration, time zone, errors, and any transformations. Cite the primary source for each factual claim and label analytical confidence.

## Stop conditions

Stop collection when authorization is unclear, a source signals access restrictions, the subject could be notified or harmed unexpectedly, the tool leaves scope, or the question is answered. Escalate sensitive findings through the approved reporting channel; do not publish credentials, private communications, precise home locations, or unrelated personal data.

---

[Previous: Username Investigation](../workflows/Username%20Investigation.md) · [Next: Email Investigation](../workflows/Email%20Investigation.md) · [Back to README](../README.md)
