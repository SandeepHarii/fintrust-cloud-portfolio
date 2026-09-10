import boto3

sc = boto3.client(
    "servicecatalog",
    region_name="af-south-1"
)


def get_all_portfolios():
    """
    Collect portfolios from both accepted shares
    and portfolios owned by the current account.
    """

    accepted_shares = sc.list_accepted_portfolio_shares(
        PageSize=100
    )

    shared_portfolios = accepted_shares.get(
        "PortfolioDetails",
        []
    )

    own_portfolios = sc.list_portfolios(
        PageSize=100
    ).get(
        "PortfolioDetails",
        []
    )

    # Use the portfolio ID as the dictionary key
    # to remove duplicates.
    all_portfolios = {
        portfolio["Id"]: portfolio
        for portfolio in (
            shared_portfolios + own_portfolios
        )
    }

    return all_portfolios


def list_products(portfolio_id):
    """
    List Service Catalog products in a portfolio.
    """

    response = sc.search_products_as_admin(
        PortfolioId=portfolio_id
    )

    return response.get(
        "ProductViewDetails",
        []
    )


def main():
    portfolios = get_all_portfolios()

    print("FinTrust AWS Service Catalog")
    print("=" * 80)

    if not portfolios:
        print("No Service Catalog portfolios found.")
        return

    for portfolio_id, portfolio in portfolios.items():

        print()
        print(
            f"Portfolio: {portfolio['DisplayName']}"
        )
        print(
            f"ID: {portfolio_id}"
        )
        print("-" * 80)

        products = list_products(portfolio_id)

        if not products:
            print("  No products found.")
            continue

        for product_view in products:
            product = product_view[
                "ProductViewSummary"
            ]

            print(
                f"  Product: {product['Name']}"
            )
            print(
                f"    Type: {product['Type']}"
            )
            print(
                f"    Owner: {product['Owner']}"
            )
            print(
                f"    Product ID: {product['ProductId']}"
            )


if __name__ == "__main__":
    main()