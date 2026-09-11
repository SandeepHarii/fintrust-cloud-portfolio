from fintrust_migration.s3.sync_helpers import (
    start_task_execution,
    get_execution_status
)

import time


def monitor_nightly_transfers(task_arns):
    """
    Start multiple DataSync tasks and monitor
    their executions until all are terminal.

    Args:
        task_arns: List of DataSync task ARNs.

    Returns:
        Dictionary mapping execution ARN to
        final execution status information.
    """

    # Start all tasks using a list comprehension.
    execution_arns = [
        start_task_execution(task_arn)
        for task_arn in task_arns
    ]

    start_times = {
        execution_arn: time.time()
        for execution_arn in execution_arns
    }

    task_identifiers = {
        execution_arn: task_arn.split('/')[-1]
        for execution_arn, task_arn in zip(
            execution_arns,
            task_arns
        )
    }

    terminal = {
        'SUCCESS',
        'ERROR'
    }

    final_results = {}

    while True:

        all_terminal = True

        print()
        print(
            "DataSync Transfer Monitor"
        )
        print("=" * 80)

        print(
            f"{'Task':30s}"
            f"{'Status':12s}"
            f"{'GB':12s}"
            f"{'Elapsed (min)':15s}"
        )

        print("-" * 80)

        for execution_arn in execution_arns:

            info = get_execution_status(
                execution_arn
            )

            status = info['status']

            transferred_gb = (
                info['bytes_transferred']
                / 1024**3
            )

            elapsed_minutes = (
                time.time()
                - start_times[execution_arn]
            ) / 60

            task_identifier = task_identifiers[
                execution_arn
            ]

            print(
                f"{task_identifier[:28]:30s}"
                f"{status:12s}"
                f"{transferred_gb:10.2f} GB"
                f"{elapsed_minutes:13.1f}"
            )

            if status not in terminal:
                all_terminal = False

            else:
                final_results[
                    execution_arn
                ] = info

        if all_terminal:
            break

        time.sleep(60)

    return final_results


if __name__ == '__main__':

    task_arns = [
        # Add real DataSync task ARNs here.
    ]

    if not task_arns:
        print(
            "No DataSync task ARNs configured."
        )
    else:
        results = monitor_nightly_transfers(
            task_arns
        )

        print()
        print(
            "Final Transfer Results"
        )
        print("=" * 80)

        for execution_arn, info in results.items():

            print(
                f"\nExecution: {execution_arn}"
            )

            print(
                f"Status: "
                f"{info['status']}"
            )

            print(
                f"Files transferred: "
                f"{info['files_transferred']}"
            )

            print(
                f"Bytes transferred: "
                f"{info['bytes_transferred']}"
            )