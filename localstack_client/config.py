import os
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse

# note: leave this import here for now, as some upstream code is depending on it (TODO needs to be updated)
from localstack_client.patch import patch_expand_host_prefix  # noqa

# central entrypoint port for all LocalStack API endpoints
DEFAULT_EDGE_PORT = 4566

# TODO: deprecated, remove!
# NOTE: The ports listed below will soon become deprecated/removed, as the default in the
# latest version is to access all services via a single "edge service" (port 4566 by default)
_service_ports: Dict[str, int] = {
    "edge": 4566,
    # Botocore services
    # When adding new services below, assign them port 4566
    "account": 4566,
    "acm": 4619,
    "acm-pca": 4566,
    "amplify": 4622,
    "apigateway": 4567,
    "apigatewaymanagementapi": 4625,
    "apigatewayv2": 4567,
    "appconfig": 4632,
    "appconfigdata": 4632,
    "appflow": 4566,
    "application-autoscaling": 4623,
    "appsync": 4605,
    "athena": 4607,
    "autoscaling": 4616,
    "backup": 4638,
    "batch": 4614,
    "bedrock": 4566,
    "ce": 4633,
    "cloudcontrol": 4566,
    "cloudformation": 4581,
    "cloudfront": 4606,
    "cloudsearch": 4595,
    "cloudtrail": 4612,
    "cloudwatch": 4582,
    "codebuild": 4566,
    "codecommit": 4620,
    "codeconnections": 4566,
    "codedeploy": 4566,
    "codepipeline": 4566,
    "cognito-identity": 4591,
    "cognito-idp": 4590,
    "config": 4641,
    "configservice": 4641,
    "docdb": 4594,
    "dynamodb": 4569,
    "dynamodbstreams": 4570,
    "ec2": 4597,
    "ecr": 4610,
    "ecs": 4601,
    "efs": 4637,
    "eks": 4602,
    "elasticache": 4598,
    "elasticbeanstalk": 4604,
    "elasticsearch": 4571,
    "elastictranscoder": 4566,
    "elb": 4588,
    "elbv2": 4628,
    "emr": 4600,
    "emr-serverless": 4566,
    "es": 4578,
    "events": 4587,
    "firehose": 4573,
    "fis": 4643,
    "glacier": 4613,
    "glue": 4608,
    "iam": 4593,
    "iot": 4589,
    "iotanalytics": 4589,
    "iot-data": 4589,
    "iotevents": 4589,
    "iotevents-data": 4589,
    "iot-jobs-data": 4589,
    "iotwireless": 4589,
    "kafka": 4624,
    "keyspaces": 4566,
    "kinesis": 4568,
    "kinesisanalytics": 4621,
    "kinesisanalyticsv2": 4621,
    "kms": 4599,
    "lakeformation": 4639,
    "lambda": 4574,
    "logs": 4586,
    "mediaconvert": 4634,
    "mediastore": 4617,
    "mediastore-data": 4617,
    "meteringmarketplace": 4644,
    "memorydb": 4566,
    "mq": 4566,
    "mwaa": 4642,
    "neptune": 4594,
    "opensearch": 4578,
    "organizations": 4615,
    "pinpoint": 4566,
    "pipes": 4566,
    "qldb": 4611,
    "qldb-session": 4611,
    "ram": 4566,
    "rds": 4594,
    "rds-data": 4594,
    "redshift": 4577,
    "redshift-data": 4577,
    "resource-groups": 4636,
    "resourcegroupstaggingapi": 4635,
    "route53": 4580,
    "route53domains": 4566,
    "route53resolver": 4580,
    "s3": 4572,
    "s3control": 4627,
    "s3tables": 4566,
    "sagemaker": 4609,
    "sagemaker-runtime": 4609,
    "scheduler": 4566,
    "secretsmanager": 4584,
    "serverlessrepo": 4631,
    "servicediscovery": 4630,
    "ses": 4579,
    "sesv2": 4579,
    "shield": 4566,
    "sns": 4575,
    "sqs": 4576,
    "ssm": 4583,
    "stepfunctions": 4585,
    "sts": 4592,
    "support": 4629,
    "swf": 4596,
    "timestream": 4626,
    "timestream-query": 4626,
    "timestream-write": 4626,
    "transcribe": 4566,
    "transfer": 4618,
    "verifiedpermissions": 4566,
    "waf": 4640,
    "wafv2": 4640,
    "xray": 4603,
}

# TODO remove service port mapping above entirely
if os.environ.get("USE_LEGACY_PORTS") not in ["1", "true"]:
    for key, value in _service_ports.items():
        if key not in ["dashboard", "elasticsearch"]:
            _service_ports[key] = DEFAULT_EDGE_PORT


def parse_localstack_host(given: str) -> Tuple[str, int]:
    parts = given.split(":", 1)
    if len(parts) == 1:
        # just hostname
        return parts[0].strip() or "localhost", DEFAULT_EDGE_PORT
    elif len(parts) == 2:
        hostname = parts[0].strip() or "localhost"
        port_s = parts[1]
        try:
            port = int(port_s)
            return (hostname, port)
        except Exception:
            raise RuntimeError(f"could not parse {given} into <hostname>:<port>")
    else:
        raise RuntimeError(f"could not parse {given} into <hostname>:<port>")


def get_service_endpoints(localstack_host: Optional[str] = None) -> Dict[str, str]:
    """
    Return the local endpoint URLs for the list of supported boto3 services (e.g., "s3", "lambda", etc).
    If $AWS_ENDPOINT_URL is configured in the environment, it is returned directly. Otherwise,
    the service endpoint is constructed from the dict of service ports (usually http://localhost:4566).
    """
    env_endpoint_url = os.environ.get("AWS_ENDPOINT_URL", "").strip()
    if env_endpoint_url:
        return {key: env_endpoint_url for key in _service_ports.keys()}

    if localstack_host is None:
        localstack_host = os.environ.get(
            "LOCALSTACK_HOST", f"localhost:{DEFAULT_EDGE_PORT}"
        )

    hostname, port = parse_localstack_host(localstack_host)

    protocol = "https" if os.environ.get("USE_SSL") in ("1", "true") else "http"

    return {key: f"{protocol}://{hostname}:{port}" for key in _service_ports.keys()}


def get_service_endpoint(
    service: str, localstack_host: Optional[str] = None
) -> Optional[str]:
    endpoints = get_service_endpoints(localstack_host=localstack_host)
    return endpoints.get(service)


def get_service_port(service: str) -> Optional[int]:
    ports = get_service_ports()
    return ports.get(service)


def get_service_ports() -> Dict[str, int]:
    endpoints = get_service_endpoints()
    result = {}
    for service, url in endpoints.items():
        result[service] = urlparse(url).port
    return result
