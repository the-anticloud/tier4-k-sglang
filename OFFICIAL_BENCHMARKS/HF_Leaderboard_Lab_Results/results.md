# HF_Leaderboard_Lab_Results

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

**Framework:** [HuggingFace Open LLM Leaderboard (proxy via distilbert-base-uncased)](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)

**Model used:** `distilbert-base-uncased`

### Inference Latency (Classification)

| Metric | Value |
| ------ | ----- |
| Avg latency | **56.87 ms** |
| Min latency | 49.52 ms |
| Max latency | 68.22 ms |
| Samples | 5 |

### Real Tokenization Results

| Field | Value |
| ----- | ----- |
| Token count | **30** |
| Tokenization latency | 1.0 ms |
| Classification label | `LABEL_0` |
| Classification score | 0.5819 |
| Classification latency | 63.51 ms |
| Status | **PASS** |

**Input text tokenized:**
```
K_SGLANG (sgl-project/sglang) — 0 files, 0 source lines, licence unknown, primary language []
```

**First 20 tokens:**
```
['[CLS]', 'k', '_', 'sg', '##lang', '(', 'sg', '##l', '-', 'project', '/', 'sg', '##lang', ')', '—', '0', 'files', ',', '0', 'source']
```

> Full MMLU/HellaSwag/TruthfulQA/ARC/Winogrande/GSM8K require dedicated GPU.
> These results are CPU inference proxy metrics using distilbert-base-uncased.

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_