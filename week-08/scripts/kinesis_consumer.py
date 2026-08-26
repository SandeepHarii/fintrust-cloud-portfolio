"""
Week 8 - Kinesis Consumer

AWS calls have been commented out until AWS resources
and permissions are configured.

This script demonstrates the Lambda-style consumer
pattern used by FinTrust.
"""

import base64
import json


def lambda_handler(event, context):

    for record in event["Records"]:

        raw = base64.b64decode(
            record["kinesis"]["data"]
        )

        transaction = json.loads(
            raw.decode("utf-8")
        )

        print(
            f"Received: {transaction['transaction_id']} | "
            f"Account: {transaction['account_id']} | "
            f"Amount: {transaction['amount']} "
            f"{transaction['currency']}"
        )

        # Future processing:
        # - Fraud detection
        # - OpenSearch indexing
        # - Compliance auditing
        # - Alert generation


simulated_event = {
    "Records": [
        {
            "kinesis": {
                "data": base64.b64encode(
                    json.dumps(
                        {
                            "transaction_id": "txn-test-001",
                            "account_id": "ACC-0001",
                            "amount": 15000.00,
                            "currency": "ZAR",
                            "type": "PAYMENT"
                        }
                    ).encode()
                ).decode()
            }
        }
    ]
}

lambda_handler(simulated_event, None)