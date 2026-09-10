import boto3
import json

# AWS Pricing API is always accessed through us-east-1
pricing = boto3.client(
    'pricing',
    region_name='us-east-1'
)


def get_ec2_ondemand_price(instance_type, region='af-south-1', os='Linux'):
    """
    Returns the hourly On-Demand price for an EC2 instance type in USD.
    Returns None if the instance type is not available in the region.
    """

    # AWS Pricing API uses long human-readable region names
    region_names = {
        'af-south-1': 'Africa (Cape Town)',
        'eu-west-1': 'Europe (Ireland)',
        'us-east-1': 'US East (N. Virginia)',
    }

    # Check that the region is supported by our mapping
    if region not in region_names:
        raise ValueError(
            f"Region '{region}' is not configured in region_names."
        )

    response = pricing.get_products(
        ServiceCode='AmazonEC2',
        Filters=[
            {
                'Type': 'TERM_MATCH',
                'Field': 'instanceType',
                'Value': instance_type
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'location',
                'Value': region_names[region]
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'operatingSystem',
                'Value': os
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'tenancy',
                'Value': 'Shared'
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'preInstalledSw',
                'Value': 'NA'
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'capacityStatus',
                'Value': 'Used'
            }
        ],
        MaxResults=1
    )

    # No matching product was found
    if not response['PriceList']:
        return None

    # PriceList contains JSON strings, so parse the first result
    product = json.loads(response['PriceList'][0])

    # Navigate through the nested AWS pricing structure
    terms = product['terms']['OnDemand']

    price_dimensions = next(
        iter(
            next(iter(terms.values()))['priceDimensions'].values()
        )
    )

    price_usd = float(
        price_dimensions['pricePerUnit']['USD']
    )

    return price_usd


# ---------------------------------------------------------
# Test 1: FinTrust EC2 instance types in Africa (Cape Town)
# ---------------------------------------------------------

instances = [
    'm5.xlarge',
    'r5.2xlarge',
    'c5.large'
]

print("EC2 On-Demand prices in Africa (Cape Town)")
print("-" * 55)

for instance in instances:

    price = get_ec2_ondemand_price(
        instance,
        region='af-south-1'
    )

    if price is not None:

        monthly_cost = price * 730

        print(
            f"{instance}: "
            f"${price:.4f}/hr = "
            f"${monthly_cost:.2f}/month"
        )

    else:

        print(
            f"{instance}: "
            f"price not found for af-south-1"
        )


# ---------------------------------------------------------
# Test 2: Compare m5.xlarge between Africa and Ireland
# ---------------------------------------------------------

print("\n")
print("m5.xlarge Regional Price Comparison")
print("-" * 55)

africa_price = get_ec2_ondemand_price(
    'm5.xlarge',
    region='af-south-1'
)

ireland_price = get_ec2_ondemand_price(
    'm5.xlarge',
    region='eu-west-1'
)


if africa_price is not None:

    print(
        f"Africa (Cape Town): "
        f"${africa_price:.4f}/hr = "
        f"${africa_price * 730:.2f}/month"
    )

else:

    print("Africa (Cape Town): price not found")


if ireland_price is not None:

    print(
        f"Europe (Ireland): "
        f"${ireland_price:.4f}/hr = "
        f"${ireland_price * 730:.2f}/month"
    )

else:

    print("Europe (Ireland): price not found")


# ---------------------------------------------------------
# Test 3: Check None handling
# ---------------------------------------------------------

print("\n")
print("Availability Check")
print("-" * 55)

# Deliberately use an instance type that may not exist
# in Africa (Cape Town)
unavailable_instance = 'c5.24xlarge'

unavailable_price = get_ec2_ondemand_price(
    unavailable_instance,
    region='af-south-1'
)

if unavailable_price is None:

    print(
        f"{unavailable_instance}: "
        f"No On-Demand price found in af-south-1"
    )

else:

    print(
        f"{unavailable_instance}: "
        f"${unavailable_price:.4f}/hr"
    )