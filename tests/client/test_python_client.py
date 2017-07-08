import localstack_client.session


def test_session():
    session = localstack_client.session.Session()
    sqs = session.client('sqs')
    assert sqs.list_queues() is not None
