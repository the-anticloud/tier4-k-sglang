# Deploy Guide — K_SGLANG
**Tier:** TIER_4_INFERENCE_AGENTS | **Stack:** Python 3.11, SGLang 0.2+, PyTorch 2.10+, PAX 27B, AIOSS_FORMAT
**Air-gap capable after initial setup.**

## Prerequisites
Python 3.11+, sglang 0.2+, PyTorch 2.10+, PAX 27B weights, T4 GPU.

## Environment
T4 GPU (15.6GB VRAM). SGLang runtime adds ~200MB overhead beyond PAX 27B base.

## AIOSS Integration
```bash
aioss init --module K_SGLANG --output ./k_sglang.aioss
aioss append --chain ./k_sglang.aioss --payload ./output.bin --module K_SGLANG
aioss verify --chain ./k_sglang.aioss
```

## Air-Gap Setup
```bash
pip download -r requirements.txt -d ./wheels/
pip install --no-index --find-links ./wheels/ -r requirements.txt
```

## PAX 27B Harness Wiring
```python
from anticloud_pax import PAXHarness
harness = PAXHarness(
    model_path="./pax-27b-q4.gguf",
    module="K_SGLANG",
    aioss_chain="./K_SGLANG.aioss",
    classification="L5_NARROW_L2_GENERAL"
)
result = harness.process(input_data)
```

## Verification
```bash
aioss verify --chain ./K_SGLANG.aioss --verbose
python -m K_SGLANG.tests.smoke
```
