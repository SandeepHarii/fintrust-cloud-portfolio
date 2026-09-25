import os
from datetime import date
from pathlib import Path

import boto3

from fintrust_migration.cost_reporting import (
    get_monthly_spend_by_service,
    get_per_account_spend,
    write_csv_report,
    write_html_report,
    write_per_account_csv_report,
)


def upload_to_s3(
    file_path: Path,
    bucket: str,
    s3_key: str
):
    """Upload a report file to S3."""

    s3 = boto3.client("s3")

    s3.upload_file(
        str(file_path),
        bucket,
        s3_key
    )

    print(
        f"Uploaded {file_path} "
        f"to s3://{bucket}/{s3_key}"
    )


def main():
    """Generate and upload FinTrust cost reports."""

    reports_dir = Path("reports")
    reports_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # Get service-level cost data
    # --------------------------------------------------------

    service_data = get_monthly_spend_by_service(
        months_back=1
    )

    # --------------------------------------------------------
    # Generate CSV report
    # --------------------------------------------------------

    csv_path = write_csv_report(
        service_data,
        reports_dir / "cost_report.csv"
    )

    print(f"Created: {csv_path}")

    # --------------------------------------------------------
    # Generate HTML report
    # --------------------------------------------------------

    html_path = write_html_report(
        service_data,
        reports_dir / "cost_report.html"
    )

    print(f"Created: {html_path}")

    # --------------------------------------------------------
    # Get per-account cost data
    # --------------------------------------------------------

    per_account_data = get_per_account_spend(
        months_back=1
    )

    per_account_csv_path = write_per_account_csv_report(
        per_account_data,
        reports_dir / "per_account_cost_report.csv"
    )

    print(
        f"Created: {per_account_csv_path}"
    )

    # --------------------------------------------------------
    # Upload service CSV to S3
    # --------------------------------------------------------

    audit_bucket = os.getenv(
        "FINTRUST_AUDIT_BUCKET"
    )

    if not audit_bucket:
        raise RuntimeError(
            "FINTRUST_AUDIT_BUCKET environment variable "
            "is not set. Set it to your audit S3 bucket "
            "before running the upload."
        )

    today = date.today()

    s3_key = (
        f"cost-reports/"
        f"{today.year}/"
        f"{today.month:02d}/"
        f"cost_report.csv"
    )

    upload_to_s3(
        csv_path,
        audit_bucket,
        s3_key
    )


if __name__ == "__main__":
    main()