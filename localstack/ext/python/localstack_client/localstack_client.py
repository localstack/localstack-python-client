import os
import boto3.session
from botocore.credentials import Credentials

DEFAULT_SESSION = None


class Session():
    """
    This is a custom localstack session used to
    emulate the boto3.session object.
    """

    def __init__(self, aws_access_key_id='accesskey', aws_secret_access_key='secretkey',
                 aws_session_token='token', region_name='us-east-1',
                 botocore_session=None, profile_name=None, localstack_host=None):
        self.env = 'local'
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_session_token = aws_session_token
        self.region_name = region_name

        if localstack_host is None:
            localstack_host = os.environ.get('LOCALSTACK_HOST', 'localhost')

        self._service_endpoint_mapping = {
            'kinesis': 'http://%s:4568' % (localstack_host),
            'dynamodb': 'http://%s:4569' % (localstack_host),
            's3': 'http://%s:4572' % (localstack_host),
            'es': 'http://%s:4578' % (localstack_host),
            'firehose': 'http://%s:4573' % (localstack_host),
            'sqs': 'http://%s:4576' % (localstack_host)
        }

    def get_credentials(self):
        """
        Returns botocore.credential.Credential object.
        """
        return Credentials(access_key=self.aws_access_key_id,
                           secret_key=self.aws_secret_access_key,
                           token=self.aws_session_token)

    def client(self, service_name, **kwargs):
        if service_name not in self._service_endpoint_mapping:
            raise Exception('%s is not supported by this mock session.' % (service_name))

        return boto3.client(service_name, endpoint_url=self._service_endpoint_mapping[service_name],
                            region_name=self.region_name)

    def resource(self, service_name, **kwargs):
        if service_name not in self._service_endpoint_mapping:
            raise Exception('%s is not supported by this mock session.' % (service_name))
        return boto3.resource(service_name, endpoint_url=self._service_endpoint_mapping[service_name],
                              region_name=self.region_name)


def _get_default_session():
    global DEFAULT_SESSION

    if DEFAULT_SESSION is None:
        DEFAULT_SESSION = Session()

    return DEFAULT_SESSION


def client(*args, **kwargs):
    return _get_default_session.client(*args, **kwargs)


def resource(*args, **kwargs):
    return _get_default_session.resource(*args, **kwargs)
