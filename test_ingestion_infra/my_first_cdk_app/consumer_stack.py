from aws_cdk import Stack
from constructs import Construct
from aws_cdk import Fn

class ConsumerStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Import the bucket name exported by the Producer stack
        shared_bucket_name = Fn.import_value("SharedBucketName")

        # Now you can use shared_bucket_name inside this stack!
        # Example: Just print it
        print(f"Imported bucket name: {shared_bucket_name}")
