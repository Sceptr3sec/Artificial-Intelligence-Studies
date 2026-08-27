# 2. GOVERN — Establish the Rules of Risk

[← Back to README](../README.md) · Next: [MAP →](02-map.md)

---

GOVERN establishes who is accountable, who can accept risk, what policies and external obligations apply, how incidents are handled, and what outcomes the organization is unwilling to tolerate. It is the foundation phase — every later phase (MAP, MEASURE, MANAGE, MONITOR) inherits its authority and boundaries from decisions made here.

## Required Roles

| Role | Responsibility |
|---|---|
| **Business owner** | Owns the business outcome the AI system supports |
| **System owner** | Owns technical operation of the system |
| **AI risk owner(s)** | Owns identification and tracking of AI-specific risk |
| **Control owners** | Responsible for implementing and maintaining individual controls |
| **Risk acceptance authority** | Authorized to formally accept residual risk |
| **Security authority** | Owns security architecture and testing sign-off |
| **Data owner** | Accountable for data used, retained, and disclosed by the system |
| **Legal/Compliance stakeholders** | Ensure regulatory and contractual obligations are met |
| **Incident-response roles** | Own detection, escalation, and remediation of AI incidents |

## Governance Inputs

- Organizational policies
- Legal and regulatory requirements
- Contractual obligations
- Industry standards
- AI-specific policies
- Human-in-the-loop (HITL) requirements
- Data governance
- Access control
- Vendor governance
- Records / logging requirements
- Incident response
- Model / configuration change management

## Illustrative Risk Tolerance

Risk tolerance should be set *before* MEASURE defines thresholds — tolerance drives thresholds, not the other way around.

| Risk Domain | Tolerance |
|---|:---:|
| Unauthorized PII disclosure | Zero |
| Unauthorized retrieval | Zero |
| Autonomous hiring rejection | Zero |
| Material discriminatory outcomes | Very low |
| Prompt injection success | Low |
| Hallucinated qualifications | Low |
| Temporary availability loss | Moderate |

## Outputs of This Phase

- A named risk acceptance authority for the system
- A documented risk tolerance table
- Confirmed applicable policies/regulations
- Escalation and incident-response ownership

## See Also

- [System Inventory Template](../templates/ai-system-inventory.md)
- [Case Study: SentinelHire — GOVERN](../case-studies/sentinelhire/govern.md)
