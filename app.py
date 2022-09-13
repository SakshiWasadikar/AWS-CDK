#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import App, Environment

from cdk_workshop.cdk_workshop_stack import CdkLampStack

from cdk_workshop.networking_stack import NetworkingStack

from cdk_workshop.waf_regional import WafRegionalStack
app = cdk.App()


stack1 = NetworkingStack(app, "NetworkingStack",
        env=cdk.Environment(account="298401204930", region="us-east-1"))

stack2 = CdkLampStack(app, "cdk-workshop", vpc=stack1.vpc,
        env=cdk.Environment(account="298401204930", region="us-east-1"))


app.synth()
