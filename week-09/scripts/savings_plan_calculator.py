def calculate_savings_plan_savings(
    hourly_commitment_usd,
    term_years=3,
    discount_pct=0.66
):
    """
    Calculate total savings from a Compute Savings Plan
    compared with On-Demand pricing.
    """

    # Calculate the equivalent On-Demand hourly cost
    effective_ondemand_hourly = (
        hourly_commitment_usd / (1 - discount_pct)
    )

    # Calculate total hours in the Savings Plan term
    hours_in_period = term_years * 365 * 24

    # Calculate total costs
    total_ondemand_cost = (
        effective_ondemand_hourly * hours_in_period
    )

    total_sp_cost = (
        hourly_commitment_usd * hours_in_period
    )

    # Calculate total savings
    total_savings = (
        total_ondemand_cost - total_sp_cost
    )

    return {
        'commitment_per_hour': hourly_commitment_usd,
        'effective_ondemand_hourly': round(
            effective_ondemand_hourly, 4
        ),
        'total_ondemand_cost': round(
            total_ondemand_cost, 2
        ),
        'total_sp_cost': round(
            total_sp_cost, 2
        ),
        'total_savings_usd': round(
            total_savings, 2
        ),
        'savings_pct': round(
            discount_pct * 100, 1
        )
    }


# ---------------------------------------------------------
# FinTrust Scenario
# ---------------------------------------------------------

result = calculate_savings_plan_savings(
    hourly_commitment_usd=32.47,
    term_years=3,
    discount_pct=0.66
)


# ---------------------------------------------------------
# Display Results
# ---------------------------------------------------------

print("FinTrust Compute Savings Plan")
print("-" * 45)

for key, value in result.items():
    print(f"{key}: {value}")