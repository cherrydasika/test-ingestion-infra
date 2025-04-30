from aws_cdk import CfnOutput, Stage
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from constructs import Construct

from test_ingestion_infra.my_app_stack import MyBucketStack


class BucketCreationStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        bucket_stack = MyBucketStack(
            self, "MyBucketStack", bucket_name="mars-opportunity-flyby-v01"
        )


class RdsCreationStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        pass
