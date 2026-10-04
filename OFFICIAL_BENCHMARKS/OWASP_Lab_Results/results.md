# OWASP_Lab_Results

**Project:** `K_SGLANG`  
**Tier:** `TIER_4_INFERENCE_AGENTS`  
**Slug:** `sgl-project/sglang`  
**Commit:** ``  
**Run:** `2026-09-30T15:07:07.146295+00:00`  

## Isolation Environment

| Field | Value |
| ----- | ----- |
| Platform | `win32` |
| Python | `3.12.10` |
| HF model | `distilbert-base-uncased` |
| HF load time | `4.42s` |
| Inference device | `cpu` |

## Results

**Framework:** [OWASP LLM Top 10 v1.1 (2024)](https://genai.owasp.org/resource/llm-top-10-for-llms-v1-1/)

Pass rate: **4/5** (80%)

| Check ID | Name | Status | Method |
| -------- | ---- | ------ | ------ |
| `LLM01` | Prompt Injection | **UNVERIFIED** | grep for input sanitization patterns |
| `LLM02` | Insecure Output Handling | **PASS** | grep for output escaping/sanitization |
| `LLM06` | Sensitive Information Disclosure | **PASS** | grep for env-var based secret management |
| `LLM09` | Overreliance | **PASS** | grep for confidence thresholds or human review gates |
| `LLM10` | Model Theft | **PASS** | grep for rate limiting or endpoint auth |

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_