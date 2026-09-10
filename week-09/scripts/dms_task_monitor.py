import boto3
import time
from datetime import datetime


dms = boto3.client(
    "database-migration-service",
    region_name="af-south-1"
)


def get_task_progress(task_arn):
    """
    Returns a summary of a DMS replication task's
    current progress.
    """

    response = dms.describe_replication_tasks(
        Filters=[
            {
                "Name": "replication-task-arn",
                "Values": [task_arn]
            }
        ]
    )

    if not response["ReplicationTasks"]:
        return None

    task = response["ReplicationTasks"][0]
    stats = task.get(
        "ReplicationTaskStats",
        {}
    )

    return {
        "task_id": task["ReplicationTaskIdentifier"],
        "status": task["Status"],
        "tables_loaded": stats.get(
            "TablesLoaded",
            0
        ),
        "tables_loading": stats.get(
            "TablesLoading",
            0
        ),
        "tables_errored": stats.get(
            "TablesErrored",
            0
        ),
        "tables_queued": stats.get(
            "TablesQueued",
            0
        ),
        "full_load_pct": stats.get(
            "FullLoadProgressPercent",
            0
        ),
        "elapsed_seconds": stats.get(
            "ElapsedTimeMillis",
            0
        ) // 1000,
        "start_time": task.get(
            "ReplicationTaskStartDate",
            "not started"
        ),
    }


def monitor_task(
    task_arn,
    poll_interval=30,
    max_polls=20
):
    """
    Poll a DMS task until it reaches a terminal
    state or max_polls is reached.
    """

    terminal = {
        "stopped",
        "failed",
        "deleting"
    }

    for i in range(max_polls):

        progress = get_task_progress(
            task_arn
        )

        if not progress:
            print("Task not found.")
            break

        ts = datetime.now().strftime(
            "%H:%M:%S"
        )

        print(
            f'[{ts}] Status: '
            f'{progress["status"]} | '
            f'Full load: '
            f'{progress["full_load_pct"]}% | '
            f'Loaded: '
            f'{progress["tables_loaded"]} | '
            f'Errored: '
            f'{progress["tables_errored"]}'
        )

        if progress["status"] in terminal:
            print(
                f'Task reached terminal state: '
                f'{progress["status"]}'
            )
            break

        time.sleep(poll_interval)


# Usage:
# Replace with a real task ARN from the DMS console.
#
# monitor_task(
#     "arn:aws:dms:af-south-1:123456789012:task:ABCDEFGHIJ12345"
# )

print(
    "DMS monitor function ready. "
    "Provide a real task ARN to run."
)