from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy
from constructs import Construct


class ProducerStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.bucket = s3.Bucket(
            self,
            "SharedBucket",
            bucket_name="shared-bucket-cdk-example-1234567890",  # <-- your unique bucket name
            versioned=True,
        )

        # Upload the scripts to the bucke
        s3deploy.BucketDeployment(
            self,
            "DeployFiles",
            sources=[
                s3deploy.Source.asset(
                    "C:\\D\\github\\test-ingestion-infra\\test_ingestion_infra\\local_files"
                )
            ],  # <-- your local folder
            destination_bucket=self.bucket,
            destination_key_prefix="uploaded/",  # optional folder prefix inside the bucket
        )

        # Export the bucket name
        CfnOutput(
            self,
            "BucketNameExport",
            value=self.bucket.bucket_name,
            export_name="SharedBucketName",
        )
