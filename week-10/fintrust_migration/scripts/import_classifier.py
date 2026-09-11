from fintrust_migration import classify_instances


portfolio, untagged = classify_instances()


print("=== FinTrust Migration Portfolio Summary ===")

total = sum(
    len(instances)
    for instances in portfolio.values()
)


for strategy, instances in sorted(portfolio.items()):
    pct = (
        len(instances) / total * 100
        if total
        else 0
    )

    print(
        f"{strategy.upper():12s}: "
        f"{len(instances):4d} instances "
        f"({pct:.1f}%)"
    )


print(
    f"{'UNTAGGED':12s}: "
    f"{len(untagged):4d} instances "
    f"(needs classification)"
)


print(
    f"{'TOTAL':12s}: "
    f"{total + len(untagged):4d}"
)