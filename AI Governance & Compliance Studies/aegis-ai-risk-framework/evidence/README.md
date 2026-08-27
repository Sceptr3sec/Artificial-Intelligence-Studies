# Evidence Directory

[← Back to README](../README.md)

---

This directory holds the evidence artifacts referenced by the [metric register](../templates/ai-metric-register.xlsx), [control matrix](../templates/ai-control-matrix.xlsx), and [risk acceptance records](../templates/ai-risk-acceptance.md).

## What Belongs Here

- Test reports (e.g., `AIM-002-test-report.pdf`)
- Red-team / adversarial testing logs
- System logs supporting a control validation claim
- Fairness testing statistical output
- Signed risk acceptance records
- Incident response exercise/tabletop reports
- Audit logging coverage reports

## Naming Convention

```
<metric-or-control-id>-<short-description>-<YYYY-MM-DD>.<ext>
```

Example: `AIM-002-cross-department-retrieval-test-2026-08-27.pdf`

## Why This Matters

AARF's core principle is that a control is not "effective" merely because it is documented or implemented — every claim of control effectiveness must trace to a real evidence artifact:

```
RISK → CONTROL → IMPLEMENTATION → METRIC → TEST → EVIDENCE → RESIDUAL RISK
```

If a metric or control entry references a file in this directory that doesn't exist, the residual risk determination is not valid — treat it as "TBD after test," not "Accept."

## Current Contents

*This is a template repository. Populate this directory with real evidence artifacts as assessments are performed. No evidence files are included by default.*
