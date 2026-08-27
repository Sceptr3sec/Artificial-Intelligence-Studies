# 5. MANAGE — Treat and Accept Risk

[← MEASURE](03-measure.md) · [Back to README](../README.md) · Next: [MONITOR →](05-continuous-monitoring.md)

---

MANAGE turns evidence into action. Each significant risk receives a treatment decision, and residual risk must be explicitly accepted by an authorized role before deployment.

## Treatment Decisions

| Decision | Meaning |
|---|---|
| **MITIGATE** | Apply a control to reduce likelihood or impact |
| **ACCEPT** | Formally accept the risk as-is (requires named authority) |
| **AVOID** | Change or remove the capability that creates the risk |
| **TRANSFER** | Shift risk via contract, insurance, or vendor terms |

## Illustrative Risk Treatment Table

| ID | Risk | Inherent | Control | Metric | Residual | Decision |
|---|---|:---:|---|---|:---:|:---:|
| `AIR-001` | Prompt injection | High | Input isolation + guardrails | AIM-001/012 | *TBD after test* | Mitigate |
| `AIR-002` | Unauthorized retrieval | Critical | Retrieval ACL + authorization | AIM-002 | *TBD after test* | Mitigate |
| `AIR-003` | PII leakage | High | Access control + DLP/output filtering | AIM-003 | *TBD after test* | Mitigate |
| `AIR-004` | Hiring bias | High | HITL + fairness testing + governance | AIM-006–008 | *TBD after test* | Mitigate |

## Evidence-Based Control Validation

A control is not considered effective merely because it is documented or implemented. AARF requires a traceable chain from risk to residual-risk decision:

```
RISK → CONTROL → IMPLEMENTATION → METRIC → TEST → EVIDENCE → RESIDUAL RISK
```

### Worked Example — Unauthorized Resume Retrieval

| Step | Detail |
|---|---|
| **Risk** | Recruiters retrieve resumes outside their authorized department |
| **Control** | Department-level retrieval authorization |
| **Implementation** | Vector metadata filtering plus authorization middleware |
| **Metric** | `AIM-002` — Unauthorized Retrieval Rate |
| **Test** | 1,000 cross-department retrieval attempts |
| **Evidence** | Authorization test report and system logs |
| **Residual risk** | Determined only after test evidence is reviewed |

## Current Profile → Target Profile

| Capability | Current Example | Target State / Evidence |
|---|---|---|
| Prompt injection resistance | Not validated | Defined threshold met; red-team report |
| Retrieval authorization | Cross-department access possible | 0% unauthorized retrieval; authorization test |
| PII protection | Partial | 0% unauthorized leakage; DLP/access-control evidence |
| Human oversight | Informal | Mandatory HITL workflow; configuration and audit evidence |
| Fairness assurance | Not tested | Approved fairness metrics tested and reviewed |
| Logging | Outputs only | Required event coverage demonstrated |
| AI incident response | Not established | Approved playbook + exercise/test evidence |
| Model monitoring | Not established | Drift/performance monitoring with thresholds and alerts |

## Final AI Risk Determination

| Decision | Meaning |
|---|---|
| **APPROVE** | Acceptable for production |
| **CONDITIONAL APPROVAL** | Deployment allowed only under documented restrictions/actions |
| **DO NOT APPROVE** | Unacceptable risk remains and deployment is blocked |

The final assessment should state: overall risk, deployment recommendation, blocking findings, required actions, residual risks, risk acceptance authority, and reassessment conditions.

## Outputs of This Phase

- Completed [risk register](../templates/ai-risk-register.xlsx) with treatment decisions
- Completed [control matrix](../templates/ai-control-matrix.xlsx)
- Signed [risk acceptance record](../templates/ai-risk-acceptance.md)
- A [final assessment report](../templates/ai-assessment-report.md)

## See Also

- [Case Study: SentinelHire — MANAGE](../case-studies/sentinelhire/manage.md)
- [Case Study: SentinelHire — Final Assessment](../case-studies/sentinelhire/final-assessment.md)
