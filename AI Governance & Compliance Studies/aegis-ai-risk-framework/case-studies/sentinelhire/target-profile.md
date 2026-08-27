# SentinelHire — Target Profile

[← Current Profile](current-profile.md) · [Back to README](../../README.md) · Next: [Final Assessment →](final-assessment.md)

---

The Target Profile records the **required state**. SentinelHire moves from Current to Target only when evidence demonstrates that each capability's control and assurance requirements are met.

| Capability | Current | Target State / Evidence Required |
|---|---|---|
| Prompt injection resistance | Not validated | `AIM-001` threshold met (< 0.5%); red-team report on file |
| Retrieval authorization | Cross-department access possible | `AIM-002` = 0% unauthorized retrieval; authorization test report on file |
| PII protection | Partial | `AIM-003` = 0% unauthorized leakage; DLP/access-control evidence on file |
| Human oversight | Informal | Mandatory HITL workflow enforced in system config; configuration and audit evidence on file |
| Fairness assurance | Not tested | `AIM-006`/`AIM-007`/`AIM-008` tested and reviewed against approved thresholds |
| Logging | Outputs only | Full retrieval + generation + access event coverage demonstrated (`AIM-011`) |
| AI incident response | Not established | Approved playbook in place; tabletop exercise completed and documented |
| Model monitoring | Not established | Drift (`AIM-010`) and guardrail performance (`AIM-012`/`AIM-013`) monitored with alert thresholds configured |

## Gap Closure Ownership

Each row's transition from Current → Target is owned by the control owner named in [MANAGE](manage.md) and tracked via [continuous monitoring](../../framework/05-continuous-monitoring.md) once achieved.

Next: [Final Assessment →](final-assessment.md)
