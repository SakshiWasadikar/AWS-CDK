import imp
from inspect import stack
from main import *
import os
import yaml
import sys
from constructs import Construct
from aws_cdk import (
    App, Stack, Aws, CfnOutput, Tags, Fn,
    aws_elasticloadbalancingv2 as elbv2,
    aws_autoscaling as autoscaling,
    aws_wafv2 as wafv2,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_rds as rds,
    aws_ec2 as vpc,
    CfnOutput, Stack, Tags
)


sys.path.append(os.path.abspath(os.curdir))

with open("/home/sakshiwasadikar/cdk_workshop/user_data/user_data.sh") as f:
    user_data = f.read()


class CdkLampStack(Stack):

    def __init__(self, scope: Construct,  construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
                


        sec_group = ec2.SecurityGroup(
            self,
            "sec-group-allow-ssh",
            vpc=vpc,
            allow_all_outbound=True,
        )

        sec_group.add_ingress_rule(
            peer=ec2.Peer.ipv4('10.0.0.0/16'),
            description="Allow SSH connection", 
            connection=ec2.Port.tcp(22))

        ec2_instance = ec2.Instance(
            self,
            "ec2-instance",
            instance_name=instance_name,
            instance_type=ec2.InstanceType(instance_type),
            machine_image=ec2.MachineImage().lookup(name=machine_image),
            vpc=vpc,
            security_group=sec_group,)
 

        role = iam.Role(self, "InstanceSSM",
		                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name(
		    "AmazonSSMManagedInstanceCore"))


        alb = elbv2.ApplicationLoadBalancer(
            self, "lampALB", vpc=vpc, internet_facing=True,)

        alb.set_attribute(
            key="routing.http.drop_invalid_header_fields.enabled", value="true")

        http_listener = alb.add_listener("ALBListenerHttps", port=80,  protocol=elbv2.ApplicationProtocol.HTTP)
        http_listener.add_targets("Target", port=80)

        http_listener.connections.allow_default_port_from_any_ipv4(
            "Hello, Good Evening to you!!")


     

        CfnOutput(self, "LoadBalancer", export_name="LoadBalancer",
                  value=alb.load_balancer_dns_name)


        RDS = rds.DatabaseInstance(self, "MySQL8",
                                         engine=rds.DatabaseInstanceEngine.mysql(
                                             version=rds.MysqlEngineVersion.VER_8_0_21
                                         ),
                                         instance_type=ec2.InstanceType("m5.4xlarge"),
                                         vpc=vpc,
                                         multi_az=False,
                                         publicly_accessible=True,
                                         allocated_storage=100,
                                         storage_type=rds.StorageType.GP2,
                                         cloudwatch_logs_exports=["error", "general", "slowquery"],
                                         deletion_protection=True,
                                         enable_performance_insights=True,
                                         delete_automated_backups=True,
                                         parameter_group=rds.ParameterGroup.from_parameter_group_name(
                                             self, "para-group-mysql",
                                             parameter_group_name="default.mysql8.0"
                                         )
                                         )
