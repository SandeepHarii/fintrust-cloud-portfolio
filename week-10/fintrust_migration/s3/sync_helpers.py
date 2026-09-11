from ..utils.sessions import get_client
import os
import time


def start_task_execution(task_arn):
    ds = get_client('datasync')

    resp = ds.start_task_execution(
        TaskArn=task_arn
    )

    return resp['TaskExecutionArn']


def get_execution_status(execution_arn):
    ds = get_client('datasync')

    resp = ds.describe_task_execution(
        TaskExecutionArn=execution_arn
    )

    return {
        'status': resp['Status'],
        'files_prepared': resp['Result'].get(
            'PrepareDuration'
        ),
        'files_transferred': resp.get(
            'FilesTransferred',
            0
        ),
        'bytes_transferred': resp.get(
            'BytesTransferred',
            0
        ),
        'files_verified': resp.get(
            'FilesVerified',
            0
        ),
        'errors': resp.get(
            'FilesDeleted',
            0
        ),
        'result': resp.get(
            'Result',
            {}
        )
    }


def wait_for_execution(
    execution_arn,
    poll_seconds=60
):
    terminal = {
        'SUCCESS',
        'ERROR'
    }

    while True:

        info = get_execution_status(
            execution_arn
        )

        status = info['status']

        transferred_gb = (
            info['bytes_transferred']
            / 1024**3
        )

        print(
            f'[{time.strftime("%H:%M:%S")}] '
            f'{status} | '
            f'{info["files_transferred"]} files | '
            f'{transferred_gb:.2f} GB'
        )

        if status in terminal:
            return info

        time.sleep(poll_seconds)


MBPS_TO_BYTES = 1_000_000 / 8


def set_task_throttle(
    task_arn,
    bandwidth_mbps
):
    ds = get_client('datasync')

    if bandwidth_mbps == 0:
        throttle = 0
    else:
        throttle = int(
            bandwidth_mbps * MBPS_TO_BYTES
        )

    ds.update_task(
        TaskArn=task_arn,
        Options={
            'BytesPerSecond': throttle
        }
    )

    label = (
        f'{bandwidth_mbps} Mbps'
        if throttle
        else 'unlimited'
    )

    print(
        f'Task throttle updated to '
        f'{label} '
        f'({throttle} bytes/sec)'
    )


def lambda_handler(event, context):
    task_arn = os.getenv(
        'DATASYNC_TASK_ARN'
    )

    mode = event.get(
        'mode',
        'daytime'
    )

    throttle_map = {
        'daytime': 500,
        'overnight': 9000
    }

    bandwidth = throttle_map.get(
        mode,
        500
    )

    set_task_throttle(
        task_arn,
        bandwidth
    )

    return {
        'statusCode': 200,
        'bandwidth_mbps': bandwidth,
        'mode': mode
    }