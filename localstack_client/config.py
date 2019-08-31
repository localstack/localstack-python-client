import os
import json
from six.moves.urllib.parse import urlparse

_service_endpoints_template = {
    'apigateway': '{proto}://{host}:4567',
    'kinesis': '{proto}://{host}:4568',
    'dynamodb': '{proto}://{host}:4569',
    'dynamodbstreams': '{proto}://{host}:4570',
    'elasticsearch': '{proto}://{host}:4571',
    's3': '{proto}://{host}:4572',
    'firehose': '{proto}://{host}:4573',
    'lambda': '{proto}://{host}:4574',
    'sns': '{proto}://{host}:4575',
    'sqs': '{proto}://{host}:4576',
    'redshift': '{proto}://{host}:4577',
    'es': '{proto}://{host}:4578',
    'ses': '{proto}://{host}:4579',
    'route53': '{proto}://{host}:4580',
    'cloudformation': '{proto}://{host}:4581',
    'cloudwatch': '{proto}://{host}:4582',
    'ssm': '{proto}://{host}:4583',
    'secretsmanager': '{proto}://{host}:4584',
    'stepfunctions': '{proto}://{host}:4585',
    'logs': '{proto}://{host}:4586',
    'events': '{proto}://{host}:4587',
    'elb': '{proto}://{host}:4588',
    'iot': '{proto}://{host}:4589',
    'iotanalytics': '{proto}://{host}:4589',
    'iotevents': '{proto}://{host}:4589',
    'iotevents-data': '{proto}://{host}:4589',
    'iot-data': '{proto}://{host}:4589',
    'iot-jobs-data': '{proto}://{host}:4589',
    'cognito-idp': '{proto}://{host}:4590',
    'cognito-identity': '{proto}://{host}:4591',
    'sts': '{proto}://{host}:4592',
    'iam': '{proto}://{host}:4593',
    'rds': '{proto}://{host}:4594',
    'cloudsearch': '{proto}://{host}:4595',
    'swf': '{proto}://{host}:4596',
    'ec2': '{proto}://{host}:4597',
    'elasticache': '{proto}://{host}:4598',
    'kms': '{proto}://{host}:4599',
    'emr': '{proto}://{host}:4600',
    'ecs': '{proto}://{host}:4601',
    'eks': '{proto}://{host}:4602'
}


def get_service_endpoint(service, localstack_host=None):
    endpoints = get_service_endpoints(localstack_host=localstack_host)
    return endpoints.get(service)


def get_service_endpoints(localstack_host=None):
    if localstack_host is None:
        localstack_host = os.environ.get('LOCALSTACK_HOST', 'localhost')
    protocol = 'https' if os.environ.get('USE_SSL') in ('1', 'true') else 'http'

    return json.loads(json.dumps(_service_endpoints_template)
        .replace('{proto}', protocol).replace('{host}', localstack_host))


def get_service_port(service):
    ports = get_service_ports()
    return ports.get(service)


def get_service_ports():
    endpoints = get_service_endpoints()
    result = {}
    for service, url in endpoints.items():
        result[service] = urlparse(url).port
    return result
