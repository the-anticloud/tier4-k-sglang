# Anticloud × SGLANG
> Structured LLM generation without a single cloud API call.

**Part of:** Inference Agents · Anticloud FZ LLE · 0-1.gg
**Upstream:** sgl-project/sglang (Apache-2.0)
**License:** Apache-2.0 OR LicenseRef-Anticommons-Enterprise-1.0
**IP:** USPTO pending · Lois-Kleinner Alpasan · 2026

SGLang's RadixAttention enables prefix caching for 40% latency reduction on shared prompts. We add cryptographic audit trail.

```bash
python -m sglang.launch_server \
    --model kleinnner/pax-one-27b \
    --ledger ./pax_ledger.aioss

# Every request auto-logged to ledger with confidence/contradiction
```

**Plays well with:** L-VLLM (alternative backend), K-PAXSCHED (multi-agent coordinator), K-AIOSS (ledger)
