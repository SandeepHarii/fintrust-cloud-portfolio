import boto3
import os


_session = None


def get_session():
    global _session

    if _session is None:
        _session = boto3.Session(
            region_name=os.getenv(
                "AWS_REGION",
                "af-south-1"
            ),
            profile_name=os.getenv(
                "AWS_PROFILE",
                "fintrust-migration"
            )
        )

    return _session


def get_client(service):
    return get_session().client(service)


def get_resource(service):
    return get_session().resource(service)