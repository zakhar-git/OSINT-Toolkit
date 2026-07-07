# Tool card template

[Previous: Contributing](../CONTRIBUTING.md) · [Next: README](../README.md) · [Back to README](../README.md)

Copy the data fields into `scripts/build_docs.py`; category pages are generated. Replace every placeholder. Use `TODO` only for a bounded unknown that does not undermine the recommendation; if existence, official source, maintenance, or core functionality cannot be verified, do not include the tool.

## Table of contents

<!-- toc:start -->
- [Template](#template)
- [Acceptance checklist](#acceptance-checklist)
<!-- toc:end -->

## Template

````markdown
<a id="tool-name"></a>
<details>
<summary><strong>Tool Name</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Tool Name |
| **Description** | One factual sentence. |
| **Category** | Primary category |
| **Platform** | Supported operating systems and runtime |
| **Repository** | [Official repository](https://example.com/) |
| **Official website** | [Official website](https://example.com/) |
| **License** | SPDX identifier or `TODO` |
| **Status** | Active, Maintained, Experimental, Archived, Deprecated, or Community |
| **Last verified** | YYYY-MM-DD |

**Installation**

```text
official minimal installation command
```

**Quick example**

```text
safe command using synthetic or reserved input
```

**Supported sources**

Exact public, local, authenticated, or directly probed source types.

**Pros**

Concrete strengths relevant to an investigation.

**Limitations**

Specific failure modes, access conditions, safety concerns, and inference limits.

</details>
````

## Acceptance checklist

- Official upstream identity, documentation, and license verified.
- Status justified by current commits, releases, issues, service updates, or maintainer statements.
- Installation follows current official documentation.
- Example uses only synthetic or reserved input.
- Supported sources do not overstate access.
- Limitations are specific and actionable.
- The tool is not archived, deprecated, abandoned, duplicated, or added only for popularity.
- No duplicate card exists in another category.

---

[Previous: Contributing](../CONTRIBUTING.md) · [Next: README](../README.md) · [Back to README](../README.md)
