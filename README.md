
# Welcome to CDK Python CI Pipeline Project

This guide demonstrates a CDK app with an instance of a stack (`cdk_workshop_stack`)
which contains Codepipeline , Codecommit and Codebuild to create your CI/CD Pipeline.

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


Create an empty directory on your system:

```
mkdir cdk_workshop && cd cdk_workshop
```
Use cdk init to create a new project in Python

```
cdk init sample-app --language python
```

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## To build your CI Pipeline :

1. Create a Codepipeline first. 

>> *Codepipeline* : CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define. This enables you to rapidly and reliably deliver features and updates.



2. You will need to setup your *Codecommit* repository to build your code for CI pipeline. You can use Amazon ECR or your another version control systems such as GitHub and BitBucket.

>> *Codecommit* : CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories. CodeCommit eliminates the need for you to manage your own source control system or worry about scaling its infrastructure. You can use CodeCommit to store anything from code to binaries.


3. In your repository you have to pass the **buildspec.yal** file which is a collection of build commands and related settings, in YAML format, that CodeBuild uses to run a build.

4. In the last stage when the source is created we have to build the pipeline using Codebuild in the refrence of *buildspec.yml* file 

>> *Codebuild* : AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. 

After successfully writing your code you can now synthesize the CloudFormation template by using:

```
cdk synth
```

After synthesizing , you need to bootstrap your code

```
cdk bootstrap
```

Deploy your CDK code with

```
cdk deploy
```

## Troubleshooting

1. While passig the parameters in buildspec.yml file make sure to mention the correct extension to the file as "yml" instead of "yaml".

2. User must have required IAM permissions to build the code to create the pipeline. Pass the (AmazonEC2ContainerRegistryFullAccess) permission to your IAM user.


## Conclusion

1. A pipeline defines your release process workflow, and describes how a new code change progresses through your release process.

2. AWS CodePipeline can pull source code for your pipeline directly from AWS CodeCommit, GitHub, Amazon ECR, or Amazon S3. It can run builds and unit tests in AWS CodeBuild. 

3. AWS CodePipeline uses AWS IAM to manage who can make changes to your release workflow, as well as who can control it. You can grant users access through IAM users, IAM roles, and SAML-integrated directories.
