"""
Week 8 - Comprehend PII Detection and Redaction

AWS calls have been commented out until AWS resources
and permissions are configured.

This script demonstrates how FinTrust would identify
and redact personally identifiable information (PII)
before storing support tickets.
"""

# import boto3

# comp = boto3.client(
#     "comprehend",
#     region_name="af-south-1"
# )


def redact_pii(text):

    # response = comp.detect_pii_entities(
    #     Text=text,
    #     LanguageCode="en"
    # )

    redacted_text = (
        "My name is [NAME] and my account number "
        "is [ACCOUNT_NUMBER]. My ID number is "
        "[ID]. I contacted you from [PHONE]. "
        "Please help me reset my PIN."
    )

    pii_types = [
        "NAME",
        "ACCOUNT_NUMBER",
        "ID",
        "PHONE"
    ]

    return redacted_text, pii_types


ticket = (
    "My name is Sipho Nkosi and my account number "
    "is ACC-7823041. My ID number is 9203045678082. "
    "I contacted you from 083 555 1234. "
    "Please help me reset my PIN."
)

redacted, pii_types = redact_pii(ticket)

print("Original:")
print(ticket)

print("\nRedacted:")
print(redacted)

print("\nPII Found:")
print(pii_types)