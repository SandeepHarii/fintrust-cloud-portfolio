# Week 6 - Day 5: FinTrust Security Architecture Summary

## Executive Summary

FinTrust's security architecture combines high availability, controlled identity and access, layered security services, and automated threat detection into a single defence-in-depth approach. The architecture is designed around the requirements of a banking environment where availability, customer data protection, least privilege, monitoring and rapid incident response are critical. Each layer provides a different security or resilience control, while the layers work together to reduce the impact of failures, unauthorised access and security incidents.

## 1. High Availability Layer

The high-availability layer is designed to keep FinTrust's banking application available even if an individual Availability Zone experiences a failure. Application traffic is distributed through an Application Load Balancer to an Auto Scaling Group deployed across two Availability Zones, while Amazon RDS Multi-AZ provides database resilience. Each Availability Zone has its own NAT Gateway to avoid creating a single point of failure for outbound private-subnet connectivity. For disaster recovery, FinTrust uses a **Pilot Light** strategy in `eu-west-1`, providing a secondary recovery environment that can be activated if the primary Region becomes unavailable. The architecture should also define appropriate **RPO and RTO targets** so that recovery expectations are clear to the business.

## 2. Identity and Access Management Layer

The IAM layer separates workforce identity from customer identity because the two groups have fundamentally different access requirements. Approximately 300 employees use **AWS IAM Identity Center** integrated with the company's existing Active Directory, allowing centralised identity management and permission sets based on job responsibilities. Approximately 100,000 customers use **Amazon Cognito with Cognito Identity Pools** to obtain temporary AWS credentials for controlled access to their own S3 data. The DevOps role uses a **Permission Boundary** to limit its maximum permissions, while identity-based policies determine what it is actually allowed to perform. This architecture supports least privilege, separation of duties, centralised workforce access and customer data isolation.

## 3. Security Services Layer

The security services layer provides multiple controls across FinTrust's AWS environment rather than relying on a single security mechanism. **AWS Config** can monitor required resource configurations and compliance rules, while **AWS Secrets Manager** protects application credentials and supports controlled secret rotation. **AWS Certificate Manager (ACM)** manages certificates required for secure HTTPS communication, and **AWS WAF** protects public-facing applications by inspecting and filtering web requests. **AWS Systems Manager Session Manager** provides secure administrative access to managed instances without requiring an internet-facing bastion host. Together, these controls reduce the attack surface, protect sensitive credentials and communications, and provide ongoing visibility into whether resources remain aligned with FinTrust's security requirements.

## 4. Threat Detection and Incident Response Layer

The threat detection layer provides FinTrust with a structured approach to detecting, containing and investigating security incidents. **Amazon GuardDuty** can identify suspicious activity and generate security findings, while **Amazon EventBridge** can detect qualifying findings and trigger **AWS Lambda** to perform an approved response. Lambda can apply a dedicated isolation Security Group to restrict an affected workload while the security team investigates. **VPC Flow Logs** provide network-level evidence, including accepted and rejected traffic, while **AWS CloudTrail** provides evidence of AWS API activity and actions performed within the environment. The proposed response process is **Detect → Trigger → Contain → Investigate → Remediate → Recover**, with automated containment limited to clearly defined high-confidence scenarios and human oversight retained for uncertain or high-impact incidents.

## Conclusion

The four layers work together to provide FinTrust with a resilient and security-focused cloud architecture. The **HA layer** protects application availability, the **IAM layer** controls who can access resources, the **security services layer** protects identities, applications, credentials and infrastructure, and the **threat detection layer** provides the capability to detect, contain and investigate incidents. Together, these layers support a defence-in-depth architecture aligned with the security, availability and operational requirements of a banking environment.