import json
import os
import tempfile
from datetime import date
from pathlib import Path

import boto3

from fintrust_migration.cost_reporting import (
    get_monthly_spend_by_service,
    write_csv_report,
    write_html_report,
)


S3_BUCKET = os.environ.get(
    "FINTRUST_COST_REPORT_BUCKET",
    "fintrust-cost-reports",
)


def lambda_handler(event, context):
    """
    Generate monthly FinTrust cost reports and upload them to S3.
    """

    today = date.today()

    prefix = (
        f"cost-reports/"
        f"{today.year}/"
        f"{today.month:02d}"
    )

    data = get_monthly_spend_by_service(
        months_back=1
    )

    uploaded_files = []

    with tempfile.TemporaryDirectory() as tmpdir:

        csv_path = write_csv_report(
            data,
            Path(tmpdir) / "cost_report.csv"
        )

        html_path = write_html_report(
            data,
            Path(tmpdir) / "cost_report.html"
        )

        s3 = boto3.client("s3")

        reports = [
            (
                csv_path,
                "cost_report.csv"
            ),
            (
                html_path,
                "cost_report.html"
            ),
        ]

        for path, filename in reports:

            s3_key = f"{prefix}/{filename}"

            s3.upload_file(
                str(path),
                S3_BUCKET,
                s3_key
            )

            uploaded_files.append(
                f"s3://{S3_BUCKET}/{s3_key}"
            )

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Reports uploaded successfully",
                "files": uploaded_files,
            }
        ),
    }