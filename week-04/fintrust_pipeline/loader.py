"""
This module reads transaction data from a CSV file and validates each
transaction before it is loaded into the database.
"""

import csv
from pathlib import Path

VALID_TRANSACTION_TYPES = {"TRANSFER", "DEPOSIT", "WITHDRAWAL"}
VALID_TRANSACTION_STATUSES = {"COMPLETED", "FAILED", "PENDING"}


def validate_row(row: dict) -> tuple[bool, str | None]:
    """Validate a transaction record.

    Returns:
        tuple:
            (True, None) if the row is valid.
            (False, reason) if validation fails.
    """

    if not row["account_from"].strip():
        return False, "missing account_from"

    try:
        amount = float(row["amount"])
    except (ValueError, TypeError):
        return False, f"invalid amount: {row['amount']!r}"

    if amount <= 0:
        return False, f"amount must be positive, got {amount}"

    if row["type"] not in VALID_TRANSACTION_TYPES:
        return False, f"unknown type: {row['type']!r}"

    if row["status"] not in VALID_TRANSACTION_STATUSES:
        return False, f"unknown status: {row['status']!r}"

    return True, None


def load_csv(filepath: Path) -> tuple[list[dict], list[dict]]:
    """Read a CSV file and separate valid and invalid transactions."""

    valid = []
    invalid = []

    with filepath.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            ok, reason = validate_row(row)

            if ok:
                valid.append(row)
            else:
                invalid.append(
                    {
                        "row": row,
                        "reason": reason,
                    }
                )

    return valid, invalid