"""
K-SGLANG Anticloud Integration — AIOSS Ledger for SGLang RadixAttention

RadixAttention tracks prefix cache hits/misses. AIOSS logs every
request with cache_hit flag, enabling audit of prefix reuse patterns.

Usage:
    from aioss_integration import AIossSGLangWrapper

    runtime = sgl.Runtime(model_path="kleinnner/pax-one-27b-fp8")
    wrapped = AIossSGLangWrapper(runtime, ledger_path="./sglang_ledger.aioss")

No frontier API keys. Local inference only.
"""

from __future__ import annotations
import hashlib
import json
import subprocess
import time
from pathlib import Path
from typing import Optional


class AIossSGLangWrapper:
    """
    Wraps SGLang Runtime to log inference + prefix cache hits to AIOSS.

    Cache hit logging enables analysis of prefix reuse — useful for
    detecting repeated system prompts (potential security indicator).
    """

    def __init__(
        self,
        runtime,
        ledger_path: str = "./sglang_ledger.aioss",
        aioss_bin: str = "aioss",
    ):
        self.runtime = runtime
        self.ledger_path = Path(ledger_path)
        self.aioss_bin = aioss_bin

        if not self.ledger_path.exists():
            self._init_ledger()

    def _init_ledger(self):
        subprocess.run(
            [self.aioss_bin, "init", str(self.ledger_path.parent), "--user", "sglang-anticloud"],
            check=True,
            capture_output=True,
        )

    def _log(
        self,
        prompt: str,
        output: str,
        tokens_in: int,
        tokens_out: int,
        wall_time_ms: float,
        cache_hit: bool,
        prefix_len: int = 0,
    ):
        content = json.dumps({
            "model": "sglang-local",
            "prompt_hash": hashlib.sha3_256(prompt.encode()).hexdigest(),
            "output_hash": hashlib.sha3_256(output.encode()).hexdigest(),
            "radix_attention": {
                "cache_hit": cache_hit,
                "prefix_tokens_reused": prefix_len,
                "latency_saved_ms": round(prefix_len * 0.05, 2) if cache_hit else 0,
            },
            "telemetry": {
                "tokens_in": tokens_in,
                "tokens_out": tokens_out,
                "wall_time_ms": round(wall_time_ms, 1),
                "cost_if_cloud_microcents": 0,
            },
        })

        subprocess.run(
            [
                self.aioss_bin, "append", str(self.ledger_path),
                "--type", "inference_result",
                "--actor", "sglang",
                "--content", content,
            ],
            capture_output=True,
        )

    def run(self, prompt: str, **kwargs):
        """
        Runs SGLang inference and logs to AIOSS with cache hit info.
        """
        start = time.perf_counter()

        # Track if this is likely a cache hit (same prefix seen before)
        prompt_hash = hashlib.sha3_256(prompt[:256].encode()).hexdigest()

        result = self.runtime.run(prompt, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000

        output_text = str(result) if result else ""

        self._log(
            prompt=prompt,
            output=output_text,
            tokens_in=len(prompt.split()),
            tokens_out=len(output_text.split()),
            wall_time_ms=elapsed_ms,
            cache_hit=elapsed_ms < 100,  # heuristic: fast = likely cache hit
        )

        return result

    def analyze_cache_efficiency(self) -> dict:
        """
        Reads AIOSS ledger to compute RadixAttention cache hit rate.
        High cache hit rate = efficient prefix reuse.
        """
        result = subprocess.run(
            [self.aioss_bin, "export", str(self.ledger_path), "--format", "json"],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            return {"error": "could not read ledger"}

        entries = json.loads(result.stdout).get("entries", [])
        cache_hits = sum(
            1 for e in entries
            if e.get("content", {}).get("radix_attention", {}).get("cache_hit", False)
        )

        return {
            "total_requests": len(entries),
            "cache_hits": cache_hits,
            "cache_hit_rate": f"{cache_hits/max(len(entries),1)*100:.1f}%",
            "estimated_latency_saved_ms": sum(
                e.get("content", {}).get("radix_attention", {}).get("latency_saved_ms", 0)
                for e in entries
            ),
        }


# Minimal test without SGLang installed
if __name__ == "__main__":
    class MockRuntime:
        def run(self, prompt, **kwargs):
            return f"Response to: {prompt[:50]}"

    wrapper = AIossSGLangWrapper(MockRuntime(), ledger_path="./sglang_test.aioss")

    # Simulate requests with shared prefix
    shared_prefix = "You are a helpful AI assistant. "
    for q in ["What is 2+2?", "What is Python?", "What is vLLM?"]:
        wrapper.run(shared_prefix + q)

    print("Cache analysis:", wrapper.analyze_cache_efficiency())


# SECURITY_PATCH — B602 — subprocess shell=True (CWE-78, Command Injection)
# Applied: 2026-09-30 | Anticloud FZ LLE

def safe_run(cmd):
    """Anticloud patch for B602: never pass shell=True."""
    import shlex
    parts = shlex.split(cmd) if isinstance(cmd, str) else cmd
    return subprocess.run(parts, shell=False, capture_output=True, text=True, timeout=30)
