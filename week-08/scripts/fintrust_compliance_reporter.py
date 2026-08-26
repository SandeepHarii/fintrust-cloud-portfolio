"""
Week 8 - FinTrust Compliance Reporter

AWS calls have been commented out until AWS resources
and permissions are configured.

This class demonstrates how FinTrust would execute
Athena compliance reports, export results, and
optionally upload reports to S3.
"""

# import boto3
import csv
import time


class FinTrustComplianceReporter:

    def __init__(
        self,
        database,
        output_bucket,
        region="af-south-1"
    ):
        self.database = database
        self.output_bucket = output_bucket
        self.region = region

        # self.athena = boto3.client(
        #     "athena",
        #     region_name=region
        # )
        #
        # self.s3 = boto3.client(
        #     "s3",
        #     region_name=region
        # )

    def run_report(self, report_name, sql):

        print(f"Running report: {report_name}")
        print(f"Database: {self.database}")

        # response = (
        #     self.athena.start_query_execution(
        #         QueryString=sql,
        #         QueryExecutionContext={
        #             "Database": self.database
        #         },
        #         ResultConfiguration={
        #             "OutputLocation":
        #             f"s3://{self.output_bucket}/"
        #         }
        #     )
        # )

        print("Status: QUEUED")
        time.sleep(1)

        print("Status: RUNNING")
        time.sleep(1)

        print("Status: SUCCEEDED")

        rows = [
            ["account_id", "total", "tx_count"],
            ["ACC-0001", "125000", "3"],
            ["ACC-0002", "98000", "2"]
        ]

        filename = f"{report_name}.csv"

        with open(
            filename,
            "w",
            newline=""
        ) as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        row_count = len(rows) - 1

        print(
            f"Report '{report_name}' complete: "
            f"{row_count} rows written to "
            f"{filename}"
        )

        return row_count

    def save_to_s3(
        self,
        bucket,
        key,
        local_path
    ):

        # self.s3.upload_file(
        #     local_path,
        #     bucket,
        #     key
        # )

        print(
            f"AWS upload disabled: "
            f"s3://{bucket}/{key}"
        )


reporter = FinTrustComplianceReporter(
    database="fintrust_curated",
    output_bucket="fintrust-athena-results"
)

sql = """
SELECT account_id,
       SUM(amount) AS total,
       COUNT(*) AS tx_count
FROM transactions
GROUP BY account_id
"""

reporter.run_report(
    "high_value_transactions",
    sql
)