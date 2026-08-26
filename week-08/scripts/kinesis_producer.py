"""
Week 8 - Kinesis Data Streams Producer

AWS calls have been commented out until AWS resources
and permissions are configured.

This implementation follows the FinTrust streaming
architecture presented during Week 8.
"""

# import boto3
import json
import uuid
import datetime

# kinesis = boto3.client(
#     "kinesis",
#     region_name="af-south-1"
# )

STREAM_NAME = "transaction-stream"


def publish_transaction(account_id, amount, currency, tx_type):
    event = {
        "transaction_id": str(uuid.uuid4()),
        "account_id": account_id,
        "amount": amount,
        "currency": currency,
        "type": tx_type,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

    print("Prepared transaction event:")
    print(json.dumps(event, indent=4))

    print(f"Partition Key: {account_id}")

    # response = kinesis.put_record(
    #     StreamName=STREAM_NAME,
    #     Data=json.dumps(event).encode("utf-8"),
    #     PartitionKey=account_id
    # )
    #
    # return (
    #     response["SequenceNumber"],
    #     response["ShardId"]
    # )

    print("AWS execution disabled.")


publish_transaction(
    account_id="ACC-0001",
    amount=1500.00,
    currency="ZAR",
    tx_type="PAYMENT"
)