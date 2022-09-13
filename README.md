
# Welcome to the CDK Python project!

The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework to define your cloud application resources using familiar programming languages.

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (**`cdk_workshop_stack`**) which contains an Amazon S3 Bucket with objects inside it.

## Prerequisite 

1. To install CDK on your environment:

* First install AWS-Cli in your machine according to the base OS.
* Configure the AWS by mentioning proper access key and access key id.
* Next install the Nodejs and NPM packages with the following commands:

```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
```
2. Once the NodeSource repository is enabled, install Node.js and npm by typing:

```
sudo apt install nodejs
```
3. Verify that the Node.js and npm were successfully installed by printing their versions:

```
nodejs --verison
npm --version
```
4. Install NVM (Node Version Manager) script

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
```
> Note : Output
=> Close and reopen your terminal to start using nvm or run the following to use it now:
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

5. Once the script is in your PATH, verify that nvm was properly installed by typing:

```
nvm --version
```
6. Now that the nvm is installed you can install the latest available version of Node.js, by typing:

```
nvm install node 
```
7. Last install the aws-cdk package to the latest version.

```
npm install -g aws-cdk
```

## Overview

### Steps to create your CDK Python Project

Create an empty directory on your system:

```
mkdir cdk_workshop && cd cdk_workshop
```
Use cdk init to create a new project in Python

```
cdk init sample-app --language python
```

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

You can now write your own code in "cdk_workshop_ stack.py and create your own CloudFormation Template.

After successfully writing your code you can now synthesize the CloudFormation template by using: 

```
$ cdk synth
```
> The cdk synth command executes your app, which causes the resources defined in it to be translated into an AWS CloudFormation template.

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

You can list your stacks in the app by using: 

```
cdk ls
```
After synthesizing , you need to bootstrap your code 

```
cdk bootstrap
```

> CDK bootstrap is a tool in the AWS CDK command-line interface responsible for populating a given environment (that is, a combination of AWS account and region) with resources required by the CDK to perform deployments into that environment.

To deploy your cdk application use the command:

```
cdk deploy
```
> The cdk deploy subcommand deploys the specified stack(s) to your AWS account. 

Last you can aslo check your modified stack with the help of :

```
cdk diff
```

Now you can go the AWS CloudFormation Console and check that your stack has been created by CDK very easily.


## Conclusion

* AWS CDK helps in easier cloud onboarding and cloud infrastructure
* It helps in faster development process 
*  It also provides high-level components that preconfigure cloud resources with proven defaults, helping you build on AWS without needing to be an expert.


