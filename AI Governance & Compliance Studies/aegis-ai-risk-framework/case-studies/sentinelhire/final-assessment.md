# SentinelHire — Final AI Risk Determination

[← Target Profile](target-profile.md) · [Back to README](../../README.md)

---

Applying [Framework Phase 9: Final AI Risk Determination](../../framework/04-manage.md#final-ai-risk-determination) to SentinelHire.

## 1. System Overview

SentinelHire is a candidate-screening and recruiter decision-support tool built on a commercial LLM with retrieval-augmented generation over resumes and job descriptions. It is advisory-only — recruiters retain full decision authority.

## 2. Overall Risk Rating

**Overall risk: High (pre-mitigation)** — driven primarily by unauthorized retrieval (Critical inherent) and PII leakage / hiring bias (High inherent). No metric has yet been tested to demonstrate residual risk reduction.

## 3. Deployment Recommendation

- [ ] APPROVE
- [x] **CONDITIONAL APPROVAL** — pending completion of MEASURE-phase testing for `AIR-001` through `AIR-004`
- [ ] DO NOT APPROVE

## 4. Blocking Findings

| Finding | Severity | Required Action | Owner | Due Date |
|---|---|---|---|---|
| Retrieval authorization not yet validated | Critical | Complete `AIM-002` cross-department retrieval test | Platform Engineering | Before production launch |
| PII leakage controls untested | High | Complete `AIM-003` red-team PII extraction test | Security Engineering | Before production launch |
| Fairness metrics not yet tested | High | Run `AIM-006`–`AIM-008` against historical applicant data | AI Governance | Before production launch |
| Human oversight workflow informal | High | Enforce mandatory HITL step in system configuration | HR Technology | Before production launch |

## 5. Residual Risks Carried Forward

None yet accepted — all four priority risks remain in **Mitigate** status pending test evidence. See [MANAGE](manage.md) and the [risk register template](../../templates/ai-risk-register.xlsx).

## 6. Risk Acceptance Authority

Per [GOVERN](govern.md): joint sign-off required from CISO and VP HR Technology before any residual risk in this case study may be marked "Accept."

## 7. Reassessment Conditions

Per [Continuous Monitoring](../../framework/05-continuous-monitoring.md), SentinelHire must be reassessed if:

- The underlying LLM provider or model version changes
- Retrieval authorization logic changes
- A new applicant data source is added
- Any confirmed incident occurs in the risk domains above

---

*This is a fictional illustrative case study demonstrating AARF's methodology end-to-end, not an assessment of any real product.*
