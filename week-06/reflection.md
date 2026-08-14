# Week 6 Reflection

## Overview

Week 6 focused on AWS security and how different security controls can work together to protect a banking environment. Rather than looking at security as a single AWS service, I learned how identity management, application protection, data protection, monitoring, threat detection and incident response can form different layers of a larger security architecture. Applying these concepts to the FinTrust environment helped me understand how security decisions should be based on business requirements rather than simply deploying every security service available.

---

## What I Learned

One of the biggest areas I developed this week was identity and access management. I learned that workforce identities and customer identities should be treated differently because they have different requirements. For FinTrust employees, IAM Identity Center integrated with Active Directory provides centralised workforce access and permission sets, while Amazon Cognito and Cognito Identity Pools can provide customers with controlled access using temporary credentials. I also gained a better understanding of Permission Boundaries and how they limit the maximum permissions an IAM role can receive without directly granting permissions.

I also explored a much broader range of AWS security services, including KMS, Secrets Manager, ACM, WAF, Shield, Config, GuardDuty, Inspector, Detective, Security Hub, CloudTrail, CloudWatch, Macie and Systems Manager Session Manager. The important lesson was that these services do not all solve the same problem. Some protect identities and data, some protect applications and networks, while others provide monitoring, threat detection or investigation capabilities. This helped me understand the importance of selecting security controls based on the actual requirements of an environment.

The incident-response work helped connect these concepts together. I learned how GuardDuty can detect suspicious activity, EventBridge can respond to relevant security findings, and Lambda can perform an approved automated containment action. An isolation Security Group can then restrict an affected workload while VPC Flow Logs and CloudTrail provide evidence for investigation. I also learned that automation should be used carefully. Not every security finding should automatically result in isolation, particularly when the response could disrupt legitimate workloads.

---

## Biggest Challenge

The biggest challenge this week was understanding the large number of AWS security services and determining where each one fits within an overall architecture. Many of the services have related security purposes, so simply memorising their names is not enough. I needed to understand the problem each service solves and when FinTrust would actually benefit from using it.

---

## How I Overcame It

Working with the FinTrust banking scenario made the security concepts easier to understand because I could connect each service to a specific requirement. The IAM design showed how employee and customer identities could be separated, while the security services work helped me compare different controls based on their purpose. The incident-response architecture also helped me understand how multiple services can work together rather than operating independently.

The architecture diagrams were particularly useful because they allowed me to see how the different security layers connect. This made concepts such as defence in depth, least privilege, monitoring and rapid containment much easier to understand in a practical context.

---

## Key Takeaways

The biggest takeaway from Week 6 is that AWS security is about layers and appropriate controls, not simply using as many security services as possible.

I also learned that identity is one of the foundations of a secure AWS environment. Workforce access, customer access and privileged roles should have different controls based on their requirements.

Another important lesson was the difference between detection and response. Detecting suspicious activity is only the beginning. A secure architecture also needs a way to investigate the event, contain the affected resource, preserve evidence and eventually recover the workload.

---

## Certification Reflection

Week 6 strengthened my understanding of several security concepts that are important for the AWS Certified Solutions Architect – Associate exam. In particular, I became more comfortable distinguishing between IAM roles, policies, permission boundaries, IAM Identity Center and Cognito, as well as understanding the different purposes of services such as WAF, Shield, GuardDuty, Inspector and Security Hub.

The week also reinforced that SAA-C03 questions are often about choosing the most appropriate solution for a specific requirement rather than simply identifying an AWS service. Understanding why a service is appropriate is therefore more useful than memorising definitions.

---

## Looking Ahead

Going forward, I want to continue strengthening my ability to read AWS scenarios and identify the security requirement before thinking about the specific service. I also want to keep connecting the theory to the FinTrust architecture so that the services become easier to recognise in real-world scenarios and certification questions.

---

## Final Thoughts

Overall, Week 6 gave me a much broader understanding of AWS security. I moved from thinking about individual security services to thinking about how identity, protection, monitoring, detection and incident response work together as part of a larger architecture. The FinTrust exercises helped me see how these concepts could be applied to a realistic banking environment while also showing me that good security design is about choosing the right controls, applying least privilege and maintaining appropriate human oversight.