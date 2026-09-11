import boto3
from datetime import datetime, timezone, timedelta


dms = boto3.client(
    'dms',
    region_name='af-south-1'
)

cloudwatch = boto3.client(
    'cloudwatch',
    region_name='af-south-1'
)


def get_cdc_latency(
    replication_instance_id,
    task_identifier,
    lookback_minutes=5
):
    now = datetime.now(timezone.utc)

    def get_metric(metric_name):
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/DMS',
            MetricName=metric_name,
            Dimensions=[
                {
                    'Name': 'ReplicationInstanceIdentifier',
                    'Value': replication_instance_id
                },
                {
                    'Name': 'ReplicationTaskIdentifier',
                    'Value': task_identifier
                }
            ],
            StartTime=(
                now
                - timedelta(minutes=lookback_minutes)
            ),
            EndTime=now,
            Period=60,
            Statistics=['Maximum']
        )

        points = response.get(
            'Datapoints',
            []
        )

        if not points:
            return None

        latest = sorted(
            points,
            key=lambda x: x['Timestamp']
        )[-1]

        return latest['Maximum']

    return get_metric('CDCLatencySource')


def check_dms_tasks():
    paginator = dms.get_paginator(
        'describe_replication_tasks'
    )

    print("FinTrust DMS Health Check")
    print("=" * 80)

    task_count = 0

    for page in paginator.paginate():

        for task in page.get(
            'ReplicationTasks',
            []
        ):
            task_count += 1

            identifier = task[
                'ReplicationTaskIdentifier'
            ]

            status = task[
                'Status'
            ]

            replication_instance = task.get(
                'ReplicationInstanceArn',
                ''
            ).split(':')[-1]

            print(
                f"\nTask:   {identifier}"
            )

            print(
                f"Status: {status}"
            )

            if status == 'running':

                latency = get_cdc_latency(
                    replication_instance,
                    identifier
                )

                print(
                    f"CDC latency: "
                    f"{latency}s"
                )

                cutover_ready = (
                    latency is not None
                    and latency < 30
                )

                print(
                    f"Cutover-ready: "
                    f"{cutover_ready}"
                )

            else:
                print(
                    "CDC latency: not checked"
                )

                print(
                    "Cutover-ready: False"
                )

    print(
        f"\nTotal DMS tasks: {task_count}"
    )


if __name__ == '__main__':
    check_dms_tasks()