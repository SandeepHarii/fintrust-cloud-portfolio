"""
Week 8 - FinTrust Support Ticket Processor

AWS calls have been commented out until AWS resources
and permissions are configured.

This script demonstrates how FinTrust would:
1. Detect and redact PII
2. Perform sentiment analysis
3. Route tickets to appropriate queues
"""

# import boto3
import json

# sqs = boto3.client(
#     "sqs",
#     region_name="af-south-1"
# )
#
# comp = boto3.client(
#     "comprehend",
#     region_name="af-south-1"
# )

URGENT_QUEUE_URL = (
    "https://sqs.af-south-1.amazonaws.com/"
    "ACCOUNT_ID/fintrust-support-urgent"
)

STANDARD_QUEUE_URL = (
    "https://sqs.af-south-1.amazonaws.com/"
    "ACCOUNT_ID/fintrust-support-standard"
)


def process_support_ticket(ticket_text):

    redacted_text = (
        "My name is [NAME]. "
        "My account number is [ACCOUNT_NUMBER]."
    )

    pii_types = [
        "NAME",
        "ACCOUNT_NUMBER"
    ]

    # sentiment_response = comp.detect_sentiment(
    #     Text=ticket_text,
    #     LanguageCode="en"
    # )

    sentiment = "NEGATIVE"

    queue_url = (
        URGENT_QUEUE_URL
        if sentiment == "NEGATIVE"
        else STANDARD_QUEUE_URL
    )

    message = {
        "redacted_text": redacted_text,
        "sentiment": sentiment,
        "pii_types_found": pii_types,
        "priority": (
            "HIGH"
            if sentiment == "NEGATIVE"
            else "STANDARD"
        )
    }

    # sqs.send_message(
    #     QueueUrl=queue_url,
    #     MessageBody=json.dumps(message)
    # )

    print("AWS queue routing disabled.")
    print(f"Would send to: {queue_url}")

    return message


ticket = (
    "My name is Sipho Nkosi and I am unable "
    "to access my account."
)

result = process_support_ticket(ticket)

print(json.dumps(result, indent=4))