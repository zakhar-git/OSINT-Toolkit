# Infrastructure Investigation

[Previous: Domain Investigation](../workflows/Domain%20Investigation.md) · [Next: Company Investigation](../workflows/Company%20Investigation.md) · [Back to README](../README.md)

> [!IMPORTANT]
> Use this workflow only for a legitimate, documented purpose. Public availability does not remove privacy, contractual, or data-protection obligations.

## Table of contents

<!-- toc:start -->
- [Outcome](#outcome)
- [Before collection](#before-collection)
- [1. Obtain authorization](#1-obtain-authorization)
- [2. Establish passive inventory](#2-establish-passive-inventory)
- [3. Resolve and classify](#3-resolve-and-classify)
- [4. Probe conservatively](#4-probe-conservatively)
- [5. Validate findings](#5-validate-findings)
- [6. Assess change over time](#6-assess-change-over-time)
- [7. Report responsibly](#7-report-responsibly)
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

## 1. Obtain authorization

Define targets, ports, dates, rate limits, excluded systems, data handling, and an abuse contact before sending traffic.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 2. Establish passive inventory

Collect DNS, certificates, routing, public cloud references, and known hostnames. Track source and observation time.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 3. Resolve and classify

Resolve hostnames, account for CDNs and shared hosting, and separate owned systems from third-party dependencies.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 4. Probe conservatively

Start with low-rate HTTP and service identification. Use explicit input lists and stop on instability or scope ambiguity.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 5. Validate findings

Reproduce important observations manually, capture raw responses, and distinguish a technology hint from a confirmed exposure.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 6. Assess change over time

Compare current results with authorized prior snapshots while accounting for dynamic addresses and ephemeral cloud assets.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 7. Report responsibly

Provide evidence, affected asset, timestamp, severity rationale, reproduction limits, and remediation channel; never publish exploitable details prematurely.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## Evidence package

Create a case directory with a read-only original, working copies, exports, screenshots, and a research log. Hash acquired files with SHA-256. Record tool name, version, configuration, time zone, errors, and any transformations. Cite the primary source for each factual claim and label analytical confidence.

## Stop conditions

Stop collection when authorization is unclear, a source signals access restrictions, the subject could be notified or harmed unexpectedly, the tool leaves scope, or the question is answered. Escalate sensitive findings through the approved reporting channel; do not publish credentials, private communications, precise home locations, or unrelated personal data.

---

[Previous: Domain Investigation](../workflows/Domain%20Investigation.md) · [Next: Company Investigation](../workflows/Company%20Investigation.md) · [Back to README](../README.md)
