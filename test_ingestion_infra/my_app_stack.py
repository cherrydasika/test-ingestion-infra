from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    CfnOutput
)
from constructs import Construct
import os

class MyBucketStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, bucket_name: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.bucket_name = bucket_name
        # 1. Create the S3 bucket
        self.bucket = s3.Bucket(self, "SharedBucket",
            bucket_name=self.bucket_name,  # must be globally unique
            versioned=True,
        )

        # 2. Upload local files to S3
        # Upload the scripts to the bucke
        s3deploy.BucketDeployment(self, "DeployFiles",
            sources=[s3deploy.Source.asset("C:\\D\\github\\test-ingestion-infra\\test_ingestion_infra\\local_files")],  # <-- your local folder
            destination_bucket=self.bucket,
            destination_key_prefix="uploaded/"  # optional folder prefix inside the bucket
        )

        # 3. Export the bucket name
        CfnOutput(self, "BucketNameExport",
            value=self.bucket.bucket_name,
            export_name="SharedBucketName"
        )
