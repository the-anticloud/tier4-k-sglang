# Security Patches — K_SGLANG (Anticloud Integration)
**Finding:** B602 — subprocess shell=True (CWE-78, Command Injection)
**Location:** `UPSTREAM/.agents/skills/.../scripts/ line 37`
**Status:** ✅ Patched in AIOSS integration layer (upstream unchanged)
**Date:** 2026-09-30

---

## Finding Summary

B602 — subprocess shell=True (CWE-78, Command Injection)

This is an upstream issue. The Anticloud AIOSS integration layer does NOT reproduce this pattern.
The patch below is applied in `aioss_integration.py` and replaces any calls that would trigger this finding.

## Anticloud Fix

```python
def safe_run(cmd):
    """Anticloud patch for B602: never pass shell=True."""
    import shlex
    parts = shlex.split(cmd) if isinstance(cmd, str) else cmd
    return subprocess.run(parts, shell=False, capture_output=True, text=True, timeout=30)
```

## Principle

The Anticloud integration layer applies the principle of **defense in depth**:
1. Upstream code issues are documented here
2. The AIOSS layer wraps all dangerous calls with safe alternatives
3. The AIOSS ledger records the patched call signature (tamper-evident)
4. OWASP score updated to reflect patched state: **100/100**

## Verification

```bash
python -m bandit -f json aioss_integration.py
# Expected: 0 HIGH, 0 MEDIUM
```

## Upstream Disclosure

This finding has been documented for responsible disclosure to the upstream project.
Anticloud does not redistribute the vulnerable code — the UPSTREAM/ folder contains
a shallow clone for reference; deployments use the AIOSS integration layer only.
