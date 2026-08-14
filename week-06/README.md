# Week 6 — AWS Security

## Overview

Week 6 focused on designing secure AWS environments for the FinTrust banking application. The week covered identity and access management, AWS security services, encryption, data protection, network and application security, threat detection, monitoring, auditing, and incident response.

The practical work focused on applying these concepts to the FinTrust environment. This included designing workforce and customer identity solutions using IAM Identity Center and Amazon Cognito, evaluating AWS security services for different banking requirements, and designing an incident-response architecture using GuardDuty, EventBridge, Lambda and Security Groups.

Day 1 was a public holiday, so no training activities were completed.

---

## What I Learned This Week

### AWS (AM Sessions)

* Explored advanced AWS Identity and Access Management concepts.
* Learnt how AWS IAM manages users, roles, policies and permissions.
* Designed workforce identity management using AWS IAM Identity Center and Active Directory.
* Designed customer identity management using Amazon Cognito and Cognito Identity Pools.
* Applied Permission Boundaries to limit the maximum permissions available to an IAM role.
* Applied least privilege and separation of duties to the FinTrust security architecture.
* Explored AWS security services covering identity, encryption, data protection, network security, application security, threat detection, monitoring and compliance.
* Studied AWS Key Management Service (KMS), AWS CloudHSM and AWS Secrets Manager.
* Explored AWS Certificate Manager, AWS WAF, AWS Shield and AWS Network Firewall.
* Studied Amazon Macie for sensitive-data discovery in Amazon S3.
* Explored Amazon GuardDuty, Amazon Inspector, Amazon Detective and AWS Security Hub for threat detection and investigation.
* Studied AWS CloudTrail, Amazon CloudWatch and AWS Config for monitoring, auditing and compliance.
* Explored AWS Systems Manager Session Manager for secure administrative access to managed instances.
* Studied AWS Audit Manager and its role in collecting evidence for compliance assessments.
* Designed an incident-response workflow using Amazon GuardDuty, Amazon EventBridge, AWS Lambda and an isolation Security Group.
* Explored VPC Flow Logs and AWS CloudTrail as sources of evidence during security investigations.
* Applied defence in depth, rapid containment, least privilege and human oversight to incident-response design.
* Distinguished between security services that should be used, services that may be considered, and services that are requirement-dependent for FinTrust.
* Synthesised the week's security work into a layered FinTrust security architecture suitable for presenting to a CISO.

### Python & SQL (PM Sessions)

* Continued Python security automation concepts.
* Worked with Python and boto3 for AWS-related automation.
* Continued SQL development through the programme's practical exercises, including SQL Window Functions.

---

## Repository Contents

| File / Folder | Description |
| --- | --- |
| [`day2_iam_design.md`](./day2_iam_design.md) | FinTrust IAM design covering workforce identity, customer identity, Cognito Identity Pools, and Permission Boundaries. |
| [`day3_security_services.md`](./day3_security_services.md) | AWS security services covered during the week and their recommended use within the FinTrust environment. |
| [`day4_incident_response.md`](./day4_incident_response.md) | FinTrust incident-response design using GuardDuty, EventBridge, Lambda, Security Groups, VPC Flow Logs, and CloudTrail. |
| [`day5_security_architecture_summary.md`](./day5_security_architecture_summary.md) | CISO-facing synthesis of the FinTrust high-availability, IAM, security services, and threat detection layers. |
| [`reflection.md`](./reflection.md) | Weekly reflection covering AWS security concepts, challenges, key takeaways, and certification preparation. |
| [`diagrams/`](./diagrams/) | Architecture diagrams supporting the FinTrust IAM, security services, and incident-response designs. |

---

## Key Takeaways

* Workforce and customer identities should be managed separately because they have different access requirements.
* IAM Identity Center can provide centralised workforce access using existing corporate identities and permission sets.
* Amazon Cognito can provide customer authentication and temporary AWS credentials through Cognito Identity Pools.
* Permission Boundaries limit the maximum permissions an IAM role can receive without directly granting permissions.
* Least privilege and separation of duties are essential security principles for a banking environment.
* AWS provides specialised security services for identity, encryption, application protection, threat detection, monitoring and compliance.
* Security services should be selected based on FinTrust's requirements rather than deploying every available security service.
* GuardDuty can provide managed threat detection for suspicious activity.
* EventBridge can trigger automated responses to qualifying security findings.
* Lambda can perform approved security-response actions using least-privilege permissions.
* Isolation Security Groups can provide rapid containment of affected workloads.
* VPC Flow Logs provide network-level evidence during security investigations.
* CloudTrail provides AWS API activity and audit evidence.
* Automated incident response should include human oversight for uncertain or high-impact security findings.
* Defence in depth combines multiple security controls rather than relying on a single security service.
* The different security layers need to work together as one architecture rather than being treated as isolated services.

---

## Outcome

By the end of Week 6, I developed a stronger understanding of how AWS security services can be combined to protect a banking environment.

I designed a FinTrust identity architecture that separates workforce access from customer access, using IAM Identity Center and Active Directory for employees and Amazon Cognito with Cognito Identity Pools for customers. I also applied Permission Boundaries to limit the maximum permissions available to privileged roles.

I evaluated a broad range of AWS security services and identified which services would provide the most value for FinTrust's identity management, encryption, data protection, application security, threat detection, monitoring and compliance requirements.

I also designed an incident-response architecture that connects GuardDuty, EventBridge, Lambda and Security Groups to support automated containment, while VPC Flow Logs and CloudTrail provide evidence for investigation.

The final Day 5 synthesis brought these concepts together into a coherent FinTrust security architecture, showing how the high-availability, IAM, security services and threat detection layers work together from a CISO perspective.

The week's work reinforced that effective AWS security is based on layered controls, least privilege, centralised identity management, monitoring, threat detection and appropriate human oversight rather than relying on a single security service.

---

## Week 6 Activities

| Day | Topic | Outcome |
| --- | --- | --- |
| Day 1 | Public Holiday | No training activities completed. |
| Day 2 | IAM Advanced | Designed workforce and customer identity solutions and applied Permission Boundaries. |
| Day 3 | AWS Security Services | Evaluated AWS security services and designed a layered FinTrust security architecture. |
| Day 4 | Observability & Threat Detection | Designed an incident-response workflow and explored security investigation evidence. |
| Day 5 | Security Architecture Synthesis | Combined the week's security work into a CISO-facing FinTrust security architecture summary. |

---

## Week 6 Deliverables

| Day | Deliverable | Description |
| --- | --- | --- |
| Day 1 | HA Architecture Diagram | High-availability FinTrust architecture showing an ALB, Auto Scaling Group across two Availability Zones, Multi-AZ RDS, separate NAT Gateways, Pilot Light disaster recovery and RPO/RTO values. |
| Day 2 | IAM Design Decision Doc | Workforce and customer identity design using IAM Identity Center, Active Directory, Amazon Cognito, Cognito Identity Pools and Permission Boundaries. |
| Day 3 | Security Services Config Summary | Summary of the security services selected for FinTrust, including their configuration requirements and reasons for their use. |
| Day 4 | Incident Response Flow Diagram | Incident-response design showing the EventBridge → Lambda → isolation Security Group response chain, supported by GuardDuty, VPC Flow Logs and CloudTrail. |
| Day 5 | Security Architecture Summary | CISO-facing synthesis explaining how the HA, IAM, security services and threat detection layers work together. |

---

## Week 6 Security Architecture

The week's work builds toward a layered FinTrust security model:

**Identity → Application → Network → Data → Threat Detection → Monitoring & Audit**

The incident-response design extends this model by connecting security findings to automated containment:

**GuardDuty → EventBridge → Lambda → Isolation Security Group**

Supporting investigation evidence is provided through:

**VPC Flow Logs + CloudTrail**

The final architecture brings these controls together with the high-availability and identity designs to create a security model that addresses availability, access control, protection, detection, containment and investigation.

---

## Practical vs Theoretical Coverage

Not every AWS security service discussed during Week 6 was deployed as part of the FinTrust environment.

The IAM work included hands-on activity through **Lab 279: Introduction to IAM**, while many of the other security services were covered through theory, reading, discussions and architecture design.

The incident-response workflow using:

**GuardDuty → EventBridge → Lambda → Isolation Security Group**

was designed as a proposed FinTrust architecture rather than deployed as a complete end-to-end automated incident-response lab.

The security services covered during the week should therefore be distinguished between services actually configured, services evaluated for FinTrust, and services proposed based on the target architecture.

Where evidence does not exist for an actual configuration, the portfolio treats the relevant architecture or configuration as theoretical, simulated or proposed rather than claiming that it was deployed.

---

## Links

- [Day 2 - IAM Design](./day2_iam_design.md)
- [Day 3 - Security Services](./day3_security_services.md)
- [Day 4 - Incident Response](./day4_incident_response.md)
- [Day 5 - Security Architecture Summary](./day5_security_architecture_summary.md)