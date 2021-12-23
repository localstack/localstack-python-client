# LocalStack Python Client

<p align="center">
    <a href="https://img.shields.io/pypi/v/localstack-client"><img src="https://img.shields.io/pypi/v/localstack-client" alt="PyPI version" height="18"></a>
    <img src="https://img.shields.io/badge/license-Apache License 2.0-brightgreen" alt="license Apache 2.0"/>
    <img src="https://github.com/localstack/localstack-python-client/actions/workflows/ci.yml/badge.svg" alt="GitHub-Actions-Build"/>
    <a href="https://pepy.tech/project/localstack-client"><img src="https://pepy.tech/badge/localstack-client" alt="PyPi downloads" height="18"></a>
</p>

This is an easy-to-use Python client for [LocalStack](https://github.com/localstack/localstack).
The client library provides a thin wrapper around [boto3](https://github.com/boto/boto3) which
automatically configures the target endpoints to use LocalStack for your local cloud
application development.

## Prerequisites

To make use of this library, you need to have [LocalStack](https://github.com/localstack/localstack) installed on your local machine. In particular, the `localstack` command needs to be available.

## Installation

The easiest way to install *LocalStack* is via `pip`:

```
pip install localstack-client
```

## Usage

This library provides an API that is identical to `boto3`'s. A minimal way to try it out is to replace `import boto3` with `import localstack_client.session as boto3`. This will allow your boto3 calls to work as normal.

For example, to list all s3 buckets in localstack:

```python
import localstack_client.session as boto3
client = boto3.client('s3')
response = client.list_buckets()
```

Another example below shows using `localstack_client` directly. To list the SQS queues
in your local (LocalStack) environment, use the following code:

```python
import localstack_client.session

session = localstack_client.session.Session()
sqs = session.client('sqs')
assert sqs.list_queues() is not None
```

If you use `boto3.client` directly in your code, you can mock it.

```python
import localstack_client.session
import pytest


@pytest.fixture(autouse=True)
def boto3_localstack_patch(monkeypatch):
    session_ls = localstack_client.session.Session()
    monkeypatch.setattr(boto3, "client", session_ls.client)
    monkeypatch.setattr(boto3, "resource", session_ls.resource)
```

```python
sqs = boto3.client('sqs')
assert sqs.list_queues() is not None  # list SQS in localstack
```

## Developing

We welcome feedback, bug reports, and pull requests!

Use these commands to get you started and test your code:

```
make install
make test
```

## Changelog

Please refer to [`CHANGELOG.md`](CHANGELOG.md) to see the complete list of changes for each release.

## License

The LocalStack Python Client is released under the Apache License, Version 2.0 (see `LICENSE`).
