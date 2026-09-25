import csv
from datetime import date, timedelta
from pathlib import Path

import boto3


COST_EXPLORER_REGION = "us-east-1"


def get_cost_explorer_client():
    """Return a Cost Explorer client in the required region."""
    return boto3.client(
        "ce",
        region_name=COST_EXPLORER_REGION
    )


def get_date_range(months_back=1):
    """
    Return a Cost Explorer-compatible start and end date.

    Cost Explorer's End date is exclusive.
    """
    today = date.today()

    start_month = today.replace(day=1)

    for _ in range(months_back):
        previous_month = (
            start_month - timedelta(days=1)
        ).replace(day=1)

        start_month = previous_month

    start = start_month.strftime("%Y-%m-%d")
    end = today.strftime("%Y-%m-%d")

    return start, end


def get_monthly_spend_by_service(months_back=1):
    """
    Return cost data grouped by AWS service.

    Returns:
        list[dict]: period, service and cost in USD.
    """

    ce = get_cost_explorer_client()

    start, end = get_date_range(months_back)

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start,
            "End": end
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "SERVICE"
            }
        ]
    )

    results = []

    for period in response["ResultsByTime"]:
        period_start = period["TimePeriod"]["Start"]

        for group in period["Groups"]:
            service = group["Keys"][0]

            cost = float(
                group["Metrics"]["UnblendedCost"]["Amount"]
            )

            results.append(
                {
                    "period": period_start,
                    "service": service,
                    "cost_usd": cost
                }
            )

    return results


def write_csv_report(
    data,
    output_path="cost_report.csv"
):
    """Write service cost data to a CSV file."""

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "period",
                "service",
                "cost_usd"
            ]
        )

        writer.writeheader()
        writer.writerows(data)

    return path


def write_html_report(
    data,
    output_path="cost_report.html"
):
    """Write service cost data to an HTML report."""

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    sorted_data = sorted(
        data,
        key=lambda row: row["cost_usd"],
        reverse=True
    )

    rows = "".join(
        (
            "<tr>"
            f"<td>{row['period']}</td>"
            f"<td>{row['service']}</td>"
            f"<td>${row['cost_usd']:.2f}</td>"
            "</tr>\n"
        )
        for row in sorted_data
        if row["cost_usd"] > 0
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FinTrust Cost Report</title>
</head>
<body>
    <h1>FinTrust Monthly Cost Report</h1>

    <table border="1">
        <thead>
            <tr>
                <th>Period</th>
                <th>Service</th>
                <th>Cost (USD)</th>
            </tr>
        </thead>

        <tbody>
            {rows}
        </tbody>
    </table>
</body>
</html>
"""

    path.write_text(
        html,
        encoding="utf-8"
    )

    return path


def get_account_name_mapping():
    """
    Return a mapping of AWS account IDs to account names.

    Uses AWS Organizations.
    """

    organizations = boto3.client("organizations")

    accounts = {}
    next_token = None

    while True:

        if next_token:
            response = organizations.list_accounts(
                NextToken=next_token
            )
        else:
            response = organizations.list_accounts()

        for account in response["Accounts"]:
            accounts[account["Id"]] = account["Name"]

        next_token = response.get("NextToken")

        if not next_token:
            break

    return accounts


def get_per_account_spend(
    months_back=1
):
    """
    Return AWS spend grouped by linked account and service.

    Returns:
        list[dict]: account ID, account name, service and cost.
    """

    ce = get_cost_explorer_client()

    start, end = get_date_range(months_back)

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start,
            "End": end
        },
        Granularity="MONTHLY",
        Metrics=[
            "UnblendedCost",
            "UsageQuantity"
        ],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "LINKED_ACCOUNT"
            },
            {
                "Type": "DIMENSION",
                "Key": "SERVICE"
            }
        ]
    )

    account_names = get_account_name_mapping()

    results = []

    for period in response["ResultsByTime"]:

        for group in period["Groups"]:

            account_id = group["Keys"][0]
            service = group["Keys"][1]

            cost = float(
                group["Metrics"]["UnblendedCost"]["Amount"]
            )

            results.append(
                {
                    "account_id": account_id,
                    "account_name": account_names.get(
                        account_id,
                        "Unknown"
                    ),
                    "service": service,
                    "cost_usd": cost
                }
            )

    return results


def write_per_account_csv_report(
    data,
    output_path="per_account_cost_report.csv"
):
    """Write per-account cost data to CSV."""

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "account_id",
                "account_name",
                "service",
                "cost_usd"
            ]
        )

        writer.writeheader()
        writer.writerows(data)

    return path