# Curation policy

[Previous: Architecture](ARCHITECTURE.md) · [Next: Style guide](STYLE_GUIDE.md) · [Back to README](../README.md)

This repository is a professional knowledge base, not an exhaustive directory. A tool is included only when it improves a real investigation workflow and its claims can be checked from public, authoritative sources.

## Table of contents

<!-- toc:start -->
- [Selection standard](#selection-standard)
- [Required research trail](#required-research-trail)
- [Acceptance criteria](#acceptance-criteria)
- [Rejection criteria](#rejection-criteria)
- [Source hierarchy](#source-hierarchy)
- [Services without public repositories](#services-without-public-repositories)
- [Maintenance review](#maintenance-review)
- [Removal policy](#removal-policy)
- [TODO policy](#todo-policy)
<!-- toc:end -->

## Selection standard

Quality is more important than quantity. A category should contain only entries that an experienced analyst could reasonably justify using in a case, newsroom, research lab, or security team. Do not add a tool because it is familiar, popular, or present in another list.

Every listed tool must satisfy most of these conditions:

- official repository or official documentation is available;
- recent commits, releases, or service updates are visible;
- issue tracker, support channel, or maintainer activity shows current attention;
- documentation explains installation, operation, and data sources;
- functionality is relevant to real investigations;
- examples can be tested with synthetic or standards-reserved inputs;
- limitations can be described specifically;
- legal, privacy, and operational risks can be managed.

## Required research trail

Before adding or retaining a tool, reviewers should record:

1. Official repository URL or official service documentation.
2. Official website or documentation URL.
3. License source or terms-of-use source.
4. Most recent commit, release, package update, or vendor documentation update.
5. Issue tracker state or support channel signal.
6. Installation or access path tested, when practical.
7. Safe test input and observed output class.
8. Supported source types and access assumptions.
9. Known breakage, rate limits, account risks, privacy risks, and false-positive modes.
10. Reason the tool is better than existing entries for its category.

The pull request should summarize this trail. Reviewers may ask for raw notes when the project is unfamiliar or the capability is high-risk.

## Acceptance criteria

Accept a tool when it has a clear investigative role, a verifiable upstream source, current maintenance evidence, and limitations that can be stated without speculation. Specialized utilities, official APIs, forensic tools, archive tools, metadata analyzers, graph platforms, and actively maintained browser extensions are preferred over generic link directories.

Industry-standard tools may be included when they remain maintained and the category would be weaker without them. The card must still explain the narrow investigative use case.

## Rejection criteria

Reject or remove a tool when:

- the official repository is archived, abandoned, or inactive without historical necessity;
- the project has no verifiable official source;
- the description depends on marketing claims rather than documented behavior;
- the tool primarily bypasses access controls, evades detection, scrapes private data, or enables harassment;
- the maintenance signal is stale and no active fork is identified;
- platform changes have made the core functionality unreliable;
- the tool duplicates a stronger existing entry;
- examples cannot be made safe with synthetic or standards-reserved inputs;
- the only reason for inclusion is popularity or presence in another collection.

Historically important but unmaintained tools belong in a separate historical note only when that context is necessary. They should not be presented as current recommendations.

## Source hierarchy

Prefer sources in this order:

1. Official repository.
2. Official documentation.
3. Official release notes or package registry controlled by the project.
4. Maintainer statements in issues, discussions, mailing lists, or documentation.
5. Reproducible local test results.
6. Independent professional usage by recognized investigation, security, journalism, or research teams.

Community recommendations can support a decision but cannot replace official source verification.

## Services without public repositories

Some professional resources are official APIs or proprietary web services. They may be included only when the service has official documentation, a stable public website, clear access terms, and a distinct investigative value that cannot be covered by an open-source equivalent.

For these entries, set the repository field to `Not publicly published by vendor.` and explain the access model in limitations. Do not invent repository URLs or imply source-code availability.

## Maintenance review

Maintenance is reviewed from multiple signals: recent commits, releases, package updates, issue responses, documentation updates, and current compatibility with target platforms. A project with recent stars but no maintainer activity is not considered maintained.

Use `Maintained` only when upstream shows active development or support. Use `Community` for useful projects with limited guarantees. Use `Experimental` when upstream explicitly warns about instability or the workflow is narrow. Avoid `Archived` and `Deprecated` entries unless the page is documenting historical context.

## Removal policy

Removal is not a failure. It is part of keeping the knowledge base trustworthy. Remove or replace an entry when better evidence shows it is stale, unsafe, duplicated, unsupported, or no longer relevant to modern investigations.

When removing a tool, mention the reason in `CHANGELOG.md` and, when useful, open an issue for tracking a replacement.

## TODO policy

Use `TODO` only for a bounded unknown that does not undermine the recommendation. If the repository, existence, core functionality, or maintenance status cannot be verified, do not include the tool.

Acceptable TODO examples:

- license is unclear but official terms exist;
- installation package name changed and needs testing;
- a service has no public repository, and the card explicitly says so.

Unacceptable TODO examples:

- unknown whether the project exists;
- unknown whether the tool still works;
- unknown whether the repository is official;
- unknown whether the tool is lawful or safe to use.

---

[Previous: Architecture](ARCHITECTURE.md) · [Next: Style guide](STYLE_GUIDE.md) · [Back to README](../README.md)
