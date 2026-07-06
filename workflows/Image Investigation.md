# Image Investigation

[Previous: Phone Investigation](../workflows/Phone%20Investigation.md) · [Next: Domain Investigation](../workflows/Domain%20Investigation.md) · [Back to README](../README.md)

> [!IMPORTANT]
> Use this workflow only for a legitimate, documented purpose. Public availability does not remove privacy, contractual, or data-protection obligations.

## Table of contents

<!-- toc:start -->
- [Outcome](#outcome)
- [Before collection](#before-collection)
- [1. Preserve the original](#1-preserve-the-original)
- [2. Inspect safely](#2-inspect-safely)
- [3. Generate derivatives](#3-generate-derivatives)
- [4. Search for earlier copies](#4-search-for-earlier-copies)
- [5. Geolocate](#5-geolocate)
- [6. Chronolocate](#6-chronolocate)
- [7. Report confidence](#7-report-confidence)
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

## 1. Preserve the original

Save the highest-quality available file without re-encoding. Calculate SHA-256 and record acquisition URL, time, and method.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 2. Inspect safely

Identify the actual file type, dimensions, color profile, embedded previews, and metadata in an isolated environment.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 3. Generate derivatives

Create documented crops, frames, contrast variants, and perceptual hashes. Never overwrite the original.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 4. Search for earlier copies

Use multiple reverse-image engines and search distinctive visual elements. Prioritize the earliest verifiable publication, not the first search result.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 5. Geolocate

Extract signs, terrain, shadows, architecture, weather, road markings, and landmarks; test each clue against independent geospatial sources.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 6. Chronolocate

Compare upload history, weather, sun position, construction state, vegetation, and event context. State time ranges rather than false precision.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## 7. Report confidence

List supporting and contradicting observations, transformation history, source URLs, hashes, and confidence level.

**Record:** source, query or action, UTC time, output location, and confidence. **Decision gate:** continue only if this step produces a relevant lead within scope.

## Evidence package

Create a case directory with a read-only original, working copies, exports, screenshots, and a research log. Hash acquired files with SHA-256. Record tool name, version, configuration, time zone, errors, and any transformations. Cite the primary source for each factual claim and label analytical confidence.

## Stop conditions

Stop collection when authorization is unclear, a source signals access restrictions, the subject could be notified or harmed unexpectedly, the tool leaves scope, or the question is answered. Escalate sensitive findings through the approved reporting channel; do not publish credentials, private communications, precise home locations, or unrelated personal data.

---

[Previous: Phone Investigation](../workflows/Phone%20Investigation.md) · [Next: Domain Investigation](../workflows/Domain%20Investigation.md) · [Back to README](../README.md)
