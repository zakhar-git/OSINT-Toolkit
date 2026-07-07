# AI

[Previous: OPSEC](../categories/OPSEC.md) · [Next: Infrastructure](../categories/Infrastructure.md) · [Back to README](../README.md)

> [!NOTE]
> This guide covers lawful collection from public sources. Confirm authorization, platform terms, and local law before collecting or retaining data.

Local language, transcription, and extraction assistance for analysts.

## Table of contents

<!-- toc:start -->
- [Scope](#scope)
- [Investigation approach](#investigation-approach)
- [Tools](#tools)
  - [Ollama](#ollama)
  - [whisper.cpp](#whisper-cpp)
- [Quality controls](#quality-controls)
- [Related workflows](#related-workflows)
<!-- toc:end -->

## Scope

Use this category to generate and test leads, not to declare identity or attribution from a single match. Define the research question, collection boundary, and retention rule before opening a tool.

## Investigation approach

1. Preserve the input exactly as received and record its source.
2. Normalize only in a separate working copy and document every transformation.
3. Start with passive or locally processed sources.
4. Validate important results manually against the primary source.
5. Record UTC timestamps, URLs, tool versions, queries, and uncertainty.
6. Minimize personal data and stop when the research question is answered.

## Tools

The entries below are curated starting points, not endorsements. Verify current upstream documentation and release signatures before installation.

<a id="ollama"></a>
<details>
<summary><strong>Ollama</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | Ollama |
| **Description** | Runs supported language and vision models locally for extraction, classification, and analyst-assisted review. |
| **Category** | AI |
| **Platform** | Linux, macOS, Windows; Docker |
| **Repository** | [https://github.com/ollama/ollama](https://github.com/ollama/ollama) |
| **Official website** | [https://ollama.com/](https://ollama.com/) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
# Follow the signed installer instructions on the official website.
ollama pull gemma3
```

**Quick example**

```text
ollama run gemma3 'Extract claims and uncertainties from this public text.'
```

**Supported sources**

Analyst-supplied local text, images for supported models, and model files.

**Pros**

Local processing can reduce disclosure; scriptable API; broad model ecosystem.

**Limitations**

Models hallucinate and reproduce bias; model licenses vary; outputs require source-grounded human verification.

</details>

<a id="whisper-cpp"></a>
<details>
<summary><strong>whisper.cpp</strong></summary>

| Field | Value |
| --- | --- |
| **Name** | whisper.cpp |
| **Description** | Local C/C++ implementation of Whisper speech recognition for offline transcription and language identification of collected audio. |
| **Category** | AI |
| **Platform** | Linux, macOS, Windows, iOS, Android; CPU and GPU backends |
| **Repository** | [https://github.com/ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) |
| **Official website** | [https://github.com/ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) |
| **License** | MIT |
| **Status** | Maintained |
| **Last verified** | 2026-07-07 |

**Installation**

```text
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp
cmake -B build
cmake --build build --config Release
```

**Quick example**

```text
./build/bin/whisper-cli -m models/ggml-base.en.bin -f interview.wav -oj
```

**Supported sources**

Local audio and video converted through FFmpeg-supported formats.

**Pros**

Runs locally without sending audio to a service; timestamped JSON output; 2026 release activity observed.

**Limitations**

Names, numbers, accents, and low-quality audio remain error-prone; model files have separate provenance; transcripts must be verified against the recording.

</details>

## Quality controls

- Corroborate identity or ownership with at least two independent signals.
- Distinguish a tool result, an observed fact, and an analytical inference.
- Preserve raw output before filtering or transforming it.
- Re-run time-sensitive checks before publication.
- Document negative results; they describe coverage, not absence.

## Related workflows

Use the closest procedural guide in the [workflow index](../README.md#workflows). When no exact workflow exists, combine the relevant collection steps with the evidence-preservation requirements in [CONTRIBUTING](../CONTRIBUTING.md#evidence-and-safety-standard).

---

[Previous: OPSEC](../categories/OPSEC.md) · [Next: Infrastructure](../categories/Infrastructure.md) · [Back to README](../README.md)
