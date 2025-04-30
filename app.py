#!/usr/bin/env python3
import aws_cdk as cdk

from test_ingestion_infra.my_first_cdk_app.producer_stack import ProducerStack
from test_ingestion_infra.my_first_cdk_app.consumer_stack import ConsumerStack
from test_ingestion_infra.pipeline_ci_cd import CdkPipelineStack


app = cdk.App()
# Use this code when loading services manually.
# dev =  ProducerStack(app, "ProducerStack", env=cdk.Environment(account="211125525499", region="eu-west-2"))
# prod = ConsumerStack(app, "ConsumerStack", env=cdk.Environment(account="211125525499", region="eu-west-2"))

CdkPipelineStack(app, "MyPipelineStack", env=cdk.Environment(account="211125525499", region="eu-west-2"))
app.synth()