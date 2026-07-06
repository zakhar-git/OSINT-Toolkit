# Email Investigation

[Previous: Telegram Investigation](../workflows/Telegram%20Investigation.md) · [Next: Phone Investigation](../workflows/Phone%20Investigation.md) · [Back to README](../README.md)

> [!IMPORTANT]
> Use this workflow only for a legitimate, documented purpose. Public availability does not remove privacy, contractual, or data-protection obligations.

## Table of contents

<!-- toc:start -->
- [Outcome](#outcome)
- [Before collection](#before-collection)
- [1. Normalize the address](#1-normalize-the-address)
- [2. Validate infrastructure](#2-validate-infrastructure)
- [3. Discover public exposure](#3-discover-public-exposure)
- [4. Inspect message evidence](#4-inspect-message-evidence)
- [5. Correlate identities](#5-correlate-identities)
- [6. Assess risk](#6-assess-risk)
- [7. Report minimally](#7-report-minimally)
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

## 1. Normalize the address

Preserve the original string, normalize the domain conservatively, check for aliases, and avoid provider-specific transformations unless documented.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 2. Validate infrastructure

Inspect domain registration context, MX records, SPF, DKIM selectors when known, and DMARC. Do not send probing mail without authorization.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 3. Discover public exposure

Search exact-address variants, public documents, commits, account-recovery signals, and lawful breach sources. Record query and source dates.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 4. Inspect message evidence

When a message is provided, preserve it in RFC 5322 form and analyze the full header chain, authentication results, attachments, and URLs in isolation.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 5. Correlate identities

Compare usernames, public profiles, organization references, and historical documents. An address alone is not reliable proof of a current owner.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 6. Assess risk

Classify confirmed compromise exposure separately from spam reputation, spoofing, or mere appearance in an old dataset.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 7. Report minimally

Redact unnecessary personal data and breach content. Cite public sources, uncertainty, and lawful-access basis.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## Evidence package

Create a case directory with a read-only original, working copies, exports, screenshots, and a research log. Hash acquired files with SHA-256. Record tool name, version, configuration, time zone, errors, and any transformations. Cite the primary source for each factual claim and label analytical confidence.

## Stop conditions

Stop collection when authorization is unclear, a source signals access restrictions, the subject could be notified or harmed unexpectedly, the tool leaves scope, or the question is answered. Escalate sensitive findings through the approved reporting channel; do not publish credentials, private communications, precise home locations, or unrelated personal data.

---

[Previous: Telegram Investigation](../workflows/Telegram%20Investigation.md) · [Next: Phone Investigation](../workflows/Phone%20Investigation.md) · [Back to README](../README.md)
