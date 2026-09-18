# Week 11 Reflection

## 1. WAF Pillar Identification

The Well-Architected Framework pillar that was hardest to identify from scenario descriptions was **Performance Efficiency**.

The main confusion was distinguishing Performance Efficiency from Reliability. Both can involve architecture decisions such as scaling, distributed systems, and improving application behaviour. The difference is that Performance Efficiency focuses on using computing resources efficiently and maintaining appropriate performance, while Reliability focuses on the workload's ability to recover from failures and continue operating correctly.

Going forward, I will first identify the main objective of the scenario. If the focus is preventing failures, recovery, availability, or resilience, I will consider Reliability. If the focus is improving performance, selecting efficient resources, or adapting resources to workload demand, I will consider Performance Efficiency.

## 2. SQL Skills

Before this week, I understood the general purpose of window functions, but writing a complete query for running totals and month-over-month growth required more consideration.

I can now use window functions such as `SUM() OVER`, `LAG()`, `ROW_NUMBER()`, and `DENSE_RANK()` to perform transaction analysis while keeping the individual transaction rows available.

I can also use CTEs to break complex queries into smaller stages. The anomaly detection exercise combined multiple CTEs with `LAG()` to calculate month-over-month growth and identify accounts where transaction activity increased by more than 100%.

The most challenging part was understanding how the window function and CTE structure work together. The window function performs the row-level analytical calculation, while the CTEs provide a logical structure for processing the data through multiple stages.

## 3. Python Engineering

A previous data-processing pipeline where `@retry` would be useful is any workflow that makes temporary AWS API calls, such as retrieving S3 object metadata or interacting with other AWS services through boto3.

A retry decorator with exponential backoff can automatically retry a failed API call when the failure may be temporary. This avoids having to duplicate retry logic across every AWS API function.

`ThreadPoolExecutor` would also be useful when a pipeline needs to retrieve metadata or perform multiple independent I/O-bound operations. Instead of waiting for each network request to complete sequentially, multiple requests can be processed concurrently.

For FinTrust, combining reusable retry behaviour with controlled concurrency could make data-processing workflows more resilient and reduce unnecessary waiting when working with independent AWS API operations.