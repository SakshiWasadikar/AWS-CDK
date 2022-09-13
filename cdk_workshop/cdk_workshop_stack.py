from multiprocessing import connection
from os import path
import secrets
from aws_cdk.aws_ecr_assets import DockerImageAsset, NetworkMode
from constructs import Construct
from aws_cdk import (
    Arn,
    Duration,
    Stack,
    SecretValue,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_ec2 as ec2,
    aws_codepipeline as codepipeline,
    aws_codecommit as codecommit,
    aws_codebuild as codebuild,
    aws_codedeploy as codedeploy,
    aws_codedeploy as ServerDeploymentGroupAttributes,
    aws_codepipeline as ShellStep,
    aws_codepipeline_actions as codepipeline_actions
    
)


class CdkWorkshopStack(Stack):  

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        git_hub_source = codebuild.Source.git_hub(
            owner="awslabs",
            repo="aws-cdk",
            webhook=True,  
            webhook_triggers_batch_build=True, 
            webhook_filters=[
                  codebuild.FilterGroup.in_event_of(codebuild.EventAction.PUSH).and_branch_is("master").and_commit_message_is("the commit message")
    ]
)
          
        repository = codecommit.Repository(self, "Ecs_pipeline_repo123",
          repository_name="Ecs_pipeline_repo123"
       )
        
        project = codebuild.PipelineProject(self, "AWS-Pipeline") 

        source_output = codepipeline.Artifact()
        source_action = codepipeline_actions.CodeCommitSourceAction(
            action_name="CodeCommit",
            repository=repository,
            output=source_output    
        )
 

        build_action = codepipeline_actions.CodeBuildAction(
             action_name="CodeBuild",
             project=project,
             input=source_output,
             outputs=[codepipeline.Artifact()], 
             execute_batch_build=False,  
             combine_batch_build_artifacts=True)

        codepipeline.Pipeline(self, "CDK-Pipeline",
            stages=[codepipeline.StageProps(
                stage_name="Source",
                actions=[source_action]
            ), codepipeline.StageProps(
                stage_name="Build",
                actions=[build_action]
             )
             ]
        )
        application = codedeploy.ServerApplication(self, "CodeDeployApplication",
            application_name="MyApplication"
        )


































