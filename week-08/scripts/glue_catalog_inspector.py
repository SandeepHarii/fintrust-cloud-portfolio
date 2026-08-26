"""
Week 8 - Glue Data Catalog Inspector

AWS calls have been commented out until AWS resources
and permissions are configured.

This script demonstrates how FinTrust would inspect
the Glue Data Catalog programmatically.
"""

# import boto3

# glue = boto3.client(
#     "glue",
#     region_name="af-south-1"
# )


def list_databases():

    print("Databases:")

    # response = glue.get_databases()
    #
    # for db in response["DatabaseList"]:
    #     print(f"Database: {db['Name']}")

    print("AWS execution disabled.")


def list_tables(database):

    print(f"\nTables in database: {database}")

    # response = glue.get_tables(
    #     DatabaseName=database
    # )
    #
    # for table in response["TableList"]:
    #     print(
    #         f"Table: {table['Name']}"
    #     )

    print("AWS execution disabled.")


def show_schema(database, table_name):

    print(
        f"\nSchema inspection for "
        f"{database}.{table_name}"
    )

    # response = glue.get_table(
    #     DatabaseName=database,
    #     Name=table_name
    # )
    #
    # columns = (
    #     response["Table"]
    #     ["StorageDescriptor"]
    #     ["Columns"]
    # )
    #
    # for column in columns:
    #     print(
    #         f"{column['Name']} : "
    #         f"{column['Type']}"
    #     )

    print("AWS execution disabled.")


list_databases()
list_tables("fintrust_curated")
show_schema(
    "fintrust_curated",
    "transactions"
)