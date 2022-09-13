
# Welcome to the CDK LAMP Stack Project!

## LAMP Stack 

The LAMP Stack is a popular open source solution stack mostly used in web development and in AWS.

LAMP consists of four components. The first letters of the components names make up the LAMP acronym:

* Linux is an operating system used to run the rest of the components.
* Apache HTTP Server is a web server software used to serve static web pages.
* MySQL is a relational database management system used for creating and managing web databases, but also for data warehousing, application logging, e-commerce, etc.
* PHP, Perl, and Python are programming languages are used to create web applications.

Each component represents an essential layer of the stack. Together, the components are used to create database-driven, dynamic websites.

## Overview

We are creating the LAMP stack using CDK Python code which will create the ec2 instance with the proper requirements, the Apache web server, Application load baalncer and the RDS.

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
>> Note : Output will look like

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
8. Create an empty directory on your system:

```
mkdir cdk_workshop && cd cdk_workshop
```
9. Use cdk init to create a new project in Python

```
cdk init sample-app --language python
```

* The `cdk.json` file tells the CDK Toolkit how to execute your app.

* The `app.py` file includes the migration of your multiple stacks and helps to build your CDK application.

After successfully writing your code you can now synthesize the CloudFormation template by using:

```
cdk synth
```
>> Note: As your code contains multiple CDK stacks ; you will have to specify the stack name after the `cdk synth` command

After synthesizing , you need to bootstrap your code

```
cdk bootstrap
```
>> Note: As your code contains multiple CDK stacks ; you will have to specify the stack name after the `cdk bootstrap` command or else you can write `cdk bootstrap --all`

Deploy your CDK code with

```
cdk deploy
```
>> Note: As your code contains multiple CDK stacks ; you will have to specify the stack name after the `cdk deploy` command or else you can write `cdk deploy --all`


* At last as a output you will receive the LoadBalancer URL to access the application which you have deployed in the stack.

## Conclusion

LAMP Stack will provide you

* Flexibility and secure architecture ,also well-established encryption practices that have been proven in the enterprise.
* LAMP can help you reduce development time. Because LAMP is an open source stack that has been available for more than a decade, there is today a substantial LAMP ecosystem.
* It provides you efficiency.