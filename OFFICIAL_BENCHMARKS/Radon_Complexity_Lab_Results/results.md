# Radon_Complexity_Lab_Results
**Project:** `K_SGLANG` | **Status:** `PASS` | **Run:** `2026-09-30T17:14:20.030944+00:00`

**Framework:** [Radon — Cyclomatic Complexity & Maintainability Index](https://radon.readthedocs.io/)

## Key Metrics

- **files_analyzed:** `10`
- **average_complexity:** `{'grade': 'A', 'score': 4.924242424242424}`
- **complexity_grade:** `A`
- **complexity_score:** `4.924242424242424`
- **mi_output:** `E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SGLANG\UPSTREAM\benchmark\bench_adaptive_speculative.py - A (`

## Raw Output (first 50 lines)
```
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SGLANG\UPSTREAM\benchmark\bench_adaptive_speculative.py
    F 89:0 run_phase - C (12)
    F 144:0 summarize_phases - B (9)
    F 166:0 main - B (9)
    F 53:0 send_request - A (3)
    F 46:0 build_phase_plan - A (2)
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SGLANG\UPSTREAM\benchmark\lean_kernel_sweep.py
    F 124:0 main - B (10)
    F 44:0 bench - A (3)
    F 55:0 run - A (1)
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SGLANG\UPSTREAM\python\setup.py
    F 112:0 _match_by_substring - B (9)
    F 184:0 _selected_rust_extensions - B (7)
    F 131:0 _discovered_rust_extensions - A (5)
    F 56:0 _cargo_metadata - A (4)
    F 91:0 _cargo_workspace_metadata - A (4)
    C 219:4 BuildRust - A (4)
    F 170:0 _pyproject_rust_extensions - A (3)
    F 209:0 _declared_rust_extensions - A (3)
    M 235:8 BuildRust.run - A (3)
    M 222:8 BuildRust.run_for_extension - A (2)
E:\fenta\Downloads\The Anticloud\TIER_4_INFERENCE_AGENTS\K_SGLANG\UPSTREAM\scripts\convert_otel_2_perfetto.py
    F 138:0 extract_all_otel_spans - C (11)
    F 172:0 build_otel_span_tree - B (10)
    F 346:0 generate_perfetto_links - B (10)
    F 230:0 generate_perfetto_span - B (9)
    F 95:0 __find_line - B (7)
    F 199:0 __convert_to_perfetto_span - A (5)
    F 269:0 generate_perfetto_span_layout - A (5)
    F 312:0 __convert_to_perfetto_events - A (5)
    F 336:0 generate_perfetto_events - A (5)
    M 58:4 SpanLayoutContaine
```

---
_Anticloud Independent Benchmark — 2026-09-30T17:14:20.030944+00:00_