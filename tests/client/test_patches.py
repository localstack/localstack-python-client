import uuid

import boto3
import pytest

from localstack_client.patch import (disable_local_endpoints,
                                     enable_local_endpoints)


def test_enable_local_endpoints(monkeypatch):
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")

    # create default client, requests should fail
    with pytest.raises(Exception):
        boto3.client("s3").list_buckets()
    with pytest.raises(Exception):
        resource = boto3.resource("s3")
        bucket_name = str(uuid.uuid4())
        resource.Bucket(bucket_name).create()

    # enable local endpoints, request should pass
    enable_local_endpoints()
    assert "Buckets" in boto3.client("s3").list_buckets()
    resource = boto3.resource("s3")
    bucket_name = str(uuid.uuid4())
    resource.Bucket(bucket_name).create()
    resource.Bucket(bucket_name).delete()

    # disable local endpoints again, request should fail
    disable_local_endpoints()
    with pytest.raises(Exception):
        boto3.client("s3").list_buckets()
    with pytest.raises(Exception):
        resource = boto3.resource("s3")
        bucket_name = str(uuid.uuid4())
        resource.Bucket(bucket_name).create()
