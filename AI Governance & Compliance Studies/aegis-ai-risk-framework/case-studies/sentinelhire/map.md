# SentinelHire — MAP

[← GOVERN](govern.md) · [Back to README](../../README.md) · Next: [MEASURE →](measure.md)

---

Applying [Framework Phase 3: MAP](../../framework/02-map.md) to SentinelHire.

## Mapping Summary

| Domain | SentinelHire Specifics |
|---|---|
| **Users** | Recruiters, HR administrators, hiring managers |
| **Affected parties** | Job applicants (may never interact with the system directly), current employees referenced in comparative screening |
| **Data** | Resumes, job descriptions, applicant records, retrieved context passed to the LLM |
| **Models** | Commercial LLM (generation), embedding model (retrieval), no separate classifier |
| **Dependencies** | Commercial LLM provider, vector DB, identity provider, HR system of record |
| **Trust boundaries** | User↔App (auth), App↔Vector DB (retrieval authorization), App↔LLM provider (data leaves internal boundary) |
| **Human oversight** | Recruiter reviews every AI recommendation before any hiring action is taken |

## Failure Scenarios Identified (via Failure-Domain Checklist)

| Failure Domain | Applicable? | Scenario |
|---|:---:|---|
| Prompt injection | ✅ | Malicious content embedded in a resume manipulates the LLM into producing biased or manipulated recommendations |
| Unauthorized retrieval | ✅ | Recruiter in Department A retrieves resumes belonging to Department B's applicant pool |
| Data poisoning | ⚠️ Low likelihood | Adversarial resume content designed to skew embeddings |
| Model extraction | ⚠️ Low likelihood | Not a primary concern given commercial LLM provider |
| Privilege abuse | ✅ | Recruiter accesses records outside authorized scope |
| PII disclosure | ✅ | Applicant PII leaked in LLM output or logs |
| Excessive retention | ✅ | Resume data retained beyond policy window |
| Bias / disparate outcomes | ✅ | Recommendation rates differ materially across demographic groups |
| Hallucination | ✅ | LLM fabricates qualifications or experience not present in the resume |
| Instability | ⚠️ Monitor | Same resume/job pairing yields inconsistent recommendations across runs |
| Drift | ✅ | Recommendation patterns shift as model or vendor updates occur |
| Automation bias | ✅ | Recruiters over-trust AI recommendations, reducing effective human oversight |
| Inadequate explanation | ✅ | Recruiters cannot understand why a candidate was scored a given way |
| Vendor outage | ✅ | LLM provider outage halts screening capability |
| Cost exhaustion | ⚠️ Monitor | Unexpected usage spikes drive up API costs |
| Supply-chain changes | ✅ | LLM provider changes underlying model without notice |
| Monitoring/logging failure | ✅ | Retrieval or generation events not captured, breaking audit trail |

## Risks Carried Forward to MEASURE/MANAGE

The four highest-priority risks are tracked as `AIR-001` through `AIR-004` in the [risk register](../../templates/ai-risk-register.xlsx) and detailed in [MANAGE](manage.md):

- `AIR-001` — Prompt injection
- `AIR-002` — Unauthorized retrieval
- `AIR-003` — PII leakage
- `AIR-004` — Hiring bias

Next: [MEASURE →](measure.md)
