import localstack_client.session
from botocore.client import Config


def test_session():
    session = localstack_client.session.Session()
    sqs = session.client('sqs')
    assert sqs.list_queues() is not None


def test_client_kwargs_passed():
    """ Test kwargs passed through to boto3.client creation """
    session = localstack_client.session.Session()
    kwargs = {'config': Config(signature_version='s3v4')}
    sqs = session.client('sqs', **kwargs)
    assert sqs.meta.config.signature_version == 's3v4'


def test_protected_client_kwargs_not_passed():
    """ Test protected kwargs not overwritten in boto3.client creation """
    session = localstack_client.session.Session()
    kwargs = {'region_name': 'another_region'}
    sqs = session.client('sqs', **kwargs)
    assert not sqs.meta.region_name == 'another_region'


def test_resource_kwargs_passed():
    """ Test kwargs passed through to boto3.resource creation """
    session = localstack_client.session.Session()
    kwargs = {'config': Config(signature_version='s3v4')}
    sqs = session.resource('sqs', **kwargs)
    assert sqs.meta.client.meta.config.signature_version == 's3v4'


def test_protected_resource_kwargs_not_passed():
    """ Test protected kwargs not overwritten in boto3.resource creation """
    session = localstack_client.session.Session()
    kwargs = {'region_name': 'another_region'}
    sqs = session.resource('sqs', **kwargs)
    assert not sqs.meta.client.meta.region_name == 'another_region'
