import boto3


scheduler = boto3.client(
    'scheduler',
    region_name='af-south-1'
)


LAMBDA_ARN = (
    'arn:aws:lambda:af-south-1:123456789012:'
    'function:datasync-throttle'
)

ROLE_ARN = (
    'arn:aws:iam::123456789012:'
    'role/EventBridgeSchedulerRole'
)


# 07:00 SAST = 05:00 UTC
# Switch to daytime throttle of 500 Mbps.
scheduler.create_schedule(
    Name='datasync-throttle-daytime',
    ScheduleExpression='cron(0 5 * * ? *)',
    FlexibleTimeWindow={
        'Mode': 'OFF'
    },
    Target={
        'Arn': LAMBDA_ARN,
        'RoleArn': ROLE_ARN,
        'Input': '{"mode": "daytime"}'
    }
)


# 22:00 SAST = 20:00 UTC
# Switch to overnight throttle of 9 Gbps.
scheduler.create_schedule(
    Name='datasync-throttle-overnight',
    ScheduleExpression='cron(0 20 * * ? *)',
    FlexibleTimeWindow={
        'Mode': 'OFF'
    },
    Target={
        'Arn': LAMBDA_ARN,
        'RoleArn': ROLE_ARN,
        'Input': '{"mode": "overnight"}'
    }
)


print(
    'DataSync throttle schedules created.'
)