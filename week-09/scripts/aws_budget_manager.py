import boto3

# AWS Budgets API
budgets = boto3.client(
    'budgets',
    region_name='us-east-1'
)

# Get the current AWS account ID automatically
sts = boto3.client('sts')
ACCOUNT_ID = sts.get_caller_identity()['Account']


def create_monthly_budget(
    budget_name,
    limit_usd,
    alert_pct,
    email
):
    """
    Create a monthly cost budget with a
    percentage-threshold alert.
    """

    budgets.create_budget(
        AccountId=ACCOUNT_ID,
        Budget={
            'BudgetName': budget_name,
            'BudgetLimit': {
                'Amount': str(limit_usd),
                'Unit': 'USD'
            },
            'TimeUnit': 'MONTHLY',
            'BudgetType': 'COST'
        },
        NotificationsWithSubscribers=[
            {
                'Notification': {
                    'NotificationType': 'ACTUAL',
                    'ComparisonOperator': 'GREATER_THAN',
                    'Threshold': alert_pct,
                    'ThresholdType': 'PERCENTAGE'
                },
                'Subscribers': [
                    {
                        'SubscriptionType': 'EMAIL',
                        'Address': email
                    }
                ]
            }
        ]
    )

    print(
        f'Budget "{budget_name}" created: '
        f'${limit_usd:,.2f}/month, '
        f'alert at {alert_pct}%'
    )


def show_budget_utilisation():
    """
    List all budgets for the current AWS account
    and display their current utilisation.
    """

    response = budgets.describe_budgets(
        AccountId=ACCOUNT_ID
    )

    print()
    print("AWS Budget Utilisation")
    print("-" * 70)

    if not response['Budgets']:
        print("No budgets found.")
        return

    for budget in response['Budgets']:
        budget_name = budget['BudgetName']

        limit = float(
            budget['BudgetLimit']['Amount']
        )

        actual = float(
            budget.get(
                'CalculatedSpend',
                {}
            ).get(
                'ActualSpend',
                {}
            ).get(
                'Amount',
                0
            )
        )

        percentage = (
            actual / limit * 100
            if limit > 0
            else 0
        )

        print(
            f'{budget_name:<35} '
            f'${actual:>10,.2f} / '
            f'${limit:>10,.2f} '
            f'({percentage:>5.1f}%)'
        )


# FinTrust Analytics team budget
create_monthly_budget(
    budget_name='FinTrust-Analytics-Monthly',
    limit_usd=15000,
    alert_pct=80.0,
    email='analytics-lead@fintrust.co.za'
)


# Display current budget utilisation
show_budget_utilisation()