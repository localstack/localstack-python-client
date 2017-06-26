# LocalStack Python Client

This is an easy-to-use Python client for [LocalStack](https://github.com/atlassian/localstack).
The client library provides a thin wrapper around [boto3](https://github.com/boto/boto3) which
automatically configures the target endpoints to use LocalStack for your local cloud
application development.

## Prerequisites

To make use of this library, you need to have [LocalStack](https://github.com/atlassian/localstack)
installed on your local machine. In particular, the `localstack` command needs to be available.

## Installation

The easiest way to install *LocalStack* is via `pip`:

```
pip install localstack-client
```

## Usage

This library provides an API that is equivalent to `boto3`. For example, to list the SQS queues
in your local (LocalStack) environment, use the following code:

```
from localstack_client import localstack_client

session = localstack_client.Session()
sqs = session.client('sqs')
assert sqs.list_queues() is not None
```

## Developing

We welcome feedback, bug reports, and pull requests!

Use these commands to get you started and test your code:

```
make install
make test
```

## License

The LocalStack Python Client is released under the Apache License, Version 2.0 (see `LICENSE`).
