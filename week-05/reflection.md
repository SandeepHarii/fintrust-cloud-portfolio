# Week 5 Reflection

## Overview

Week 5 brought together many of the networking services that form the foundation of AWS solution architecture. Rather than learning each service in isolation, I saw how Amazon VPC, Application Load Balancers, Route 53 and CloudFront work together to securely deliver applications to users. Designing complete architectures using Draw.io helped me understand how requests travel through each networking layer and why each AWS service has a specific role.

---

## What I Learned

Throughout the week I learned how to:

- Design Multi-AZ VPC architectures
- Configure public and private subnets
- Use Internet Gateways and NAT Gateways
- Configure Route Tables
- Apply Security Groups and understand Network ACLs
- Build Application Load Balancers with path-based routing
- Configure Route 53 routing policies
- Secure Amazon S3 with CloudFront and Origin Access Control (OAC)

One of the biggest concepts I learned was the importance of designing for both high availability and security. By distributing resources across multiple Availability Zones, using separate public and private subnets, and controlling traffic with Security Groups and route tables, I built a network that remains resilient while reducing unnecessary exposure to the internet.

---

## Biggest Challenge

The biggest challenge was understanding how the many AWS networking services fit together. Services such as VPC Peering, Transit Gateway, PrivateLink, Direct Connect and Site-to-Site VPN all solve different problems, and choosing the correct solution depends on the business requirements.

---

## How I Overcame It

Building the architecture diagrams and completing each practical lab helped me visualise how requests travel through the network. Seeing the complete architecture made it much easier to understand how each AWS service contributes to the overall solution.

---

## Key Takeaways

- Design for High Availability using multiple Availability Zones.
- Keep application and database resources inside private subnets.
- Use layered security with Security Groups and Network ACLs.
- Select AWS networking services based on business requirements.
- Use Route 53 and CloudFront together to improve performance, availability and security.

---

## Certification Reflection

The Week 5 mock exam highlighted that my biggest challenge is no longer simply understanding AWS services but applying that knowledge efficiently under time pressure.

I scored **46%**, and although this was below my target, I realised many of the questions I missed were due to poor time management rather than a complete lack of understanding. Going forward, I plan to improve both my networking knowledge and my exam strategy by practising more scenario-based questions under timed conditions.

---

## Looking Ahead

In Week 6 I will continue building on these networking concepts while expanding my AWS architecture knowledge as I work towards the AWS Certified Solutions Architect – Associate (SAA-C03) certification.

---

## Final Thoughts

Overall, Week 5 significantly improved my understanding of AWS networking and reinforced how multiple AWS services integrate to build secure, scalable and highly available cloud architectures. It also strengthened my confidence in reading architecture diagrams and selecting the most appropriate AWS service for different networking scenarios.