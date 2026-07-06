# Documentation style guide

[Previous: Architecture](ARCHITECTURE.md) · [Next: README](../README.md) · [Back to README](../README.md)

## Table of contents

<!-- toc:start -->
- [Voice](#voice)
- [Claims and sources](#claims-and-sources)
- [Tool descriptions](#tool-descriptions)
- [Examples](#examples)
- [Links](#links)
- [Dates and time](#dates-and-time)
- [Accessibility](#accessibility)
<!-- toc:end -->

## Voice

Write concise, neutral, direct English. Prefer “records public DNS answers” to “powerful reconnaissance solution.” Avoid promotional claims, fear-based language, jokes, and emojis. Explain specialist terms when a careful non-specialist may misread them.

## Claims and sources

Use an official repository, official documentation, authoritative registry, original publication, or direct reproducible test. Say what was observed and when. Use `TODO` when a required fact is unknown. Do not silently fill gaps with likely values.

Separate these levels:

- **Tool output:** what software reported.
- **Observation:** what the analyst independently confirmed in a source.
- **Inference:** an interpretation supported by stated observations.
- **Unknown:** information that could not be established.

## Tool descriptions

Lead with the concrete operation and source type. Avoid “best,” “comprehensive,” and “accurate” unless a cited, bounded test supports the term. Limitations must describe actual failure modes: stale data, identity ambiguity, rate limits, access requirements, active traffic, or transformation loss.

## Examples

Use reserved or synthetic values:

| Data type | Safe example |
| --- | --- |
| Domain | `example.com` |
| IPv4 | `192.0.2.0/24`, `198.51.100.0/24`, or `203.0.113.0/24` |
| Phone | `+1 202-555-0123` or another documented fictional range |
| Email | `subject@example.com` |
| Username | `analyst_handle` |

Commands should be minimally invasive and explain when they produce network traffic. Never use a real private person's identifier.

## Links

Use descriptive labels and HTTPS. Link repositories to the upstream owner, not a copy, unless the mirror status is explicit. Link documentation to the exact relevant page when stable. Do not add tracking parameters or URL shorteners.

## Dates and time

Use `YYYY-MM-DD`. Use UTC for evidence events and specify the zone when quoting a source-local time. “Last verified” means a maintainer checked the link, license, core capability, status basis, and example on that date.

## Accessibility

Use ordered headings, meaningful alt text, descriptive links, compact tables, and text that does not rely on color. Collapsible cards may hide detail but never the page's scope, safety notice, or essential method.

---

[Previous: Architecture](ARCHITECTURE.md) · [Next: README](../README.md) · [Back to README](../README.md)
