import aws_cdk as core
import aws_cdk.assertions as assertions

from test_ingestion_infra.test_ingestion_infra_stack import \
    TestIngestionInfraStack


# example tests. To run these tests, uncomment this file along with the example
# resource in test_ingestion_infra/test_ingestion_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestIngestionInfraStack(app, "test-ingestion-infra")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
