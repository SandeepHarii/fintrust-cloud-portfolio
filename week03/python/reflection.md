# Week 3 Reflection

## 1. Storage Service Choice

For the FinTrust compliance archive, which requires a minimum five-year POPIA retention period, I would use **Amazon S3 Standard** for active archival storage together with **S3 Object Lock (Compliance Mode)** to prevent records from being modified or deleted before the retention period expires. I would enable **server-side encryption using AWS KMS (SSE-KMS)** to protect sensitive customer data and apply a bucket policy that restricts access to authorised users and services. This approach provides secure, compliant, and durable long-term storage while supporting regulatory requirements.

---

## 2. Most Challenging Python Concept

The most challenging Python concept this week was working with **file input/output (File I/O)** and handling different error scenarios correctly. Understanding when to use exception handling, particularly with `try`, `except`, `else`, and `finally`, took some practice. Reviewing the examples, testing different scenarios, and reading the error messages helped me understand how to build applications that handle unexpected situations more reliably.

---

## 3. Real-Project Application

If I started a cloud project tomorrow, I would apply **Amazon S3 together with CloudFront** to build a secure and scalable storage solution for static content. The FinTrust case study demonstrated how cloud storage, access control, and content delivery work together to provide reliable services while maintaining security. These are practical skills that are directly applicable to modern cloud-based applications and align with my goal of building secure, scalable solutions on AWS.