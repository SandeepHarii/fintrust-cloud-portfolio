import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# ============================================================
# W11 D4 PM
# Python Concurrency
# ============================================================


# ============================================================
# A01 - Concurrency Models
# ============================================================

def explain_concurrency_models():
    """Display the main Python concurrency approaches."""

    models = {
        "ThreadPoolExecutor": {
            "best_for": "I/O-bound work",
            "examples": "API calls, database queries, file reads",
            "parallelism": "Overlaps I/O wait time"
        },
        "asyncio": {
            "best_for": "High-concurrency I/O",
            "examples": "Thousands of simultaneous network requests",
            "parallelism": "Event loop switches during await"
        },
        "multiprocessing": {
            "best_for": "CPU-bound work",
            "examples": "Heavy computation and transformations",
            "parallelism": "True parallel execution using processes"
        }
    }

    for approach, details in models.items():
        print(f"\n{approach}")

        for key, value in details.items():
            print(f"  {key}: {value}")


# ============================================================
# A02 - ThreadPoolExecutor
# Parallel API Calls
# ============================================================

def get_object_metadata(bucket: str, key: str) -> dict:
    """
    Simulate fetching S3 object metadata.

    In a real FinTrust pipeline, this function could use:

        s3 = boto3.client("s3")
        response = s3.head_object(
            Bucket=bucket,
            Key=key
        )

    The sleep simulates network I/O without requiring
    AWS credentials to run this exercise.
    """

    time.sleep(0.1)

    return {
        "bucket": bucket,
        "key": key,
        "size": 1024
    }


def fetch_s3_metadata_concurrently(
    bucket: str,
    keys: list[str]
) -> list[dict]:
    """Fetch S3 metadata concurrently using threads."""

    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:

        futures = {
            executor.submit(
                get_object_metadata,
                bucket,
                key
            ): key
            for key in keys
        }

        for future in as_completed(futures):

            key = futures[future]

            try:
                result = future.result()
                results.append(result)

            except Exception as e:
                print(f"Failed for {key}: {e}")

    return results


# ============================================================
# A03 - asyncio Basics
# ============================================================

async def fetch_account_data(account_id: int) -> dict:
    """
    Simulate an asynchronous API request.

    In production, an async HTTP library such as aiohttp
    would be used instead of time.sleep().
    """

    await asyncio.sleep(0.1)

    return {
        "account_id": account_id,
        "status": "active"
    }


async def fetch_all_accounts(account_ids: list[int]) -> list[dict]:
    """Run multiple account requests concurrently."""

    tasks = [
        fetch_account_data(account_id)
        for account_id in account_ids
    ]

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    return results


def run_async_account_fetch(account_ids: list[int]) -> list[dict]:
    """Run the asyncio event loop."""

    return asyncio.run(
        fetch_all_accounts(account_ids)
    )


# ============================================================
# A04 - Choosing the Right Approach
# ============================================================

def print_approach_examples():
    """Display example workload-to-concurrency mappings."""

    scenarios = [
        (
            "Download 200 files from S3",
            "ThreadPoolExecutor",
            "I/O-bound and boto3 is synchronous"
        ),
        (
            "Make 5,000 simultaneous webhook calls",
            "asyncio + aiohttp",
            "High-concurrency network I/O"
        ),
        (
            "Compute SHA-256 hashes for 1 million records",
            "multiprocessing / ProcessPoolExecutor",
            "CPU-bound computation"
        ),
        (
            "Query 20 different RDS tables",
            "ThreadPoolExecutor",
            "Database I/O can overlap"
        ),
        (
            "Train a machine learning model",
            "Multiprocessing or GPU",
            "CPU/GPU-bound computation"
        )
    ]

    for scenario, approach, reason in scenarios:
        print(f"\nScenario: {scenario}")
        print(f"Approach: {approach}")
        print(f"Why: {reason}")


# ============================================================
# Exercise
# FinTrust Nightly DynamoDB Pipeline
# ============================================================

def query_dynamodb_table(table_name: str) -> dict:
    """
    Simulate a DynamoDB query.

    A real implementation would use boto3, for example:

        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(table_name)
        response = table.query(...)

    The sleep simulates the ~200ms network/database wait.
    """

    time.sleep(0.2)

    return {
        "table": table_name,
        "records": 100
    }


# ------------------------------------------------------------
# Exercise - Sequential Version
# ------------------------------------------------------------

def query_tables_sequentially(
    table_names: list[str]
) -> list[dict]:
    """Query all DynamoDB tables one after another."""

    results = []

    for table_name in table_names:
        result = query_dynamodb_table(table_name)
        results.append(result)

    return results


# ------------------------------------------------------------
# Exercise - Concurrent Version
# ------------------------------------------------------------

def query_tables_concurrently(
    table_names: list[str]
) -> list[dict]:
    """Query DynamoDB tables concurrently using threads."""

    results = []

    with ThreadPoolExecutor(max_workers=10) as executor:

        futures = {
            executor.submit(
                query_dynamodb_table,
                table_name
            ): table_name
            for table_name in table_names
        }

        for future in as_completed(futures):

            table_name = futures[future]

            try:
                result = future.result()
                results.append(result)

            except Exception as e:
                print(
                    f"Failed to query {table_name}: {e}"
                )

    return results


# ------------------------------------------------------------
# Exercise - Benchmark
# ------------------------------------------------------------

def benchmark_pipeline(table_names: list[str]):
    """Benchmark sequential and concurrent execution."""

    print("\n" + "=" * 60)
    print("FinTrust DynamoDB Pipeline Benchmark")
    print("=" * 60)

    # Sequential benchmark
    start = time.perf_counter()

    sequential_results = query_tables_sequentially(
        table_names
    )

    sequential_time = time.perf_counter() - start

    # Concurrent benchmark
    start = time.perf_counter()

    concurrent_results = query_tables_concurrently(
        table_names
    )

    concurrent_time = time.perf_counter() - start

    # Calculate speedup
    speedup = sequential_time / concurrent_time

    print(f"\nTables queried: {len(table_names)}")

    print(
        f"Sequential time: "
        f"{sequential_time:.3f} seconds"
    )

    print(
        f"Concurrent time: "
        f"{concurrent_time:.3f} seconds"
    )

    print(
        f"Speedup factor: "
        f"{speedup:.2f}x"
    )

    print(
        f"\nSequential results: "
        f"{len(sequential_results)}"
    )

    print(
        f"Concurrent results: "
        f"{len(concurrent_results)}"
    )


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # A01
    # --------------------------------------------------------

    print("=" * 60)
    print("A01 - Concurrency Models")
    print("=" * 60)

    explain_concurrency_models()


    # --------------------------------------------------------
    # A02
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("A02 - ThreadPoolExecutor")
    print("=" * 60)

    bucket = "fintrust-raw-data"

    keys = [
        "data/file1.csv",
        "data/file2.csv",
        "data/file3.csv",
        "data/file4.csv",
        "data/file5.csv"
    ]

    metadata = fetch_s3_metadata_concurrently(
        bucket,
        keys
    )

    print(f"\nObjects processed: {len(metadata)}")

    for item in metadata:
        print(item)


    # --------------------------------------------------------
    # A03
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("A03 - asyncio")
    print("=" * 60)

    account_ids = list(range(1, 11))

    account_results = run_async_account_fetch(
        account_ids
    )

    print(
        f"Accounts processed: "
        f"{len(account_results)}"
    )

    for result in account_results:
        print(result)


    # --------------------------------------------------------
    # A04
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("A04 - Choosing the Right Approach")
    print("=" * 60)

    print_approach_examples()


    # --------------------------------------------------------
    # Exercise - DynamoDB Benchmark
    # --------------------------------------------------------

    table_names = [
        f"fintrust-transactions-{i}"
        for i in range(1, 41)
    ]

    benchmark_pipeline(table_names)

# ============================================================
# A05 - PORTFOLIO DELIVERABLE
# FinTrust Parallel S3 Metadata Fetch Benchmark
# ============================================================

def fetch_s3_metadata_sequentially(
    bucket: str,
    keys: list[str]
) -> list[dict]:
    """Fetch S3 object metadata sequentially."""
    results = []

    for key in keys:
        results.append(
            get_object_metadata(bucket, key)
        )

    return results


def benchmark_s3_metadata_fetch(
    bucket: str,
    keys: list[str]
):
    """
    Compare sequential and concurrent S3 metadata fetching.

    The metadata function is simulated, so no AWS credentials
    or live S3 bucket are required for this exercise.
    """
    print("\n" + "=" * 60)
    print("FinTrust S3 Metadata Fetch Benchmark")
    print("=" * 60)

    # Sequential benchmark
    start = time.perf_counter()

    sequential_results = fetch_s3_metadata_sequentially(
        bucket,
        keys
    )

    sequential_time = time.perf_counter() - start

    # Concurrent benchmark
    start = time.perf_counter()

    concurrent_results = fetch_s3_metadata_concurrently(
        bucket,
        keys
    )

    concurrent_time = time.perf_counter() - start

    # Calculate speedup
    speedup = sequential_time / concurrent_time

    print(f"\nObjects processed: {len(keys)}")
    print(
        f"Sequential time: "
        f"{sequential_time:.3f} seconds"
    )
    print(
        f"Concurrent time: "
        f"{concurrent_time:.3f} seconds"
    )
    print(
        f"Speedup factor: "
        f"{speedup:.2f}x"
    )

    print(
        f"\nSequential results: "
        f"{len(sequential_results)}"
    )
    print(
        f"Concurrent results: "
        f"{len(concurrent_results)}"
    )


# Example usage:
#
# benchmark_s3_metadata_fetch(
#     "fintrust-raw-data",
#     [
#         "data/file1.csv",
#         "data/file2.csv",
#         "data/file3.csv",
#         "data/file4.csv",
#         "data/file5.csv"
#     ]
# )
#
# In production, get_object_metadata() could use:
#
# s3 = boto3.client("s3")
# response = s3.head_object(
#     Bucket=bucket,
#     Key=key
# )
#
# ThreadPoolExecutor is appropriate here because
# boto3 S3 metadata requests are I/O-bound operations.