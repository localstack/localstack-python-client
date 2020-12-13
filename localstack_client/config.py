import os
import json
from six.moves.urllib.parse import urlparse

# central entrypoint port for all LocalStack API endpoints
EDGE_PORT = int(os.environ.get('EDGE_PORT') or 4566)

# NOTE: The endpoints below will soon become deprecated/removed, as the default in the
# latest version is to access all services via a single "edge service" (port 4566 by default)
_service_endpoints_template = {
    'dashboard': '{proto}://{host}:8080',
    'edge': '{proto}://{host}:4566',
    'apigateway': '{proto}://{host}:4567',
    'apigatewayv2': '{proto}://{host}:4567',
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
    'redshift-data': '{proto}://{host}:4577',
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
    'rds-data': '{proto}://{host}:4594',
    'cloudsearch': '{proto}://{host}:4595',
    'swf': '{proto}://{host}:4596',
    'ec2': '{proto}://{host}:4597',
    'elasticache': '{proto}://{host}:4598',
    'kms': '{proto}://{host}:4599',
    'emr': '{proto}://{host}:4600',
    'ecs': '{proto}://{host}:4601',
    'eks': '{proto}://{host}:4602',
    'xray': '{proto}://{host}:4603',
    'elasticbeanstalk': '{proto}://{host}:4604',
    'appsync': '{proto}://{host}:4605',
    'cloudfront': '{proto}://{host}:4606',
    'athena': '{proto}://{host}:4607',
    'glue': '{proto}://{host}:4608',
    'sagemaker': '{proto}://{host}:4609',
    'sagemaker-runtime': '{proto}://{host}:4609',
    'ecr': '{proto}://{host}:4610',
    'qldb': '{proto}://{host}:4611',
    'cloudtrail': '{proto}://{host}:4612',
    'glacier': '{proto}://{host}:4613',
    'batch': '{proto}://{host}:4614',
    'organizations': '{proto}://{host}:4615',
    'autoscaling': '{proto}://{host}:4616',
    'mediastore': '{proto}://{host}:4617',
    'mediastore-data': '{proto}://{host}:4617',
    'transfer': '{proto}://{host}:4618',
    'acm': '{proto}://{host}:4619',
    'codecommit': '{proto}://{host}:4620',
    'kinesisanalytics': '{proto}://{host}:4621',
    'amplify': '{proto}://{host}:4622',
    'application-autoscaling': '{proto}://{host}:4623',
    'kafka': '{proto}://{host}:4624',
    'apigatewaymanagementapi': '{proto}://{host}:4625',
    'timestream': '{proto}://{host}:4626',
    'timestream-query': '{proto}://{host}:4626',
    'timestream-write': '{proto}://{host}:4626',
    's3control': '{proto}://{host}:4627',
    'elbv2': '{proto}://{host}:4628',
}

# TODO remove service port mapping above entirely
if os.environ.get('USE_LEGACY_PORTS') not in ['1', 'true']:
    for key, value in _service_endpoints_template.items():
        if key not in ['dashboard', 'elasticsearch']:
            _service_endpoints_template[key] = '%s:%s' % (value.rpartition(':')[0], EDGE_PORT)


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
