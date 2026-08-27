# 3. MAP — Understand the System in Context

[← GOVERN](01-govern.md) · [Back to README](../README.md) · Next: [MEASURE →](03-measure.md)

---

MAP is the AI threat- and risk-modeling phase. It identifies what can go wrong, who can be harmed, what assumptions the system depends on, and where trust changes across the architecture.

## Mapping Domains

| Domain | Questions / Examples |
|---|---|
| **Users** | Who operates, administers, or relies on the AI? |
| **Affected parties** | Who experiences consequences even if they never use the system? |
| **Data** | What data enters, is embedded, retrieved, logged, retained, or leaves the boundary? |
| **Models** | LLM, embedding model, classifiers, guardrails, scoring models |
| **Dependencies** | Identity, vector DB, databases, APIs, vendors, logging, HR systems |
| **Trust boundaries** | Where does identity, authorization, data, or control cross between components? |
| **Human oversight** | Who reviews outputs and can override or stop the system? |
| **Failure scenarios** | Security, privacy, fairness, reliability, human-factor, operational, supply-chain risks |

## Failure-Domain Checklist

Use this checklist during threat modeling sessions to ensure coverage across categories:

- [ ] Prompt injection
- [ ] Unauthorized retrieval
- [ ] Data poisoning
- [ ] Model extraction
- [ ] Privilege abuse
- [ ] PII disclosure
- [ ] Excessive retention
- [ ] Bias and disparate outcomes
- [ ] Hallucination
- [ ] Instability
- [ ] Drift
- [ ] Automation bias
- [ ] Inadequate explanation
- [ ] Vendor outage
- [ ] Cost exhaustion
- [ ] Poisoned inputs
- [ ] Supply-chain changes
- [ ] Monitoring/logging failure

## How to Use This Phase

1. Draw the system architecture, including every external dependency.
2. Mark every point where a trust boundary is crossed (e.g., user → API, API → LLM provider, LLM → vector DB).
3. For each boundary, walk the failure-domain checklist and note which failure modes are plausible.
4. Feed each identified risk into the [MEASURE](03-measure.md) phase to define how it will be tested.

## Outputs of This Phase

- System architecture diagram with trust boundaries annotated
- List of affected parties beyond direct users
- List of plausible failure scenarios, mapped to failure domains
- Input list for the [risk register](../templates/ai-risk-register.xlsx)

## See Also

- [Case Study: SentinelHire — Architecture](../case-studies/sentinelhire/architecture.md)
- [Case Study: SentinelHire — MAP](../case-studies/sentinelhire/map.md)
