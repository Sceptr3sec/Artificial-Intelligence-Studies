# 6. MONITOR — Continuous Monitoring

[← MANAGE](04-manage.md) · [Back to README](../README.md)

---

AI risk changes when models, prompts, retrieval data, users, vendors, policies, attack techniques, or business context change. AARF treats MONITOR as an ongoing phase that feeds back into MAP — it is not a one-time close-out step.

## What to Monitor

- Metric thresholds (from [MEASURE](03-measure.md))
- Drift (input/output distribution deviation from validated baseline)
- Guardrail performance (false-negative / false-positive rates)
- Access violations
- Incidents
- Model / provider changes
- Control degradation

## Reassessment Triggers

A significant change in any of the following should trigger a full or partial reassessment, returning to [MAP](02-map.md):

| Trigger | Example |
|---|---|
| Model change | LLM provider upgrades or swaps underlying model |
| Prompt/config change | System prompt, guardrail config, or retrieval logic changes |
| Data change | New data sources added to retrieval corpus |
| User population change | New user group or business unit onboarded |
| Vendor change | Change in subprocessor or infrastructure provider |
| Policy change | New regulatory or contractual obligation |
| Attack technique change | New class of prompt injection or extraction technique observed in the wild |
| Incident | Any confirmed control failure or unauthorized disclosure |

## Suggested Cadence

| Activity | Frequency |
|---|---|
| Metric threshold review | Monthly |
| Drift score review | Weekly (or real-time via dashboard) |
| Guardrail performance review | Monthly |
| Full reassessment | Annually, or immediately on trigger event |
| Access/authorization audit | Quarterly |

## Outputs of This Phase

- Monitoring dashboard or report cadence
- Logged reassessment triggers and outcomes
- Updated [risk register](../templates/ai-risk-register.xlsx) reflecting current state

## See Also

- [Case Study: SentinelHire — Target Profile](../case-studies/sentinelhire/target-profile.md)
