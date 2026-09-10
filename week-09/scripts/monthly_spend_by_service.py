import boto3
from datetime import date, timedelta

# Cost Explorer is always us-east-1
ce = boto3.client(
    'ce',
    region_name='us-east-1'
)


def get_monthly_spend_by_service(year, month):
    """
    Returns a dictionary mapping AWS service names
    to their total spend for the given month.
    """

    start = f'{year}-{month:02d}-01'

    # Compute first day of next month
    if month == 12:
        end = f'{year + 1}-01-01'
    else:
        end = f'{year}-{month + 1:02d}-01'

    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End': end
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            }
        ]
    )

    results = {}

    for group in response['ResultsByTime'][0]['Groups']:
        service = group['Keys'][0]

        cost = float(
            group['Metrics']['UnblendedCost']['Amount']
        )

        # Filter out near-zero services
        if cost > 0.01:
            results[service] = round(cost, 2)

    # Sort services from highest to lowest cost
    return dict(
        sorted(
            results.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )


# Example: June 2024
spend = get_monthly_spend_by_service(2024, 6)

print("Monthly AWS Spend by Service")
print("-" * 70)

# Display top 10 services
for service, cost in list(spend.items())[:10]:
    print(
        f"{service:<45} "
        f"${cost:>10,.2f}"
    )


# Calculate total spend
total_spend = sum(spend.values())

print("-" * 70)
print(
    f"{'Total Spend':<45} "
    f"${total_spend:>10,.2f}"
)


# Top 5 concentration ratio
print()
print("Top 5 Service Concentration")
print("-" * 70)

top_5_spend = 0

for service, cost in list(spend.items())[:5]:
    percentage = (
        cost / total_spend * 100
        if total_spend > 0
        else 0
    )

    top_5_spend += cost

    print(
        f"{service:<45} "
        f"${cost:>10,.2f} "
        f"({percentage:>5.1f}%)"
    )

concentration_ratio = (
    top_5_spend / total_spend * 100
    if total_spend > 0
    else 0
)

print("-" * 70)
print(
    f"Top 5 concentration ratio: "
    f"{concentration_ratio:.1f}%"
)