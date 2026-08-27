# SentinelHire — MEASURE

[← MAP](map.md) · [Back to README](../../README.md) · Next: [MANAGE →](manage.md)

---

Applying [Framework Phase 4: MEASURE](../../framework/03-measure.md) to SentinelHire's four priority risks.

## Metrics Selected

| ID | Metric | Target | Test Method | Sample Size |
|---|---|---|---|---|
| `AIM-001` | Prompt Injection Success Rate | < 0.5% | Adversarial resume injection test suite | 500 crafted resumes |
| `AIM-002` | Unauthorized Retrieval Rate | 0% | Cross-department retrieval attack simulation | 1,000 attempts |
| `AIM-003` | PII Leakage Rate | 0% | Red-team prompting for PII extraction | 300 test conversations |
| `AIM-006` | Demographic Parity Gap | Within approved fairness threshold | Statistical parity analysis across protected classes | Full historical applicant sample (anonymized) |
| `AIM-007` | Equal Opportunity Difference | Within approved fairness threshold | True-positive rate comparison across protected classes | Full historical applicant sample (anonymized) |
| `AIM-012` | Guardrail False-Negative Rate | < 1% | Known attack pattern replay | 200 known injection patterns |

## Worked Example — Unauthorized Retrieval (AIM-002)

| Step | Detail |
|---|---|
| **Risk** | Recruiters retrieve resumes outside their authorized department |
| **Control** | Department-level retrieval authorization |
| **Implementation** | Vector metadata filtering plus authorization middleware |
| **Metric** | `AIM-002` — Unauthorized Retrieval Rate |
| **Test** | 1,000 cross-department retrieval attempts |
| **Evidence** | Authorization test report and system logs (see [`/evidence`](../../evidence/README.md)) |
| **Residual risk** | Determined only after test evidence is reviewed |

## Status

All metrics for SentinelHire are currently **pending initial test execution**. This case study intentionally leaves results as `TBD after test` to demonstrate that AARF does not permit a risk to be marked "Accept" or a control "Effective" without evidence — see the [risk register template](../../templates/ai-risk-register.xlsx) and [metric register template](../../templates/ai-metric-register.xlsx).

Next: [MANAGE →](manage.md)
