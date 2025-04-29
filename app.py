import aws_cdk as cdk

from test_ingestion_infra.my_first_cdk_app.producer_stack import ProducerStack
from test_ingestion_infra.my_first_cdk_app.consumer_stack import ConsumerStack

app = cdk.App()
producer =  ProducerStack(app, "ProducerStack", env=cdk.Environment(account="211125525499", region="eu-west-2"))
consumer = ConsumerStack(app, "ConsumerStack", env=cdk.Environment(account="211125525499", region="eu-west-2"))

app.synth()