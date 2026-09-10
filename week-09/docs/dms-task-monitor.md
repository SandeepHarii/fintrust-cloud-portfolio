# DMS Task Monitor

## Overview

The FinTrust DMS Task Monitor demonstrates how Database Migration Service (DMS) replication tasks can be monitored during a migration programme.

The implementation focuses on checking replication task status, identifying active tasks, detecting terminal states, and determining when further investigation may be required.

The Python implementation uses simulated task data because the Week 9 practical work was completed without directly provisioning or modifying AWS services.

## What the Monitor Polls

A production implementation would use the AWS DMS `DescribeReplicationTasks` API to retrieve the current state of replication tasks.

The monitor would poll information such as:

* Replication task identifier
* Current task status
* Migration type
* Replication task state

The local implementation represents these values using simulated task data.

## Task States

The monitor distinguishes between active and terminal task states.

Terminal states used by the implementation are:

| State     | Meaning                                | Monitoring Action                     |
| --------- | -------------------------------------- | ------------------------------------- |
| `stopped` | Replication task has stopped           | Confirm whether the stop was expected |
| `failed`  | Replication task encountered a failure | Investigate the migration failure     |
| `deleted` | Replication task has been removed      | Confirm that deletion was intentional |

Other states are treated as non-terminal and remain subject to continued monitoring.

## Local Implementation

The script:

1. Loads simulated DMS replication task information.
2. Reads the status of each task.
3. Classifies each task as active or terminal.
4. Identifies failed, stopped, and deleted tasks.
5. Provides an action recommendation based on the task state.
6. Produces a monitoring summary.

This provides a local representation of the monitoring logic without requiring an active AWS DMS environment.

## Production Adaptation

In a production FinTrust environment, the simulated task data could be replaced with a `boto3` DMS client and the `describe_replication_tasks` API.

The monitoring process could then be structured as:

```text
EventBridge Schedule
        ↓
AWS Lambda
        ↓
AWS DMS API
        ↓
Replication Task Status
        ↓
Status Evaluation
        ↓
Logging / Alerting
```

Amazon EventBridge could trigger the monitoring function on a scheduled interval.

AWS Lambda could execute the Python monitoring logic without requiring a continuously running server.

The function could retrieve current DMS task states, identify terminal or failed tasks, and send an alert when investigation is required.

## FinTrust Use Case

FinTrust has a large server fleet requiring migration planning and execution. DMS task monitoring can support database migration workloads by providing visibility into replication progress and identifying tasks requiring attention.

For example, a failed replication task could trigger an operational investigation before the migration proceeds to its next stage.

This supports a controlled migration approach by combining migration execution with automated monitoring.

## Portfolio Scope

No live AWS DMS task monitoring was performed for this portfolio entry.

The implementation is intentionally limited to a local simulation and production design. AWS API calls are documented as commented production guidance rather than executed against live infrastructure.

No live task identifiers, migration results, or AWS monitoring metrics are claimed.

## Outcome

The DMS Task Monitor demonstrates the Python logic required to monitor replication task states and provides a clear path from local implementation to a production AWS Lambda and EventBridge solution.