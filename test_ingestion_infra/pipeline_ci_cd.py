from aws_cdk import (
    Stack,
    SecretValue,
    aws_s3 as s3,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as cpactions,
    aws_codebuild as codebuild,
)
from constructs import Construct


class MyPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Artifact bucket (optional)
        artifact_bucket = s3.Bucket(self, "ArtifactBucket")

        # Pipeline artifacts
        source_output = codepipeline.Artifact()
        build_output = codepipeline.Artifact()

        # CodeBuild project
        build_project = codebuild.PipelineProject(self, "MyBuildProject")

        # CodePipeline definition
        pipeline = codepipeline.Pipeline(self, "MyPipeline",
            artifact_bucket=artifact_bucket,
            pipeline_name="MySamplePipeline"
        )

        # Source stage (from GitHub)
        pipeline.add_stage(
            stage_name="Source",
            actions=[
                cpactions.GitHubSourceAction(
                    action_name="GitHub_Source",
                    owner="my-github-user",
                    repo="my-repo",
                    branch="main",
                    oauth_token=SecretValue.secrets_manager("my-github-token"),
                    output=source_output
                )
            ]
        )

        # Build stage
        pipeline.add_stage(
            stage_name="Build",
            actions=[
                cpactions.CodeBuildAction(
                    action_name="CodeBuild",
                    project=build_project,
                    input=source_output,
                    outputs=[build_output]
                )
            ]
        )
