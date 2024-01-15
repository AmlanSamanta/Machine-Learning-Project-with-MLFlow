# MLOps-Project-with-MLFlow-Github-Actions-AWS



## Workflow

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
https://github.com/AmlanSamanta/Machine-Learning-Project-with-MLFlow
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


##### CLI - to fire up mlflow service UI from local 
- mlflow ui

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

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Launch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 992382432296.dkr.ecr.us-east-1.amazonaws.com/mlopsproject

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optional

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    In Github UI, go to setting>actions>runner>new self hosted runner> choose os> then run the mentioned commands one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 992382432296.dkr.ecr.us-east-1.amazonaws.com/mlopsproject

    ECR_REPOSITORY_NAME = mlopsproject




## About MLflow 
MLflow

 - It is Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


