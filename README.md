# LocalStack Python Client

This is an easy-to-use Python client for [LocalStack](https://github.com/localstack/localstack).
The client library provides a thin wrapper around [boto3](https://github.com/boto/boto3) which
automatically configures the target endpoints to use LocalStack for your local cloud
application development.

## Prerequisites

To make use of this library, you need to have [LocalStack](https://github.com/localstack/localstack)
installed on your local machine. In particular, the `localstack` command needs to be available.

## Installation

The easiest way to install *LocalStack* is via `pip`:

```
pip install localstack-client
```

## Usage

This library provides an API that is identical to `boto3`'s. For example, to list the SQS queues
in your local (LocalStack) environment, use the following code:

```
import localstack_client.session

session = localstack_client.session.Session()
sqs = session.client('sqs')
assert sqs.list_queues() is not None
```

If you use `boto3.client` directly in your code, you can mock it.

```
import localstack_client.session
import pytest


@pytest.fixture(autouse=True)
def boto3_localstack_patch(monkeypatch):
    session_ls = localstack_client.session.Session()
    monkeypatch.setattr(boto3, "client", session_ls.client)
    monkeypatch.setattr(boto3, "resource", session_ls.resource)
```

```
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

* v1.10: Add endpoint for ELBv2
* v1.7: Add endpoints for AWS API GW Management, Timestream, S3 Control, and others
* v1.5: Add endpoint for AWS Application Autoscaling, Kafka (MSK)
* v1.4: Configure USE_LEGACY_PORTS=0 by default to accommodate upstream changes
* v1.2: Add endpoint for AWS Amplify
* v1.1: Add USE_LEGACY_PORTS config to disable using legacy ports
* v1.0: Switch to using edge port for all service endpoints by default
* v0.25: Add endpoint for AWS Kinesis Analytics; prepare for replacing service ports with edge port
* v0.24: Add endpoints for AWS Transfer, ACM, and CodeCommit
* v0.23: Add endpoints for AWS Autoscaling and MediaStore
* v0.22: Import boto3 under different name to simplify mocking
* v0.20: Add endpoints for AWS CloudTrail, Glacier, Batch, Organizations
* v0.19: Add endpoints for AWS ECR and QLDB
* v0.18: Add endpoint for AWS API Gateway V2
* v0.16: Add endpoint for AWS SageMaker
* v0.15: Add endpoint for AWS Glue
* v0.14: Add endpoint for AWS Athena
* v0.13: Add endpoint for AWS CloudFront
* v0.8: Add more service endpoint mappings that will be implemented in the near future
* v0.7: Add endpoint for AWS Step Functions
* v0.6: Add endpoint for AWS Secrets Manager
* v0.5: Fix passing of credentials to client session
* v0.4: Add functions to retrieve service port mappings
* v0.3: Add new service endpoints
* v0.2: Add missing service endpoints; enable SSL connections; put default endpoints into `config.py`
* v0.1: Initial version

## License

The LocalStack Python Client is released under the Apache License, Version 2.0 (see `LICENSE`).
