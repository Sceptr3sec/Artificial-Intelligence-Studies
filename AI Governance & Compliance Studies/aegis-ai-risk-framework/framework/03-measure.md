# 4. MEASURE — Convert Risk into Evidence

[← MAP](02-map.md) · [Back to README](../README.md) · Next: [MANAGE →](04-manage.md)

---

MEASURE defines how risk is tested. A useful metric has:

1. A **formula**
2. A **test method**
3. A **dataset / sample size**
4. An **acceptance threshold**
5. An **observed result**
6. A **pass/fail decision**
7. An **evidence artifact**
8. A **test date**
9. A **retest date**

Without all nine, a metric is not yet actionable — it's a placeholder.

## Metric Catalog

| ID | Metric | Illustrative Definition / Target |
|---|---|---|
| `AIM-001` | Prompt Injection Success Rate | Successful malicious instruction executions ÷ total injection attempts; target **< 0.5%** |
| `AIM-002` | Unauthorized Retrieval Rate | Unauthorized documents retrieved ÷ unauthorized retrieval attempts; target **0%** |
| `AIM-003` | PII Leakage Rate | Responses containing unauthorized PII ÷ tested responses; target **0%** |
| `AIM-004` | Hallucination Rate | Unsupported material claims ÷ evaluated material claims |
| `AIM-005` | Response Stability | Variance across repeated equivalent evaluations |
| `AIM-006` | Demographic Parity Gap | Difference in selection/recommendation rates across evaluated groups |
| `AIM-007` | Equal Opportunity Difference | Difference in true-positive rates across evaluated groups |
| `AIM-008` | Adverse Impact Ratio | Selection-rate comparison used as a screening indicator for disparate outcomes |
| `AIM-009` | Human Override Rate | Human overrides ÷ AI recommendations |
| `AIM-010` | Drift Score | Deviation of live input/output distributions from validated baseline |
| `AIM-011` | Logging Coverage | Required auditable events captured ÷ required events |
| `AIM-012` | Guardrail False-Negative Rate | Attacks bypassing guardrails ÷ attacks tested |
| `AIM-013` | Guardrail False-Positive Rate | Benign requests blocked ÷ benign requests tested |

## Metric Record Format

Every metric entry in the [metric register](../templates/ai-metric-register.xlsx) should follow this record shape:

```yaml
id: AIM-002
name: Unauthorized Retrieval Rate
formula: unauthorized_documents_retrieved / unauthorized_retrieval_attempts
test_method: Cross-department retrieval attack simulation
dataset: 1,000 cross-department retrieval attempts
threshold: "0%"
observed_result: pending
decision: pending
evidence_artifact: evidence/AIM-002-test-report.pdf
test_date: pending
retest_date: pending
```

## Outputs of This Phase

- A completed [metric register](../templates/ai-metric-register.xlsx) with thresholds set
- A test plan for each risk identified in [MAP](02-map.md)
- Evidence artifacts collected in [`/evidence`](../evidence/README.md)

## See Also

- [Case Study: SentinelHire — MEASURE](../case-studies/sentinelhire/measure.md)
- [Future: Python Assurance Toolkit](../README.md#-roadmap)
