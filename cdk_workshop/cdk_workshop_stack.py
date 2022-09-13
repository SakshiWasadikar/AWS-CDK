from xml.etree.ElementInclude import include
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3_deploy,
    aws_s3  as s3_assets
    

)

class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self,"sakshibucket", public_read_access=True, website_index_document="index.png",)
        
        s3_deploy.BucketDeployment(self, "deploywebsite",
          
        
            sources=[s3_deploy.Source.asset("./web")],
            destination_bucket=bucket,
            
        )
       