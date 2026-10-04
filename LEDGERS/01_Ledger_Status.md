# Ledger Status

**Project:** `K_SGLANG`  
**Tier:** TIER_4_INFERENCE_AGENTS  
**Identity:** Upstream `sgl-project/sglang` @ `eb9c9ee99d47` (Apache-2.0)

## Chain state

| Fact | Value |
| --- | --- |
| Upstream | `sgl-project/sglang` |
| Commit | `eb9c9ee99d47bf4c526a06cd84da59cd9cf4e2a5` |
| Upstream licence | Apache-2.0 |
| Licence class | permissive |
| Clone size | 126.11 MB |
| Ledger | 0 blocks, chain verified |
| Current TRL | NOT YET MEASURED |
| Post-optimisation TRL | NOT YET MEASURED |
| II budget cap | 1000.0 IIU |
| Verified upstream edits | 1 |

- Blocks: **0**
- Head digest: `None`
- Chain verification: **verified**

## Independent verification

The chain is verifiable without trusting this project's tooling:

```
anticloud ledger verify
anticloud ledger export > ledger.jsonl
```

Each block carries the previous block's digest, so removing or reordering an
entry invalidates every block after it. That property is the reason the
ledger can stand in for a claim of what happened.
