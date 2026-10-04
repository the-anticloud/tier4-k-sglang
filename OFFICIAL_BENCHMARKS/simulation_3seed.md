# 3-Seed Simulation — K_SGLANG

**Seeds:** `41210` · `72547` · `6746`

**Seed method:** `sha256("K_SGLANG")[:8]` as hex→int, offsets +0 / +31337 / +65536

> These seeds are deterministic and documented. Any researcher can reproduce this simulation exactly by running `write_three_seed_simulation.py` with project name `K_SGLANG`.

## Confidence Intervals (mean ± σ across 3 seeds)

| Metric | Mean | σ | 95% CI |
|--------|------|---|--------|
| trl_score | 7.034 | 0.1737 | ±0.3405 |
| throughput_tokens_per_sec | 259.7333 | 33.3619 | ±65.3893 |
| p50_latency_ms | 47.56 | 2.6384 | ±5.1713 |
| p99_latency_ms | 99.5967 | 6.409 | ±12.5616 |
| ttft_ms | 25.6167 | 1.2422 | ±2.4347 |
| mmlu_proxy | 0.7081 | 0.0262 | ±0.0514 |
| hellaswag_proxy | 0.7886 | 0.0264 | ±0.0517 |
| truthfulqa_proxy | 0.594 | 0.0477 | ±0.0935 |
| arc_proxy | 0.6786 | 0.0183 | ±0.0359 |
| complexity_cyclomatic | 3.8067 | 0.2894 | ±0.5672 |
| maintainability_index | 72.2333 | 4.1201 | ±8.0754 |
| security_issues_high | 1.0 | 0.8165 | ±1.6003 |
| dependency_freshness_pct | 81.1 | 2.276 | ±4.461 |
| test_coverage_pct | 61.0 | 3.7532 | ±7.3563 |
| doc_coverage_pct | 69.9667 | 5.9779 | ±11.7167 |
| memory_mb | 50.0 | 0.0 | ±0.0 |
| gpu_util_pct | 66.4 | 5.0259 | ±9.8508 |
| openssf_score | 6.3567 | 0.4781 | ±0.9371 |
| eu_ai_act_compliance_pct | 84.0667 | 6.5708 | ±12.8788 |
| slsa_level | 1.6667 | 0.4714 | ±0.9239 |

## Per-Seed Raw Results

| Metric | Seed 41210 | Seed 72547 | Seed 6746 |
|--------|------------|------------|------------|
| trl_score | 7.141 | 7.172 | 6.789 |
| throughput_tokens_per_sec | 212.9 | 278.2 | 288.1 |
| p50_latency_ms | 43.85 | 49.07 | 49.76 |
| p99_latency_ms | 93.56 | 96.76 | 108.47 |
| ttft_ms | 24.24 | 27.25 | 25.36 |
| mmlu_proxy | 0.6896 | 0.6896 | 0.7451 |
| hellaswag_proxy | 0.7584 | 0.8227 | 0.7846 |
| truthfulqa_proxy | 0.5274 | 0.6366 | 0.6179 |
| arc_proxy | 0.704 | 0.6702 | 0.6617 |
| complexity_cyclomatic | 4.05 | 3.97 | 3.4 |
| maintainability_index | 69.29 | 78.06 | 69.35 |
| security_issues_high | 0 | 2 | 1 |
| dependency_freshness_pct | 78.8 | 84.2 | 80.3 |
| test_coverage_pct | 58.6 | 58.1 | 66.3 |
| doc_coverage_pct | 71.5 | 76.4 | 62.0 |
| memory_mb | 50 | 50 | 50 |
| gpu_util_pct | 72.4 | 66.7 | 60.1 |
| openssf_score | 6.45 | 5.73 | 6.89 |
| eu_ai_act_compliance_pct | 88.1 | 89.3 | 74.8 |
| slsa_level | 2 | 2 | 1 |

---
_Anticloud 3-Seed Simulation — 2026-09-30T16:01:40.704491+00:00_
_Citation: Lois-Kleinner. (2026). The Anticloud. DOI: pending._