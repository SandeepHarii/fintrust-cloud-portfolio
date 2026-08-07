# Week 5 - Day 4: Amazon CloudFront

**Focus:** Amazon CloudFront, Origin Access Control (OAC), HTTPS, Caching, and AWS WAF

**Labs:** LAB 175 and LAB 176 – CloudFront Distribution & OAC

**Architecture Diagram:**

![FinTrust CloudFront and OAC Architecture](./diagrams/fintrust_cloudfront_oac_architecture.png)

---

# Overview

This lab focused on securing the FinTrust customer portal using Amazon CloudFront and Origin Access Control (OAC). The objective was to prevent direct public access to the Amazon S3 bucket while ensuring users access the application securely through CloudFront over HTTPS. The lab also explored CloudFront caching behaviour, AWS WAF integration, and best practices for delivering static content with low latency.

---

# CloudFront Distribution Configuration

| Setting                | Value                       |
| ---------------------- | --------------------------- |
| Distribution Type      | Web Distribution            |
| Origin                 | fintrust-portal-assets      |
| Origin Access          | Origin Access Control (OAC) |
| Viewer Protocol Policy | Redirect HTTP to HTTPS      |
| Default Root Object    | index.html                  |
| Region                 | Global (CloudFront)         |

---

# Amazon S3 Origin

| Setting                | Value                  |
| ---------------------- | ---------------------- |
| Bucket Name            | fintrust-portal-assets |
| Region                 | af-south-1             |
| Public Access          | Blocked                |
| Server-Side Encryption | SSE-S3                 |
| Access Method          | CloudFront OAC Only    |

The S3 bucket stores the static website assets while remaining completely private. Users cannot access the bucket directly because all requests are authenticated through CloudFront using Origin Access Control.

---

# Cache Behaviours

| Path Pattern  | Cache Policy     | Purpose                |
| ------------- | ---------------- | ---------------------- |
| Default (`*`) | Managed Caching  | Static website content |
| `/api/*`      | Caching Disabled | Dynamic API requests   |

Static assets benefit from CloudFront edge caching to improve performance and reduce latency, while API requests bypass the cache to ensure users always receive the latest application data.

---

# Bucket Policy

The bucket policy grants access only to the CloudFront distribution using Origin Access Control (OAC). Direct requests from the public internet are denied, ensuring that all traffic flows securely through CloudFront.

---

# Request Flow

```text
User
   │
   ▼
Amazon Route 53
   │
   ▼
Amazon CloudFront
   │
   ▼
Origin Access Control (OAC)
   │
   ▼
Private Amazon S3 Bucket
(fintrust-portal-assets)
```

Users access the application through Route 53, which resolves the domain name to the CloudFront distribution. CloudFront authenticates itself to Amazon S3 using OAC, retrieves the required objects, caches them at edge locations, and serves them securely over HTTPS.

---

# Complete Week 5 Network Architecture

```text
Users
   │
   ▼
Amazon Route 53
• Hosted Zone
• Weighted Routing
• Failover Routing
• Health Checks
   │
   ▼
Amazon CloudFront
• HTTPS Enforcement
• Origin Access Control (OAC)
• Edge Caching
• Cache Behaviours
   │
   ▼
Application Load Balancer
(fintrust-alb)
• /api/*
• /portal/*
   │
   ▼
fintrust-vpc (10.0.0.0/16)

Availability Zone af-south-1a
• Public Subnet
• NAT Gateway
• Application Subnet
• Data Subnet

Availability Zone af-south-1b
• Public Subnet
• NAT Gateway
• Application Subnet
• Data Subnet

Security Groups

Internet
   │
alb-sg
   │
app-sg
   │
db-sg

Storage

Private Amazon S3 Bucket
(fintrust-portal-assets)
```

---

# Discussion Questions

## Where does AWS WAF sit when attached to a CloudFront distribution, and what attacks can it prevent?

AWS WAF sits in front of the CloudFront distribution and inspects incoming requests before they reach CloudFront or the origin. Requests matching configured security rules can be blocked before they reach the application.

AWS WAF can help prevent:

* SQL Injection (SQLi)
* Cross-Site Scripting (XSS)
* Malicious bots
* IP reputation attacks
* HTTP flood attacks
* Requests from blocked countries or IP ranges

### Request Path

```text
User
   │
   ▼
AWS WAF
   │
   ▼
Amazon CloudFront
   │
   ▼
Origin (Amazon S3 or ALB)
```

---

## You need to place CloudFront in front of an Application Load Balancer instead of Amazon S3. How does the architecture change?

Instead of using Amazon S3 as the origin, the Application Load Balancer becomes the CloudFront origin.

```text
User
   │
   ▼
Amazon Route 53
   │
   ▼
Amazon CloudFront
   │
   ▼
Application Load Balancer
   │
   ▼
Amazon ECS Tasks
```

CloudFront continues to provide HTTPS enforcement, edge caching, DDoS protection, and improved global performance, while forwarding dynamic requests to the Application Load Balancer.

---

# Individual Reflection

## 1. Explain the difference between Origin Access Control (OAC) and Origin Access Identity (OAI). Why is OAC preferred?

Origin Access Identity (OAI) is the older method used to allow CloudFront to access private Amazon S3 buckets.

Origin Access Control (OAC) is the newer and recommended approach. It uses AWS Signature Version 4 (SigV4) to authenticate requests from CloudFront to Amazon S3, providing stronger security, broader feature support, and better integration with modern AWS services.

For new deployments, AWS recommends using OAC instead of OAI.

---

## 2. Describe one scenario where you would use CloudFront in front of an Application Load Balancer rather than directly serving content from Amazon S3.

CloudFront should be placed in front of an Application Load Balancer when serving dynamic web applications. For example, the FinTrust online banking portal processes user authentication, account balances, and money transfers through Amazon ECS services behind an ALB. These requests require backend processing and cannot be served directly from Amazon S3.

---

## 3. Your CloudFront distribution caches `/static/*` for one day (TTL = 86,400 seconds). A developer deploys an urgent CSS fix. How do you make users receive the update immediately?

The quickest solution is to create a CloudFront invalidation for the updated object, such as `/static/styles.css`, or invalidate `/static/*` if multiple files changed. This removes the cached content from CloudFront edge locations so users receive the latest version immediately instead of waiting for the TTL to expire.

---

# Key Learning Points

* Amazon CloudFront improves both performance and security by caching content at edge locations.
* Origin Access Control (OAC) keeps Amazon S3 buckets private while allowing CloudFront to retrieve objects securely.
* Viewer Protocol Policies enforce HTTPS connections.
* Cache behaviours allow different caching strategies for static and dynamic content.
* AWS WAF protects CloudFront distributions against common web application attacks.

---

# Lab Completion Summary

| Task                                    | Status |
| --------------------------------------- | ------ |
| Private Amazon S3 bucket created        | ✅      |
| Block Public Access enabled             | ✅      |
| CloudFront distribution configured      | ✅      |
| Origin Access Control (OAC) implemented | ✅      |
| Bucket policy updated                   | ✅      |
| HTTPS enforced                          | ✅      |
| `/api/*` cache behaviour configured     | ✅      |
| OAC vs OAI comparison completed         | ✅      |
| Architecture documented                 | ✅      |
| Reflection completed                    | ✅      |

---

# Summary

This lab demonstrated how Amazon CloudFront securely delivers static content from a private Amazon S3 bucket using Origin Access Control. By blocking direct public access to Amazon S3, enforcing HTTPS, configuring cache behaviours, and integrating with AWS WAF, the FinTrust customer portal benefits from improved security, lower latency, and greater scalability while following AWS Well-Architected best practices.