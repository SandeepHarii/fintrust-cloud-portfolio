"""
This module runs SQL queries against the database and generates
a formatted daily report.
"""

from datetime import datetime
from pathlib import Path
import sqlite3

from .database import query


def generate_report(
    conn: sqlite3.Connection,
    report_path: Path,
) -> str:
    """Generate a formatted transaction report and save it to disk."""

    report_lines = []

    report_lines.append("=" * 60)
    report_lines.append("FINTRUST DAILY TRANSACTION REPORT")
    report_lines.append(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    report_lines.append("=" * 60)

    row = query(conn, """
        SELECT
            COUNT(*) AS total_count,
            ROUND(SUM(amount), 2) AS total_volume,
            ROUND(AVG(amount), 2) AS avg_amount,
            ROUND(MIN(amount), 2) AS min_amount,
            ROUND(MAX(amount), 2) AS max_amount
        FROM transactions
    """)[0]

    report_lines.append("\n── SUMMARY ──────────────────────────────────────────")
    report_lines.append(f"  Total transactions : {row['total_count']}")
    report_lines.append(
        f"  Total volume       : ZAR {row['total_volume']:,.2f}"
    )
    report_lines.append(
        f"  Average amount     : ZAR {row['avg_amount']:,.2f}"
    )
    report_lines.append(
        f"  Min / Max          : "
        f"ZAR {row['min_amount']:,.2f} / "
        f"ZAR {row['max_amount']:,.2f}"
    )

    report_lines.append(
        "\n── BREAKDOWN BY TYPE ────────────────────────────────"
    )

    rows = query(conn, """
        SELECT
            type,
            COUNT(*) AS cnt,
            ROUND(SUM(amount), 2) AS volume
        FROM transactions
        GROUP BY type
        ORDER BY volume DESC
    """)

    for row in rows:
        report_lines.append(
            f"  {row['type']:<12}  "
            f"{row['cnt']:>3} txns   "
            f"ZAR {row['volume']:>10,.2f}"
        )

    report_lines.append(
        "\n── BREAKDOWN BY STATUS ──────────────────────────────"
    )

    rows = query(conn, """
        SELECT
            status,
            COUNT(*) AS cnt,
            ROUND(SUM(amount), 2) AS volume
        FROM transactions
        GROUP BY status
        ORDER BY cnt DESC
    """)

    for row in rows:
        report_lines.append(
            f"  {row['status']:<12}  "
            f"{row['cnt']:>3} txns   "
            f"ZAR {row['volume']:>10,.2f}"
        )

    report_lines.append(
        "\n── TOP 3 LARGEST TRANSACTIONS ───────────────────────"
    )

    rows = query(conn, """
        SELECT
            transaction_id,
            account_from,
            amount,
            type,
            status
        FROM transactions
        ORDER BY amount DESC
        LIMIT 3
    """)

    for index, row in enumerate(rows, start=1):
        report_lines.append(
            f"  #{index}  {row['transaction_id']}  "
            f"{row['account_from']}  "
            f"ZAR {row['amount']:,.2f}  "
            f"[{row['type']} / {row['status']}]"
        )

    report_lines.append("\n" + "=" * 60)

    report_text = "\n".join(report_lines)

    report_path.write_text(report_text, encoding="utf-8")

    return report_text