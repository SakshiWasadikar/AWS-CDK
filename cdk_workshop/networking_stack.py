from ipaddress import IPv4Address
from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
import yaml
from constructs import Construct
with open('/home/sakshiwasadikar/cdk_workshop/Networking/networking/network.yaml', 'r') as net:
    net_config = yaml.load(net, Loader=yaml.FullLoader)


class NetworkingStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
 
        self.vpc = ec2.Vpc(self, "TheVPC",
                      cidr=net_config['dev']['vpc_cidr'],
                      vpc_name=net_config['dev']['env_name'] + '-vpc',
                      nat_gateways=1,
                      max_azs=2,
                      subnet_configuration=[
                          ec2.SubnetConfiguration(
                            name="Public",
                            subnet_type=ec2.SubnetType.PUBLIC,
                            cidr_mask=24
                          ),
                          ec2.SubnetConfiguration(
                              name="Private",
                              subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                              cidr_mask=24
                          )
                      ],
                      )
        network_acl = ec2.NetworkAcl(self, "PublicSubnetACL",
                                     vpc=self.vpc,

                                     network_acl_name=net_config['dev']['env_name'] + '-nacl',
                                     subnet_selection=ec2.SubnetSelection(

                                         subnet_type=ec2.SubnetType.PUBLIC
                                     )
                                     )

        network_acl_entry = ec2.NetworkAclEntry(self, "PublicACLEntry", cidr=ec2.AclCidr.any_ipv4(),
                                               rule_number=100,
                                               traffic=ec2.AclTraffic.all_traffic(),
                                               direction=ec2.TrafficDirection.EGRESS,
                                               rule_action=ec2.Action.ALLOW,
                                               network_acl=network_acl
                                               
                                               
                                               )
