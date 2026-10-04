# Developer Cookbook — K_SGLANG
**Stack:** Python 3.11, SGLang 0.2+, PyTorch 2.10+, PAX 27B, AIOSS_FORMAT
**Domain:** SGLang: structured generation language runtime for PAX 27B constrained outputs

## Structured JSON generation
```python
from k_sglang import SGLangEngine
import sglang as sgl

engine = SGLangEngine(pax_model="./pax-27b-q4.gguf", aioss_chain="./sglang.aioss")

@sgl.function
def analyze_biosignal(s, eeg_data):
    s += sgl.user(f"Analyze this EEG data: {eeg_data}")
    s += sgl.assistant(sgl.gen("analysis", max_tokens=256))
    s += sgl.user("Format as JSON with fields: seizure_probability, dominant_frequency, artifact_detected")
    s += sgl.assistant(sgl.gen("json_output", max_tokens=128,
                                 regex=r'\{"seizure_probability".*\}'))

result = engine.run(analyze_biosignal, eeg_data="[0.1, 0.3, -0.2, ...]")
print(result["json_output"])  # guaranteed valid JSON
print(f"Chain: {result.chain_hash}")
```

## Schema-constrained generation
```python
from k_sglang import JSONSchemaConstrained

schema = {
    "type": "object",
    "properties": {
        "project": {"type": "string"},
        "trl": {"type": "integer", "minimum": 1, "maximum": 9},
        "compliant": {"type": "boolean"}
    }
}
result = engine.generate_constrained(
    prompt="Describe K_BRAINFLOW's compliance status",
    schema=schema
)
```

## Parallel structured generation
```python
results = engine.batch_run(analyze_biosignal,
                           [{"eeg_data": d} for d in eeg_samples])
```

## AIOSS Chain Append
```python
import hashlib, time

def aioss_append(chain_path, payload: bytes, module_id: str):
    entry_hash = hashlib.sha3_256(payload).digest()
    ts = int(time.time_ns()).to_bytes(8, 'big')
    with open(chain_path, 'rb') as f:
        f.seek(-32, 2); prev_hash = f.read(32)
    new_hash = hashlib.sha3_256(prev_hash + entry_hash + ts).digest()
    with open(chain_path, 'ab') as f:
        f.write(ts + entry_hash + new_hash)
    return new_hash.hex()
```
