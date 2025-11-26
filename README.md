Azure CI/CD Pipeline with Jenkins, AKS, ACR & Helm
Overview

This project demonstrates a complete CI/CD pipeline on Microsoft Azure, integrating:

Jenkins for Continuous Integration

Azure Container Registry (ACR) for container image storage

Azure Kubernetes Service (AKS) for application deployment

Helm for Kubernetes packaging and upgrades

GitHub for version control and webhook triggers

The pipeline automatically builds, tests, containerizes, pushes, and deploys a Flask-based TODO API onto AKS.

This repository is designed to be easy to follow for beginners yet professional for interviews and recruiters.

Architecture
GitHub → Jenkins → ACR → AKS (via Helm)
         ↑
       Webhook

Workflow

Code pushed to GitHub triggers Jenkins.

Jenkins runs unit tests using Pytest.

Jenkins builds a Docker image and pushes to ACR.

Helm automatically updates the image tag.

Helm upgrades the app release in AKS.

AKS serves the new version.

Repository Structure
.
├── app/
│   ├── app.py
│   ├── __init__.py
│   └── requirements.txt
│
├── tests/
│   └── test_api.py
│
├── docker/
│   └── Dockerfile
│
├── helm/
│   └── todo-app/
│       ├── templates/
│       ├── Chart.yaml
│       └── values.yaml
│
├── infra/
│   ├── rg-create.json
│   ├── acr-create.json
│   ├── aks-create.json
│   └── azure-setup.md
│
├── jenkins/
│   └── Jenkinsfile
│
└── README.md

Prerequisites
Local

VS Code

Git

Docker Desktop

Azure CLI

kubectl

Helm

Cloud

Azure free tier account

ACR registry

AKS cluster

Jenkins running on AKS

Setup Steps
1. Create Resource Group
az group create --name <rg-name> --location <region>

2. Create Azure Container Registry (ACR)
az acr create \
  --resource-group <rg-name> \
  --name <acr-name> \
  --sku Basic


Get login server:

az acr show -n <acr-name> --query loginServer -o tsv

3. Create AKS Cluster
az aks create \
  --resource-group <rg-name> \
  --name <aks-name> \
  --node-count 1 \
  --enable-managed-identity \
  --generate-ssh-keys


Connect:

az aks get-credentials -g <rg-name> -n <aks-name>

4. Install Jenkins on AKS (via Helm)

Create namespace:

kubectl create namespace jenkins


Add chart & install:

helm repo add jenkinsci https://charts.jenkins.io
helm repo update

helm install jenkins jenkinsci/jenkins -n jenkins \
  --set controller.serviceType=ClusterIP \
  --set persistence.enabled=false \
  --set controller.admin.username=admin \
  --set controller.admin.password="ChangeMe123!"


Port-forward to access Jenkins:

kubectl port-forward svc/jenkins -n jenkins 8080:8080


Visit:

👉 http://localhost:8080

5. Configure Jenkins Credentials
Add three credentials:
ID	Type	Description
git-creds	GitHub PAT	Pull/push access
acr-creds	Username + password	Push images to ACR
azure-sp	Service principal	az login inside Jenkins
6. Create Jenkins Multibranch Pipeline

Jenkins → New Item

Select Multibranch Pipeline

Add repo URL

Add git-creds

Jenkins automatically detects:

jenkins/Jenkinsfile


This triggers the CI/CD flow.

7. First Deployment to AKS
helm upgrade --install todo-app ./helm/todo-app \
  --set image.repository=<acr-login-server>/todo \
  --set image.tag=<version>


Verify:

kubectl get pods
kubectl get svc
kubectl get deploy

8. Accessing the App

If using LoadBalancer:

kubectl get svc todo-app


Open the EXTERNAL-IP in your browser.

9. Cleanup (To Avoid Billing)
az group delete --name <rg-name> --yes --no-wait


This deletes:

AKS

ACR

Jenkins

Load Balancers

Public IPs

✔️ Completely stops billing.

Challenges & How We Solved Them
1. Jenkins Init Container OutOfMemoryError

Jenkins plugin download exceeded memory
✔️ Reduced plugin list & reinstalled chart with lighter config

2. ACR Not Registered in Subscription

Error: MissingSubscriptionRegistration
✔️ Ran:

az provider register --namespace Microsoft.ContainerRegistry

3. AKS Free-Tier VM Size Not Allowed

Standard_B2s rejected by region
✔️ Used recommended VM sizes from error output

4. Jenkins Docker Agent Not Supported

agent { docker { ... } } not allowed in Kubernetes Jenkins
✔️ Removed Docker agents and used ACR Build instead

5. Azure CLI Not Found in Jenkins Pod

✔️ Used Service Principal JSON with az login --service-principal --sdk-auth

6. GitHub Scan Errors

✔️ Added GitHub PAT credential (git-creds) → fixed instantly

Skills Demonstrated

Azure AKS, ACR, Resource Groups

Jenkins Multibranch Pipelines

CI/CD pipeline design

Helm chart creation

Docker image build & push

Kubernetes deployments, services

GitHub automation

Service Principals & IAM

Debugging production-style issues


Conclusion

This repository provides a complete CI/CD pipeline running on Azure with Jenkins and AKS.
It is ideal for:

DevOps interviews

Cloud engineer portfolio

Learning Kubernetes + Jenkins automation

Demonstrating real-world AZURE DevOps workflow