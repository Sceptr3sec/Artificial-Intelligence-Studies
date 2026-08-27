# AI System Inventory Template

> Copy this file into `case-studies/<system-name>/architecture.md` (or your own assessment folder) and fill in every field before proceeding to GOVERN.

| Field | Value |
|---|---|
| **System** | *e.g., SentinelHire* |
| **Business purpose** | |
| **Business/System owner** | |
| **AI capability** | *e.g., Commercial LLM + RAG, classifier, agentic workflow* |
| **Data** | *What data types does the system ingest?* |
| **Sensitive data** | *PII, PHI, financial data, credentials, etc.* |
| **Users** | *Who directly interacts with or operates the system?* |
| **Affected parties** | *Who is impacted by outputs but doesn't use the system directly?* |
| **External dependencies** | *LLM providers, vector DBs, identity providers, APIs* |
| **Human oversight** | *Is there a human-in-the-loop? Required or optional?* |
| **AI decision authority** | *Advisory only? Autonomous? Partial autonomy with guardrails?* |

## Notes

- This inventory is the anchor artifact for the entire assessment — every later phase (GOVERN, MAP, MEASURE, MANAGE, MONITOR) should reference it.
- Re-validate this inventory whenever the system's capability, data sources, or decision authority changes.

## Next Step

Once complete, proceed to [`framework/01-govern.md`](../framework/01-govern.md).
