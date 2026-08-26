"""
Week 8 - Athena Query Runner

AWS calls have been commented out until AWS resources
and permissions are configured.

This script demonstrates the Athena async query
execution pattern used by FinTrust.
"""

# import boto3
import time

# athena = boto3.client(
#     "athena",
#     region_name="af-south-1"
# )


def run_athena_query(sql, database, output_bucket):

    print(f"Database: {database}")
    print(f"Output Bucket: {output_bucket}")

    print("\nExecuting query:")
    print(sql)

    # response = athena.start_query_execution(
    #     QueryString=sql,
    #     QueryExecutionContext={
    #         "Database": database
    #     },
    #     ResultConfiguration={
    #         "OutputLocation":
    #         f"s3://{output_bucket}/athena-results/"
    #     }
    # )

    # query_id = response["QueryExecutionId"]

    print("\nStatus: QUEUED")
    time.sleep(1)

    print("Status: RUNNING")
    time.sleep(1)

    print("Status: SUCCEEDED")

    print("\nAWS execution disabled.")

    return []


sql = """
SELECT account_id,
       SUM(amount) AS total,
       COUNT(*) AS tx_count
FROM fintrust_curated.transactions
GROUP BY account_id
ORDER BY total DESC
LIMIT 100
"""

run_athena_query(
    sql,
    "fintrust_curated",
    "fintrust-athena-results"
)