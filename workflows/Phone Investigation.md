# Phone Investigation

[Previous: Email Investigation](../workflows/Email%20Investigation.md) · [Next: Image Investigation](../workflows/Image%20Investigation.md) · [Back to README](../README.md)

> [!IMPORTANT]
> Use this workflow only for a legitimate, documented purpose. Public availability does not remove privacy, contractual, or data-protection obligations.

## Table of contents

<!-- toc:start -->
- [Outcome](#outcome)
- [Before collection](#before-collection)
- [1. Normalize the number](#1-normalize-the-number)
- [2. Check numbering context](#2-check-numbering-context)
- [3. Search public references](#3-search-public-references)
- [4. Review messaging visibility](#4-review-messaging-visibility)
- [5. Correlate cautiously](#5-correlate-cautiously)
- [6. Check temporal validity](#6-check-temporal-validity)
- [7. Preserve and redact](#7-preserve-and-redact)
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

## 1. Normalize the number

Convert to E.164 with the correct region assumption. Preserve the submitted format and document any inferred country code.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 2. Check numbering context

Determine structural validity, country, possible type, and numbering-plan context. Do not equate validity with assignment.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 3. Search public references

Search quoted international and national formats, public business listings, documents, and self-published profiles.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 4. Review messaging visibility

Use only ordinary contact-discovery behavior that is lawful and visible to the research account. Avoid invasive enumeration or notification-generating checks.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 5. Correlate cautiously

Compare names, avatars, business records, usernames, and timestamps. Recycled numbers make historical matches especially fragile.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 6. Check temporal validity

Record when each association was observed and whether the source describes a historical or current contact.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 7. Preserve and redact

Store the canonical number in restricted case notes and redact it from broad reports unless essential.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## Evidence package

Create a case directory with a read-only original, working copies, exports, screenshots, and a research log. Hash acquired files with SHA-256. Record tool name, version, configuration, time zone, errors, and any transformations. Cite the primary source for each factual claim and label analytical confidence.

## Stop conditions

Stop collection when authorization is unclear, a source signals access restrictions, the subject could be notified or harmed unexpectedly, the tool leaves scope, or the question is answered. Escalate sensitive findings through the approved reporting channel; do not publish credentials, private communications, precise home locations, or unrelated personal data.

---

[Previous: Email Investigation](../workflows/Email%20Investigation.md) · [Next: Image Investigation](../workflows/Image%20Investigation.md) · [Back to README](../README.md)
