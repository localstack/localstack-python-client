# LocalStack Python Client Change Log

* v2.9: Add endpoints for Account Management, Private Certificate Authority, Bedrock, CloudControl, CodeBuild, CodeCommit, CodeConnections, CodeDeploy, CodePipeline, ElasticTranscoder, MemoryDB, Shield, Textract and Verified Permissions
* v2.8: Removes support for python `3.6` and `3.7` and adds `3.12` and `3.13` for parity with boto3
* v2.7: Add endpoint config for EventBridge Pipes
* v2.6: Add endpoint config for Pinpoint
* v2.5: Add endpoint config for AppConfig Data
* v2.4: Add endpoint config for Resource Access Manager
* v2.3: Add endpoint config for Amazon EventBridge Scheduler
* v2.2: Add endpoint configs for `emr-serverless` and a few other services
* v2.1: Consider `AWS_ENDPOINT_URL` configuration when resolving service endpoints
* v2.0: Change `LOCALSTACK_HOSTNAME` from `<hostname>` to `<hostname>:<port>`; remove `EDGE_PORT` environment variable
* v1.39: Add endpoint for Amazon MQ
* v1.38: Add `enable_local_endpoints()` util function; slight project refactoring, migrate from `nose` to `pytests`
* v1.37: Add endpoint for Amazon Transcribe
* v1.36: Add endpoints for Fault Injection Service (FIS) and Marketplace Metering
* v1.35: Add endpoint for Amazon Managed Workflows for Apache Airflow (MWAA)
* v1.33: Patch botocore to skip adding `data-` host prefixes to endpoint URLs; remove six dependency
* v1.32: Add endpoint for KinesisAnalyticsV2
* v1.31: Revert mapping for OpenSearch (drop support for `OPENSEARCH_ENDPOINT_STRATEGY=off`)
* v1.30: Allow legacy port handling for OpenSearch (to support `OPENSEARCH_ENDPOINT_STRATEGY=off`)
* v1.29: Add endpoint for OpenSearch
* v1.28: Add endpoint for Route53Resolver
* v1.27: Add endpoint for SESv2
* v1.25: Remove mapping for deprecated/disabled Web UI on port 8080
* v1.24: Add endpoints for Config Service
* v1.23: Add endpoints for QLDB Session
* v1.22: Add endpoints for LakeFormation and WAF/WAFv2
* v1.21: Add endpoint for AWS Backup API
* v1.20: Add endpoint for Resource Groups API
* v1.19: Add endpoints for Resource Groups Tagging API
* v1.18: Add endpoints for AppConfig, CostExplorer, MediaConvert
* v1.17: Add endpoint for ServerlessApplicationRepository
* v1.16: Add endpoints for AWS Support and ServiceDiscovery (CloudMap)
* v1.14: Add endpoint for IoT Wireless
* v1.13: Add endpoints for NeptuneDB and DocumentDB
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
