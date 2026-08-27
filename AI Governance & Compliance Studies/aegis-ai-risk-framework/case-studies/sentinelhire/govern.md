# SentinelHire — GOVERN

[← Architecture](architecture.md) · [Back to README](../../README.md) · Next: [MAP →](map.md)

---

Applying [Framework Phase 2: GOVERN](../../framework/01-govern.md) to SentinelHire.

## Assigned Roles

| Role | Assignment (illustrative) |
|---|---|
| Business owner | VP, Talent Acquisition |
| System owner | Director, HR Technology |
| AI risk owner | AI Governance Lead |
| Control owners | Platform Engineering (retrieval/access), Security Engineering (guardrails) |
| Risk acceptance authority | CISO / VP HR Technology (joint sign-off for high-severity items) |
| Security authority | CISO |
| Data owner | HR Data Governance |
| Legal/Compliance | Employment Law, Privacy Office |
| Incident response | Security Operations Center |

## Applicable Obligations

- Employment/anti-discrimination law in operating jurisdictions
- Data privacy regulations covering applicant PII
- Vendor/data processing agreement with the commercial LLM provider
- Internal HR data retention policy

## Risk Tolerance (as adopted for SentinelHire)

| Risk Domain | Tolerance |
|---|:---:|
| Unauthorized PII disclosure | Zero |
| Unauthorized retrieval | Zero |
| Autonomous hiring rejection | Zero |
| Material discriminatory outcomes | Very low |
| Prompt injection success | Low |
| Hallucinated qualifications | Low |
| Temporary availability loss | Moderate |

## Governance Decisions

- SentinelHire is confirmed **advisory only** — the system may never autonomously reject a candidate. This constraint is treated as a hard governance boundary, not a configurable setting.
- All model/prompt/guardrail changes require sign-off from both the System Owner and AI Risk Owner before production deployment.
- Any confirmed PII disclosure incident triggers immediate escalation to Legal and the Privacy Office, independent of severity scoring.

Next: [MAP →](map.md)
