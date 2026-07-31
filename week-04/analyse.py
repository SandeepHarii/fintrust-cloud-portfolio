"""
Analyse FinTrust transaction data using pandas and export
an enriched dataset.
"""

from pathlib import Path
import sqlite3

import pandas as pd

DB_FILE = Path("fintrust_analytics.db")
OUTPUT_FILE = Path("transactions_enriched.csv")


def main() -> None:
    """Run the transaction analysis pipeline."""

    # Load the transactions table into a DataFrame
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()

    print("=== DataFrame Shape ===")
    print(f"Rows: {len(df)}  Columns: {len(df.columns)}")

    print("\n=== Column Types ===")
    print(df.dtypes)

    print("\n=== First 3 Rows ===")
    print(df.head(3))

    # Filter: completed transfers
    completed_transfers = df[
        (df["status"] == "COMPLETED")
        & (df["type"] == "TRANSFER")
    ]

    print(f"\nCompleted transfers: {len(completed_transfers)}")
    print(
        f"Total volume: "
        f"ZAR {completed_transfers['amount'].sum():,.2f}"
    )

    # Filter: transactions above the average amount
    average_amount = df["amount"].mean()
    large_transactions = df[df["amount"] > average_amount]

    print(
        f"\nAbove-average transactions "
        f"(>{average_amount:,.2f}):"
    )
    print(
        large_transactions[
            [
                "transaction_id",
                "amount",
                "type",
                "status",
            ]
        ]
    )

    # Group by transaction status
    by_status = (
        df.groupby("status")
        .agg(
            count=("transaction_id", "count"),
            total_volume=("amount", "sum"),
            avg_amount=("amount", "mean"),
        )
        .round(2)
    )

    print("\n=== By Status ===")
    print(by_status)

    # Group by transaction type
    by_type = (
        df.groupby("type")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n=== Volume by Type ===")
    print(by_type)

    # Add calculated columns
    df["high_value"] = df["amount"] > 2000
    df["txn_date"] = pd.to_datetime(df["timestamp"]).dt.date

    print("\n=== DataFrame with New Columns ===")
    print(
        df[
            [
                "transaction_id",
                "amount",
                "high_value",
                "txn_date",
            ]
        ].to_string(index=False)
    )

    # Export enriched dataset
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nExported to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()