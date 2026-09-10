import boto3
from collections import defaultdict

tagging = boto3.client(
    "resourcegroupstaggingapi",
    region_name="af-south-1"
)

REQUIRED_TAGS = [
    "CostCentre",
    "Team",
    "Environment"
]


def audit_tag_compliance():
    """
    Scan all tagged resources in the account and identify
    resources missing one or more required tags.

    Returns:
        dict: Resource ARN mapped to a list of missing tags.
    """

    non_compliant = {}

    paginator = tagging.get_paginator("get_resources")

    for page in paginator.paginate():
        for resource in page["ResourceTagMappingList"]:
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

    return non_compliant


violations = audit_tag_compliance()

print("FinTrust Tag Compliance Audit")
print("-" * 80)
print(f"Non-compliant resources: {len(violations)}")


# Group violations by AWS service
by_type = defaultdict(list)

for arn, missing in violations.items():
    # ARN format:
    # arn:aws:service:region:account:resource
    parts = arn.split(":")

    service = (
        parts[2]
        if len(parts) > 2
        else "unknown"
    )

    by_type[service].append(
        (arn, missing)
    )


# Display violations by service
for service, items in sorted(by_type.items()):
    print(
        f"\n{service.upper()} "
        f"({len(items)} violations):"
    )

    for arn, missing in items[:3]:
        short_arn = "..." + arn[-40:]

        print(
            f"  {short_arn} "
            f"— missing: {', '.join(missing)}"
        )