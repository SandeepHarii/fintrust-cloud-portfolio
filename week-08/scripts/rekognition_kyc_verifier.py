"""
Week 8 - FinTrust KYC Face Verification

AWS calls have been commented out until AWS resources
and permissions are configured.

This script demonstrates the Rekognition CompareFaces
workflow used for customer onboarding.
"""

# import boto3
import json

# rek = boto3.client(
#     "rekognition",
#     region_name="af-south-1"
# )


def kyc_verify(
    selfie_bucket,
    selfie_key,
    id_bucket,
    id_key,
    threshold=95.0
):

    # response = rek.compare_faces(
    #     SourceImage={
    #         "S3Object": {
    #             "Bucket": selfie_bucket,
    #             "Name": selfie_key
    #         }
    #     },
    #     TargetImage={
    #         "S3Object": {
    #             "Bucket": id_bucket,
    #             "Name": id_key
    #         }
    #     },
    #     SimilarityThreshold=threshold
    # )

    result = {
        "match": True,
        "similarity": 98.7,
        "decision": "APPROVE",
        "reason": (
            f"Face similarity 98.7% "
            f"(threshold {threshold}%)"
        )
    }

    return result


result = kyc_verify(
    "fintrust-kyc-uploads",
    "customers/ACC-0001/selfie.jpg",
    "fintrust-kyc-uploads",
    "customers/ACC-0001/id_front.jpg"
)

print(json.dumps(result, indent=2))