import boto3
import json
from collections import defaultdict
from datetime import date


# AWS clients
tagging = boto3.client(
    "resourcegroupstaggingapi",
    region_name="af-south-1"
)

s3 = boto3.client("s3")


# FinTrust required tags
REQUIRED_TAGS = [
    "CostCentre",
    "Team",
    "Environment"
]

# Governance report destination
BUCKET_NAME = "fintrust-governance"


def audit_tag_compliance():
    """
    Scan all tagged resources and identify resources
    missing one or more required tags.

    Returns:
        tuple:
            total_scanned: Total number of resources scanned.
            non_compliant: Dictionary mapping resource ARN
                           to missing tags.
    """

    total_scanned = 0
    non_compliant = {}

    paginator = tagging.get_paginator("get_resources")

    for page in paginator.paginate():
        for resource in page["ResourceTagMappingList"]:

            total_scanned += 1

            arn = resource["ResourceARN"]

            existing_keys = {
                tag["Key"]
                for tag in resource.get("Tags", [])
            }

            missing = [
                tag
                for tag in REQUIRED_TAGS
                if tag not in existing_keys
            ]

            if missing:
                non_compliant[arn] = missing

    return total_scanned, non_compliant


def group_violations_by_service(violations):
    """
    Group violations by AWS service.
    """

    by_service = defaultdict(int)

    for arn in violations:

        parts = arn.split(":")

        service = (
            parts[2]
            if len(parts) > 2
            else "unknown"
        )

        by_service[service] += 1

    return dict(sorted(by_service.items()))


def auto_remediate(violations):
    """
    Attempt to apply Environment=Production
    to every non-compliant resource.

    This is intentionally implemented for the lab activity.
    Applying Production to an actual development resource
    would be risky in a real environment.
    """

    successes = 0
    failures = 0

    for arn in violations:

        try:
            response = tagging.tag_resources(
                ResourceARNList=[arn],
                Tags={
                    "Environment": "Production"
                }
            )

            failed_resources = response.get(
                "FailedResourcesMap",
                {}
            )

            if arn in failed_resources:
                failures += 1

                failure_details = failed_resources[arn]

                print(
                    f"FAILED: {arn} - "
                    f"{failure_details}"
                )

            else:
                successes += 1

                print(
                    f"REMEDIATED: {arn}"
                )

        except Exception as exc:

            failures += 1

            print(
                f"FAILED: {arn} - {exc}"
            )

    return successes, failures


def upload_report(summary):
    """
    Upload the governance summary as JSON to S3.
    """

    today = date.today().strftime("%Y-%m-%d")

    key = (
        f"tag-audit/"
        f"{today}.json"
    )

    body = json.dumps(
        summary,
        indent=2
    ).encode("utf-8")

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=body,
        ContentType="application/json"
    )

    return key


def main():

    print("FinTrust Governance Report")
    print("=" * 80)

    # --------------------------------------------------
    # Step 1: Initial compliance audit
    # --------------------------------------------------

    total_scanned, initial_violations = (
        audit_tag_compliance()
    )

    initial_violation_count = len(
        initial_violations
    )

    print(
        f"\nTotal resources scanned: "
        f"{total_scanned}"
    )

    print(
        f"Initial violations: "
        f"{initial_violation_count}"
    )

    # Record violations by service before remediation
    violations_by_service = (
        group_violations_by_service(
            initial_violations
        )
    )

    # --------------------------------------------------
    # Step 2: Auto-remediation
    # --------------------------------------------------

    print("\nStarting auto-remediation...")

    auto_remediated, remediation_failures = (
        auto_remediate(initial_violations)
    )

    print(
        f"\nAuto-remediated: "
        f"{auto_remediated}"
    )

    print(
        f"Remediation failures: "
        f"{remediation_failures}"
    )

    # --------------------------------------------------
    # Step 3: Re-run compliance audit
    # --------------------------------------------------

    _, remaining_violations = (
        audit_tag_compliance()
    )

    remaining_violation_count = len(
        remaining_violations
    )

    print(
        f"\nRemaining violations: "
        f"{remaining_violation_count}"
    )

    # --------------------------------------------------
    # Step 4: Build and upload JSON report
    # --------------------------------------------------

    summary = {
        "total_scanned": total_scanned,
        "initial_violations": initial_violation_count,
        "auto_remediated": auto_remediated,
        "remaining_violations": remaining_violation_count,
        "violations_by_service": violations_by_service
    }

    print("\nGovernance Summary")
    print("-" * 80)

    print(
        json.dumps(
            summary,
            indent=2
        )
    )

    key = upload_report(summary)

    print(
        f"\nReport uploaded to:"
        f"\ns3://{BUCKET_NAME}/{key}"
    )


if __name__ == "__main__":
    main()