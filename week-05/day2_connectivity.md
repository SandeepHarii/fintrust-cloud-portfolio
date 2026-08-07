# Week 5 - Day 2: AWS Connectivity and Application Load Balancer

**Focus:** AWS Connectivity Services, Application Load Balancer (ALB), Path-Based Routing, VPC Peering, Transit Gateway, Direct Connect, Site-to-Site VPN and AWS PrivateLink

**Labs:**
- ALB Path-Based Routing Lab
- AWS SimuLearn: Networking Concepts

**Architecture Diagram:**

![FinTrust ALB Architecture](./diagrams/fintrust_alb_architecture.png)

---

# Overview

This lab focused on designing and configuring the FinTrust Application Load Balancer (ALB) and exploring AWS connectivity services. The ALB was configured with path-based routing to direct traffic to different ECS services, while the networking exercises compared VPC Peering, AWS Transit Gateway, AWS Direct Connect, Site-to-Site VPN, and AWS PrivateLink. These services demonstrated different approaches to connecting AWS resources securely, efficiently, and at enterprise scale.

---

# Application Load Balancer Configuration

| Setting | Value |
|----------|-------|
| Name | fintrust-alb |
| Type | Application Load Balancer |
| Scheme | Internet-facing |
| IP Address Type | IPv4 |
| VPC | fintrust-vpc |
| Availability Zones | af-south-1a, af-south-1b |
| Public Subnets | fintrust-public-1a, fintrust-public-1b |
| Security Group | alb-sg |
| Listener | HTTP :80 (Lab) |

> **Note:** In a production environment, HTTPS (443) with an ACM certificate would be used instead of HTTP.

---

# Target Groups

## api-targets

| Setting | Value |
|----------|-------|
| Protocol | HTTP |
| Port | 8080 |
| Health Check | /api/health |
| Backend | ECS Transaction API Tasks |

---

## portal-targets

| Setting | Value |
|----------|-------|
| Protocol | HTTP |
| Port | 8080 |
| Health Check | /portal/health |
| Backend | ECS Customer Portal Tasks |

---

# Path-Based Routing

| Request Path | Target Group |
|--------------|--------------|
| `/api/*` | api-targets |
| `/portal/*` | portal-targets |
| Default (`*`) | portal-targets |

The Application Load Balancer evaluates each incoming request against its listener rules and forwards it to the appropriate target group based on the request path.

---

# Connectivity Design Worksheet

| Scenario | Best AWS Service | Reason |
|----------|------------------|--------|
| Connect two VPCs | VPC Peering | Simple private connectivity between two VPCs. |
| Connect many VPCs | AWS Transit Gateway | Central networking hub that scales far better than multiple peering connections. |
| Connect FinTrust's on-premises data centre to AWS | AWS Direct Connect | Dedicated private connection with predictable latency and high bandwidth. |
| Secure access to a single service in another VPC | AWS PrivateLink | Exposes only a specific service without exposing the entire VPC. |

---

# Discussion Questions

## When does the default route table of a new VPC already have a "local" route? What does it cover?

When a new VPC is created, AWS automatically adds a **local** route to the default route table. This route covers the entire VPC CIDR block, allowing all subnets within the VPC to communicate with one another. For the FinTrust environment, the local route covers **10.0.0.0/16**.

---

## Your ALB uses path-based routing. What happens to traffic hitting `/payments/*` if no rule exists?

Because no listener rule matches `/payments/*`, the request follows the **default listener rule**. In this configuration, the default action forwards the request to the **portal-targets** target group.

---

## If FinTrust adds a fourth VPC next quarter, how many new connections are required using Transit Gateway versus VPC Peering?

Using **AWS Transit Gateway**, only **one new attachment** is required to connect the new VPC.

Using **VPC Peering**, the fourth VPC requires **three additional peering connections**, one to each of the existing VPCs. As environments grow, Transit Gateway becomes significantly easier to manage.

---

# Individual Reflection

## 1. Explain in your own words why Direct Connect is better than Site-to-Site VPN for FinTrust's mainframe connection.

AWS Direct Connect provides a dedicated private connection between the FinTrust data centre and AWS. Unlike a Site-to-Site VPN, it does not rely on the public internet, resulting in lower latency, higher bandwidth, more consistent performance, and improved reliability. These characteristics make Direct Connect the preferred solution for banking workloads that continuously transfer sensitive financial data.

---

## 2. Describe the path a `/api/transfer` request takes from a user's browser to an ECS container.

```text
User Browser
      │
      ▼
Amazon Route 53
      │
      ▼
Internet Gateway
      │
      ▼
Application Load Balancer (fintrust-alb)
      │
      ▼
Listener Rule (/api/*)
      │
      ▼
api-targets Target Group
      │
      ▼
Amazon ECS Transaction API Task
```

The user's browser sends the request to Route 53, which resolves the FinTrust domain name to the Application Load Balancer. The ALB inspects the URL path, matches the `/api/*` listener rule, forwards the request to the **api-targets** target group, and finally routes it to the appropriate ECS task running inside the private application subnet.

---

## 3. What is the key difference between AWS PrivateLink and VPC Peering?

AWS PrivateLink exposes only a specific application or service through a private endpoint, while keeping the remainder of the VPC isolated.

VPC Peering establishes private network connectivity between two complete VPCs, allowing resources in both VPCs to communicate directly, subject to routing tables and security controls.

---

# Key Learning Points

- Application Load Balancers distribute traffic using listener rules.
- Path-based routing enables multiple applications to share a single load balancer.
- Target Groups route traffic to separate backend services.
- VPC Peering is suitable for connecting a small number of VPCs.
- AWS Transit Gateway simplifies connectivity across large multi-VPC environments.
- AWS Direct Connect provides dedicated enterprise connectivity to AWS.
- AWS PrivateLink securely publishes individual services without exposing an entire VPC.

---

# Lab Completion Summary

| Task | Status |
|------|--------|
| Application Load Balancer created | ✅ |
| Path-based routing configured | ✅ |
| Target Groups configured | ✅ |
| Connectivity design worksheet completed | ✅ |
| Request path walkthrough completed | ✅ |
| Reflection completed | ✅ |

---

# Summary

This lab strengthened my understanding of AWS application networking by demonstrating how Application Load Balancers intelligently route traffic using path-based rules. It also introduced the key AWS connectivity services used to connect VPCs, on-premises environments, and private services. These concepts form the foundation for designing secure, scalable, and highly available enterprise cloud networking architectures.