# SentinelHire — MANAGE

[← MEASURE](measure.md) · [Back to README](../../README.md) · Next: [Current Profile →](current-profile.md)

---

Applying [Framework Phase 5: MANAGE](../../framework/04-manage.md) to SentinelHire.

## Risk Treatment Table

| ID | Risk | Inherent | Control | Metric | Residual | Decision |
|---|---|:---:|---|---|:---:|:---:|
| `AIR-001` | Prompt injection | High | Input isolation + guardrails | AIM-001/012 | *TBD after test* | Mitigate |
| `AIR-002` | Unauthorized retrieval | Critical | Retrieval ACL + authorization | AIM-002 | *TBD after test* | Mitigate |
| `AIR-003` | PII leakage | High | Access control + DLP/output filtering | AIM-003 | *TBD after test* | Mitigate |
| `AIR-004` | Hiring bias | High | HITL + fairness testing + governance | AIM-006–008 | *TBD after test* | Mitigate |

## Control Ownership

| Control | Owner |
|---|---|
| Input isolation + guardrails | Security Engineering |
| Retrieval ACL + authorization | Platform Engineering |
| Access control + DLP/output filtering | Security Engineering + Data Governance |
| HITL + fairness testing + governance | HR Technology + AI Governance |

## Path to Residual Risk Determination

No risk in this table may be closed out as "Accept" until:

1. The associated metric(s) have been tested per the [MEASURE](measure.md) plan
2. Evidence has been filed in [`/evidence`](../../evidence/README.md)
3. A [risk acceptance record](../../templates/ai-risk-acceptance.md) has been signed by the risk acceptance authority named in [GOVERN](govern.md)

Next: [Current Profile →](current-profile.md)
