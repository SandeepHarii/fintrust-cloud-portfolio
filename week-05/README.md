# Week 5 — AWS Networking

## Overview

Week 5 focused on designing secure, scalable, and highly available AWS networking architectures for the FinTrust banking case study. Morning (AM) sessions explored Amazon VPC, connectivity, load balancing, Route 53, and CloudFront, while afternoon (PM) sessions focused on practical architecture design and networking labs.

Throughout the week, I designed a Multi-AZ VPC, configured an Application Load Balancer with path-based routing, explored AWS connectivity services, implemented Route 53 routing strategies, and secured S3 content delivery using Amazon CloudFront and Origin Access Control (OAC).

---

## What I Learned This Week

### AWS Networking (AM Sessions)

* Designed a highly available Amazon VPC spanning multiple Availability Zones.
* Configured public and private subnets using appropriate CIDR ranges.
* Explored Internet Gateways, NAT Gateways, and route tables.
* Applied Security Groups to control communication between application layers.
* Compared Security Groups and Network ACLs and their stateful and stateless behaviour.
* Explored Application Load Balancers and path-based routing.
* Compared VPC Peering, AWS Transit Gateway, AWS Direct Connect, Site-to-Site VPN, and AWS PrivateLink.
* Configured Amazon Route 53 hosted zones, Alias records, and CNAME records.
* Explored Route 53 routing policies including Simple, Weighted, Failover, Latency, Geolocation, Geoproximity, and Multivalue Answer routing.
* Explored Amazon CloudFront for global content delivery and caching.
* Implemented Origin Access Control (OAC) to securely deliver private S3 content through CloudFront.
* Explored CloudFront cache behaviours, HTTPS enforcement, and cache invalidations.
* Studied how AWS WAF can protect CloudFront distributions from common web application attacks.

### Architecture & Practical Labs (PM Sessions)

* Built a Multi-AZ FinTrust VPC architecture using Draw.io.
* Designed an Application Load Balancer architecture with path-based routing for separate ECS services.
* Designed Route 53 routing architectures for highly available applications.
* Designed a CloudFront architecture using OAC to protect a private S3 bucket.
* Documented request paths through the FinTrust networking architecture.
* Applied AWS networking concepts to production-inspired banking scenarios.
* Completed a timed SAA-C03 mock exam and identified areas requiring further revision.

---

## Repository Contents

| File / Folder                                    | Description                                                                                                           |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| [`day1_vpc_build.md`](./day1_vpc_build.md)       | Multi-AZ VPC build covering subnets, route tables, NAT Gateways, Internet Gateway, Security Groups, and VPC security. |
| [`day2_connectivity.md`](./day2_connectivity.md) | Application Load Balancer configuration, path-based routing, and AWS connectivity service comparisons.                |
| [`day3_route53.md`](./day3_route53.md)           | Route 53 hosted zone configuration, DNS records, weighted routing, and routing policy analysis.                       |
| [`day4_cloudfront.md`](./day4_cloudfront.md)     | CloudFront distribution using Origin Access Control, private S3 storage, caching, and HTTPS configuration.            |
| [`mock_exam_review.md`](./mock_exam_review.md)   | Review of the Week 5 SAA-C03 mock exam, including performance, weak areas, and revision priorities.                   |
| [`reflection.md`](./reflection.md)               | Weekly reflection covering networking concepts, architecture design, challenges, and certification preparation.       |
| [`diagrams/`](./diagrams/)                       | Architecture diagrams covering the FinTrust VPC, ALB, Route 53, and CloudFront designs.                               |

---

## Key Takeaways

* Designed secure Multi-AZ VPC architectures using public and private subnets.
* Understood how Internet Gateways, NAT Gateways, route tables, and Security Groups work together.
* Applied layered network security to control communication between the internet, application, and database layers.
* Learned how Application Load Balancers distribute traffic and support path-based routing.
* Understood when to use VPC Peering, Transit Gateway, Direct Connect, Site-to-Site VPN, and PrivateLink.
* Applied Route 53 routing policies to support availability, performance, and deployment strategies.
* Secured private S3 content using CloudFront and Origin Access Control.
* Improved my ability to read and design AWS architecture diagrams.
* Identified time management and networking scenario analysis as important areas for further SAA-C03 preparation.

---

## Outcome

By the end of Week 5, I developed a much stronger understanding of AWS networking and how individual services integrate into complete cloud architectures. I designed a secure Multi-AZ banking network, implemented load balancing and path-based routing, explored enterprise connectivity options, and built Route 53 and CloudFront architectures.

The practical architecture work also helped me understand how traffic moves through different layers of a cloud environment and why each networking service has a specific role. Combined with the mock exam review, Week 5 strengthened both my technical networking knowledge and my preparation for the AWS Certified Solutions Architect – Associate (SAA-C03) certification.