# LocalStack Python Client Change Log

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
