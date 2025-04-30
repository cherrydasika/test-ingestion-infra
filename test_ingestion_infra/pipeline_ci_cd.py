import aws_cdk.aws_codebuild as codebuild
import aws_cdk.aws_iam as iam
from aws_cdk import Stack
from aws_cdk.pipelines import (CodeBuildOptions, CodePipeline,
                               CodePipelineSource, ShellStep)
from constructs import Construct

from test_ingestion_infra.my_app_stage import BucketCreationStage


class CdkPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="MyCdkAppPipeline",
            cross_account_keys=False,
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.connection(
                    repo_string="cherrydasika/test-ingestion-infra",
                    branch="dev",
                    connection_arn=self.node.try_get_context(
                        "github_connection"
                    ),  # supply via cdk.json or CLI
                ),
                commands=[
                    "npm install -g aws-cdk",
                    "curl -sSL https://install.python-poetry.org | python3 -",
                    "export PATH=$HOME/.local/bin:$PATH",
                    "poetry install --no-interaction --no-root --without dev,test,typing",
                    "poetry run cdk synth",
                ],
            ),
            code_build_defaults=CodeBuildOptions(
                role_policy=[
                    iam.PolicyStatement(
                        actions=["sts:GetServiceBearerToken", "codeartifact:*"],
                        resources=["*"],
                    )
                ]
            ),
            docker_enabled_for_synth=True,
        )

        # Add application stage (can be reused across environments)
        s3_bucket_stage = BucketCreationStage(
            self,
            "dev",
            env={
                "account": self.node.try_get_context("dev_account_id"),
                "region": "eu-west-2",
            },
        )
        pipeline.add_stage(s3_bucket_stage)

        # You could add a prod stage as well:
        # prod = MyAppStage(self, "Prod", env={"account": "...", "region": "..."})
        # pipeline.add_stage(prod)
