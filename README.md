# MLOps-Project-with-MLFlow-Github-Actions-AWS



## Development Workflow

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/AmlanSamanta/Machine-Learning-Project-with-MLFlow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlopsproj python==3.9.6 -y
```

```bash
conda activate mlopsproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

### Now open up you local host and port in browser



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

## About MLflow 
MLflow

 - It is Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

##### CLI - to fire up mlflow service UI from local 
```bash
mlflow ui
```

### dagshub
[dagshub](https://dagshub.com/)

### MLFlow configurations

MLFLOW_TRACKING_URI = https://dagshub.com/Amlan/Machine-Learning-Project-with-MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME = Amlan \
MLFLOW_TRACKING_PASSWORD = 5801675fa3e718edb779ace5947164241bfc2243  \
python script.py

Run these to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Amlan/Machine-Learning-Project-with-MLFlow.mlflow

export MLFLOW_TRACKING_USERNAME=Amlan 

export MLFLOW_TRACKING_PASSWORD=5801675fa3e718edb779ace5947164241bfc2243

```



# AWS-CICD-Deployment-with-Github-Actions

#Description: About the deployment workflow

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Launch your docker image in EC2

## 1. Login to AWS console.

## 2. Create an IAM user with specific access: 

	#Steps

	Type IAM in search bar and go to IAM Dashboard > Access Managament > Users > Create User > Specify Username > Next > Set permissions > Attach policies directly > Choose below mentioned policies from the list > Next > Review and create > Create user (e.g. mlopsProject-user)

	#Policy 

	1. AmazonEC2FullAccess - for EC2 access
	2. AmazonEC2ContainerRegistryFullAccess - for ECR access

	#Post successful creation of new user

	Click on mlopsProject-user > Security credentials > Access keys > Create access key > Access key best practices & alternatives > Use case > Command Line Interface (CLI) > Confirmation > Check the box > Next > Set description tag - optional > Create access key > Retrieve access keys > Download .csv file

## 3. Create ECR repo to store and manage docker image

	#Steps

	Type ECR in search bar and select Elastic Container Registry > Create a repository > Get started > Create repository > Visibility settings > Private > Repository name > (e.g. mlopsproject) > Create repository

    - Save the URI: 992382432296.dkr.ecr.us-east-1.amazonaws.com/mlopsproject

## 4. Create EC2 machine (Ubuntu) 

	#Steps

	Type ec2 in search bar and select EC2 > Launch instance in EC2 Dashboard > Launch instance > Name and tags (e.g. mlopsProject-server) > Application and OS Images (Amazon Machine Image) > Ubuntu > Ubuntu Server 22.04 LTS > Instance type > t2.large > Key pair (login) > Create new key pair > Create key pair > Key pair name (e.g. mlopsProject), Key pair type (e.g. RSA), Private key file format (e.g. .pem) > Create key pair > Network settings (Firewall (security groups) > Create security group > Check all rules) > Configure storage (e.g. 30 gb) > Launch instance > Next Steps > View all instances

	#Post successful creation of server

	Click on Instance ID link of mlopsProject-server > Click Connect

## 5. Install and configure docker in EC2 Machine:
	
	#optional

	```bash
	sudo apt-get update -y

	sudo apt-get upgrade
	```
	
	#required

	```bash
	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	```
	
# 6. Configure self-hosted runner for using with Github Action workflow:

	Basically it would establish a connectivity between your repo and EC2, so that whenever some change happens in repo, it automatically triggers the workflow.

    In Github UI and inside your repo, go to Setting>Code and automation>Actions>Runners>New self-hosted runner> Runners / Add new self-hosted runner · AmlanSamanta/Machine-Learning-Project-with-MLFlow>Runner image(Linux)>Architecture(x64)

	Then run the commands (also mentioned below):

	```bash
	mkdir actions-runner && cd actions-runner
	# Download the latest runner package
	curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz
	# Optional: Validate the hash
	echo "29fc8cf2dab4c195bb147384e7e2c94cfd4d4022c793b346a6175435265aa278  actions-runner-linux-x64-2.311.0.tar.gz" | shasum -a 256 -c
	# Extract the installer
	tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz
	# Configure - Create the runner and start the configuration experience - Provide runner group name: default; runner name: self-hosted; additional label: none; work folder: default value _work
	./config.sh --url https://github.com/AmlanSamanta/Machine-Learning-Project-with-MLFlow --token ABX5PN5KJ7UDNPNDOJZX5EDFVC65K
	./run.sh
	# Using your self-hosted runner - Use this YAML in your workflow file for each job
	runs-on: self-hosted
	```

# 7. Setup github secrets:

	Github Repo sSettings > Security > Secrets and variables > Actions > Actions secrets and variables > New repository secret

    AWS_ACCESS_KEY_ID = <your secret acess key id>

    AWS_SECRET_ACCESS_KEY = <your secret acess key>

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 992382432296.dkr.ecr.us-east-1.amazonaws.com/mlopsproject

    ECR_REPOSITORY_NAME = mlopsproject


