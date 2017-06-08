from localstack_client import localstack_client


def test_session():
    session = localstack_client.Session()
    sqs = session.client('sqs')
    assert sqs.list_queues() is not None
