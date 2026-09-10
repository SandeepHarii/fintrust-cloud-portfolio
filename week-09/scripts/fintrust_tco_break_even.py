def tco_break_even(
    on_prem_annual_cost,
    aws_monthly_cost,
    migration_one_time_cost,
    onprem_inflation_pct=0.03
):
    """
    Compare cumulative on-premises and AWS costs over 60 months.

    Returns:
        The first month where AWS cumulative cost is lower
        than on-premises cumulative cost.
        Returns None if AWS does not break even within 60 months.
    """

    cumulative_on_prem = 0
    cumulative_aws = 0
    break_even_month = None

    monthly_on_prem_cost = on_prem_annual_cost / 12

    yearly_summary = []

    for month in range(1, 61):
        # Apply annual inflation at the start of each new year
        year = (month - 1) // 12
        inflated_monthly_cost = (
            monthly_on_prem_cost
            * ((1 + onprem_inflation_pct) ** year)
        )

        cumulative_on_prem += inflated_monthly_cost

        # AWS includes the one-time migration cost
        cumulative_aws = (
            migration_one_time_cost
            + (aws_monthly_cost * month)
        )

        difference = cumulative_aws - cumulative_on_prem

        # Find the first month where AWS becomes cheaper
        if (
            break_even_month is None
            and cumulative_aws < cumulative_on_prem
        ):
            break_even_month = month

        # Store year-end figures
        if month % 12 == 0:
            yearly_summary.append({
                "year": month // 12,
                "month": month,
                "on_prem_cost": cumulative_on_prem,
                "aws_cost": cumulative_aws,
                "difference": difference
            })

    print("FinTrust TCO Break-Even Analysis")
    print("-" * 70)

    if break_even_month is not None:
        print(
            f"AWS breaks even with on-premises in "
            f"month {break_even_month}."
        )
    else:
        print(
            "AWS does not break even with on-premises "
            "within the 60-month period."
        )

    print()
    print("Year-by-Year Cumulative Cost Comparison")
    print("-" * 70)

    print(
        f"{'Year':<8}"
        f"{'On-Prem':>18}"
        f"{'AWS':>18}"
        f"{'Difference':>20}"
    )

    print("-" * 70)

    for summary in yearly_summary:
        print(
            f"{summary['year']:<8}"
            f"${summary['on_prem_cost']:>17,.2f}"
            f"${summary['aws_cost']:>17,.2f}"
            f"${summary['difference']:>19,.2f}"
        )

    return break_even_month


# FinTrust scenario
on_prem_annual_cost = 4_200_000
aws_monthly_cost = 248_000
migration_one_time_cost = 850_000
onprem_inflation_pct = 0.03

break_even = tco_break_even(
    on_prem_annual_cost=on_prem_annual_cost,
    aws_monthly_cost=aws_monthly_cost,
    migration_one_time_cost=migration_one_time_cost,
    onprem_inflation_pct=onprem_inflation_pct
)

print()
print(f"Break-even month: {break_even}")