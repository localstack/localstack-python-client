from boto3 import client as boto3_client
from boto3 import resource as boto3_resource
from botocore.credentials import Credentials
from localstack_client import config

DEFAULT_SESSION = None


class Session(object):
    """
    This is a custom LocalStack session used to
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
        self._service_endpoint_mapping = config.get_service_endpoints(localstack_host)

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

        return boto3_client(service_name,
            endpoint_url=self._service_endpoint_mapping[service_name],
            aws_access_key_id=self.aws_access_key_id, region_name=self.region_name,
            aws_secret_access_key=self.aws_secret_access_key, verify=False)

    def resource(self, service_name, **kwargs):
        if service_name not in self._service_endpoint_mapping:
            raise Exception('%s is not supported by this mock session.' % (service_name))

        return boto3_resource(service_name,
            endpoint_url=self._service_endpoint_mapping[service_name],
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name, verify=False)


def _get_default_session():
    global DEFAULT_SESSION

    if DEFAULT_SESSION is None:
        DEFAULT_SESSION = Session()

    return DEFAULT_SESSION


def client(*args, **kwargs):
    return _get_default_session().client(*args, **kwargs)


def resource(*args, **kwargs):
    return _get_default_session().resource(*args, **kwargs)
