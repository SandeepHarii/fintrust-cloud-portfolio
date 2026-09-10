# FinTrust Snow Transfer Planner

## Overview

FinTrust has a **3 PB regulatory archive** that needs to be transferred from the on-premises environment to AWS.

Because the archive is very large and contains regulatory data, a physical data transfer approach is appropriate for the initial migration planning. AWS Snowball Edge provides a physical transfer mechanism that can avoid relying entirely on the available internet connection.

AWS documentation lists the Snowball Edge Storage Optimized configuration with up to **80 TB of usable storage per device**.

This document provides a planning calculation for the required device count and compares the data-transfer time against an internet-only transfer.

---

## Planning Inputs

| Item                       |                           Value |
| -------------------------- | ------------------------------: |
| Regulatory archive size    |                            3 PB |
| Archive size in TB         |                        3,000 TB |
| Device type                | Snowball Edge Storage Optimized |
| Usable capacity per device |                           80 TB |
| Planning overhead          |                             10% |
| Effective data volume      |                        3,300 TB |
| Internet comparison speed  |                          1 Gbps |

The 10% overhead is a **planning allowance**, not an AWS requirement. It provides additional capacity for migration overhead and avoids planning the devices at exactly 100% utilisation.

---

## Device Count Calculation

### 1. Add planning overhead

```text
3,000 TB × 1.10 = 3,300 TB
```

The migration plan therefore allows for approximately **3,300 TB** of data capacity.

### 2. Calculate required devices

```text
3,300 TB ÷ 80 TB per device = 41.25 devices
```

Since a partial device cannot be ordered:

```text
Required devices = 42
```

### 3. Result

| Metric                     |       Result |
| -------------------------- | -----------: |
| Archive data               |     3,000 TB |
| Planning overhead          |       300 TB |
| Effective migration volume |     3,300 TB |
| Usable capacity per device |        80 TB |
| Required devices           |       **42** |
| Total device capacity      | **3,360 TB** |
| Remaining planned capacity |    **60 TB** |

The 42-device result is a **planning calculation**, not an actual AWS order or completed migration.

---

## Internet Transfer Comparison

An internet-only transfer is used as the baseline.

Assuming a sustained **1 Gbps** connection:

```text
3 PB × 8 = 24,000,000 Gb
```

At 1 Gbps:

```text
24,000,000 Gb ÷ 1 Gbps
= 24,000,000 seconds
```

This is approximately:

```text
277.8 days
```

So transferring the 3 PB archive over a continuously saturated 1 Gbps connection would take approximately **278 days** before accounting for protocol overhead, retransmissions, competing network traffic, outages, or other operational constraints.

---

## Snowball Data-Transfer Comparison

The Snowball approach changes the problem from continuous internet transfer to physical device transport.

Using the 42-device planning model:

```text
42 × 80 TB = 3,360 TB total usable capacity
```

The devices can be loaded locally and physically transported to AWS rather than sending the entire archive across the internet.

For comparison, the raw data-transfer time on a 10 Gbps local connection would be approximately:

```text
3 PB × 8 ÷ 10 Gbps
= 27.8 days
```

This is a theoretical transfer-time comparison only. Actual Snowball migration duration also depends on device loading speed, number of devices processed in parallel, shipping time, AWS import processing, and operational scheduling.

Therefore, this portfolio does **not** claim a specific end-to-end Snowball delivery time.

---

## Internet vs Physical Transfer

| Approach                   | Planning Basis    |          Approximate Data-Transfer Time |
| -------------------------- | ----------------- | --------------------------------------: |
| Internet                   | 1 Gbps sustained  |                          **277.8 days** |
| Local device loading       | 10 Gbps sustained |                           **27.8 days** |
| Snowball physical transfer | Device-based      | Depends on loading, shipping and import |

### Time-Saved Illustration

Using the theoretical 10 Gbps transfer baseline:

```text
277.8 days − 27.8 days
= 250 days
```

This represents approximately **250 days of data-transfer time avoided** compared with a 1 Gbps internet-only baseline.

This figure is **not an AWS service estimate**. It is a planning comparison based on the stated network-speed assumptions.

---

## FinTrust Migration Approach

The proposed approach is:

```text
3 PB Regulatory Archive
          │
          ▼
   Prepare / Validate Data
          │
          ▼
  Split Archive for Transfer
          │
          ▼
  Load Snowball Devices
          │
          ▼
   Physical Transport
          │
          ▼
       AWS Import
          │
          ▼
   Validate Imported Data
          │
          ▼
   Regulatory Archive in S3
```

The archive should be validated before and after transfer using checksums or equivalent integrity controls.

Because the data is regulatory in nature, encryption, access control, auditability and retention requirements must also be considered as part of the migration design.

---

## Why Snowball Fits the Scenario

The FinTrust archive is large enough that an internet-only migration could take many months when constrained by a 1 Gbps connection.

A physical transfer service is therefore a reasonable migration option when:

* The dataset is very large.
* Available internet bandwidth is limited.
* The migration can tolerate physical device logistics.
* Data integrity can be validated before and after transfer.
* Security and regulatory controls can be maintained throughout the migration.

This aligns with the distinction between online transfer services and physical/offline migration approaches.

---

## Scope and Limitations

This is a **migration planning exercise**, not a live AWS Snowball job.

No Snowball device was ordered or used for this portfolio.

The following values are calculated planning assumptions:

* 3 PB source archive
* 10% planning overhead
* 80 TB usable capacity per device
* 1 Gbps internet comparison
* 10 Gbps local transfer comparison

The calculated result is **42 devices** with **3,360 TB of total planned usable capacity**.

Actual production planning would require confirmation of the available Snow Family device options in the target AWS Region, current service availability, shipping logistics, source network throughput, data preparation time, and AWS import processing requirements.