import csv
import logging
import time
from functools import wraps


# ============================================================
# W11 D3 PM
# Python Decorators
# ============================================================


# ============================================================
# A01 - How Decorators Work
# ============================================================

def timer(func):
    """Decorator that logs how long a function takes to run."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start
        print(f"{func.__name__} completed in {elapsed:.3f}s")

        return result

    return wrapper


@timer
def load_data(table_name: str) -> list:
    """Simulate loading data from a database table."""
    time.sleep(0.1)
    return []


# Test A01
if __name__ == "__main__":
    print("A01 - Timer decorator")

    data = load_data("transactions")
    print(f"Loaded rows: {len(data)}")


# ============================================================
# A02 - Practical Data Pipeline Decorators
# ============================================================

def retry(max_attempts=3, delay_seconds=2):
    """Retry a function after an exception using exponential backoff."""

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    last_error = e

                    wait = delay_seconds * (2 ** attempt)

                    logging.warning(
                        f"Attempt {attempt + 1}/{max_attempts} failed: "
                        f"{e}. Retrying in {wait}s"
                    )

                    if attempt < max_attempts - 1:
                        time.sleep(wait)

            raise last_error

        return wrapper

    return decorator


api_attempts = 0


@retry(max_attempts=3, delay_seconds=1)
def fetch_from_api(endpoint: str) -> dict:
    """Simulate an API request that may fail temporarily."""

    global api_attempts

    api_attempts += 1

    if api_attempts < 3:
        raise ConnectionError("Temporary API connection failure")

    return {
        "endpoint": endpoint,
        "status": "success",
        "attempt": api_attempts
    }


# Test A02
if __name__ == "__main__":
    print("\nA02 - Retry decorator")

    logging.basicConfig(
        level=logging.WARNING,
        format="%(levelname)s: %(message)s"
    )

    response = fetch_from_api("/transactions")
    print(response)


# ============================================================
# A03 - Decorators With Arguments
# ============================================================

def validate_types(**expected_types):
    """Validate keyword argument types at runtime."""

    def decorator(func):

        @wraps(func)
        def wrapper(**kwargs):

            for param, expected in expected_types.items():

                if param in kwargs and not isinstance(
                    kwargs[param],
                    expected
                ):
                    raise TypeError(
                        f"'{param}' must be {expected.__name__}, "
                        f"got {type(kwargs[param]).__name__}"
                    )

            return func(**kwargs)

        return wrapper

    return decorator


@validate_types(account_id=int, amount=float)
def process_transaction(account_id: int, amount: float) -> bool:
    """Validate and process a transaction."""

    return amount > 0


# Test A03
if __name__ == "__main__":
    print("\nA03 - Decorator with arguments")

    valid_transaction = process_transaction(
        account_id=1001,
        amount=250.50
    )

    print(f"Valid transaction: {valid_transaction}")

    try:
        process_transaction(
            account_id="1001",
            amount=250.50
        )
    except TypeError as e:
        print(f"Validation error: {e}")


# ============================================================
# A04 - Exercise 1
# Logging Decorator
# ============================================================

logger = logging.getLogger("fintrust")


def log_call(func):
    """Log the function name, arguments and return value."""

    @wraps(func)
    def wrapper(*args, **kwargs):

        logger.info(
            "Calling %s with args=%s kwargs=%s",
            func.__name__,
            args,
            kwargs
        )

        result = func(*args, **kwargs)

        logger.info(
            "%s returned %s",
            func.__name__,
            result
        )

        return result

    return wrapper


@log_call
def load_csv_file(file_path: str) -> list:
    """Load transaction records from a CSV file."""

    records = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


# ============================================================
# A04 - Exercise 2
# Memoize / Cache Decorator
# ============================================================

def memoize(func):
    """Cache function results using the function arguments as the key."""

    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):

        # kwargs are sorted so equivalent keyword ordering
        # produces the same cache key.
        key = (
            args,
            tuple(sorted(kwargs.items()))
        )

        if key in cache:
            print(f"Cache hit for {func.__name__}{args}{kwargs}")
            return cache[key]

        print(f"Cache miss for {func.__name__}{args}{kwargs}")

        result = func(*args, **kwargs)
        cache[key] = result

        return result

    return wrapper


@memoize
def slow_database_query(account_id: int) -> dict:
    """Simulate a slow database query."""

    print(f"Executing database query for account {account_id}...")
    time.sleep(2)

    return {
        "account_id": account_id,
        "balance": 12500.75,
        "status": "active"
    }


# ============================================================
# A04 - Exercise 3
# Stacking Decorators
# ============================================================

stack_attempts = 0


@retry(max_attempts=2, delay_seconds=1)
@timer
def unreliable_pipeline():
    """
    Demonstrate retry wrapping timer.

    The retry decorator is the outer decorator.
    The timer decorator is the inner decorator.
    """

    global stack_attempts

    stack_attempts += 1

    print(f"Pipeline attempt {stack_attempts}")

    if stack_attempts == 1:
        raise ConnectionError("Temporary pipeline failure")

    return "Pipeline completed successfully"


# Equivalent to:
#
# unreliable_pipeline = retry(max_attempts=2, delay_seconds=1)(
#     timer(unreliable_pipeline)
# )


# ============================================================
# Tests
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Exercise 1 - Logging decorator
    # --------------------------------------------------------

    print("\nExercise 1 - Logging decorator")

    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                "%(levelname)s: %(message)s"
            )
        )
        logger.addHandler(handler)

    csv_file = "transactions.csv"

    try:
        transactions = load_csv_file(csv_file)
        print(f"Loaded {len(transactions)} transactions")

    except FileNotFoundError:
        logger.warning(
            "CSV test file '%s' was not found. "
            "The decorator itself was successfully applied.",
            csv_file
        )


    # --------------------------------------------------------
    # Exercise 2 - Memoize decorator
    # --------------------------------------------------------

    print("\nExercise 2 - Memoize decorator")

    print("First call:")
    result_1 = slow_database_query(1001)
    print(result_1)

    print("\nSecond call with the same argument:")
    result_2 = slow_database_query(1001)
    print(result_2)

    print("\nCall with a different argument:")
    result_3 = slow_database_query(1002)
    print(result_3)


    # --------------------------------------------------------
    # Exercise 3 - Stacking decorators
    # --------------------------------------------------------

    print("\nExercise 3 - Stacking decorators")

    result = unreliable_pipeline()

    print(f"Final result: {result}")

    print(
        "\nDecorator order:"
        "\n@retry is the outer decorator."
        "\n@timer is the inner decorator."
        "\nTherefore, retry(timer(unreliable_pipeline)) is created."
        "\nEach retry attempt runs through the timer."
    )

# ============================================================
# A05 - PORTFOLIO DELIVERABLE
# FinTrust boto3 Retry Decorator
# ============================================================

import boto3


@retry(max_attempts=3, delay_seconds=1)
def get_s3_bucket_location(bucket_name: str) -> dict:
    """
    Retrieve the location of an S3 bucket using boto3.

    The retry decorator provides exponential backoff if the
    boto3 API call fails temporarily.
    """
    s3 = boto3.client("s3")
    return s3.get_bucket_location(Bucket=bucket_name)


# Example usage:
#
# bucket_location = get_s3_bucket_location("fintrust-data-bucket")
# print(bucket_location)
#
# The boto3 call is intentionally not executed automatically.
# AWS credentials and a valid S3 bucket are required.
#
# Retry behaviour:
# Attempt 1 -> wait 1 second
# Attempt 2 -> wait 2 seconds
# Attempt 3 -> raise the final exception
#
# @wraps preserves the original function metadata.
# The decorator factory allows max_attempts and delay_seconds
# to be configured for different API calls.