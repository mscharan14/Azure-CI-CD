# Azure DevOps CI/CD Pipeline using Jenkins, AKS, Helm & Docker
A complete end-to-end DevOps project implementing CI/CD on Azure using Jenkins, AKS, ACR, Helm, and Docker.  
This repository is structured, production-style, and recruiter-friendly.

---

## 📌 Overview

This project builds a fully automated CI/CD pipeline using:

- **Azure Kubernetes Service (AKS)** for container orchestration  
- **Jenkins** inside AKS for CI/CD automation  
- **Azure Container Registry (ACR)** for image storage  
- **Docker** for containerization  
- **Helm** for Kubernetes deployment  
- **Python Flask Todo App** as the microservice application  

The pipeline:

1. Builds Docker image  
2. Pushes image to ACR  
3. Updates Helm chart  
4. Deploys application automatically to AKS  

---

## 🧩 Architecture

## Setup Steps

1. **Create Azure Resource Group**

az group create -n <RG_NAME> -l <LOCATION>

markdown
Copy code

2. **Create Azure Container Registry (ACR)**

az acr create -g <RG_NAME> -n <ACR_NAME> --sku Basic --admin-enabled false

markdown
Copy code

3. **Create AKS Cluster**

az aks create
--resource-group <RG_NAME>
--name <AKS_NAME>
--node-count 1
--node-vm-size Standard_B2s
--enable-managed-identity
--generate-ssh-keys

markdown
Copy code

4. **Connect kubectl to AKS**

az aks get-credentials -g <RG_NAME> -n <AKS_NAME>

markdown
Copy code

5. **Install Jenkins using Helm**

helm repo add jenkinsci https://charts.jenkins.io
helm repo update
kubectl create namespace jenkins

helm install jenkins jenkinsci/jenkins -n jenkins
--set controller.serviceType=LoadBalancer
--set persistence.enabled=false
--set controller.resources.requests.cpu=100m
--set controller.resources.requests.memory=256Mi
--set controller.resources.limits.cpu=500m
--set controller.resources.limits.memory=512Mi

markdown
Copy code

6. **Retrieve Jenkins admin password**

kubectl exec -it -n jenkins jenkins-0 -- cat /run/secrets/chart-admin-password

markdown
Copy code

7. **Get Jenkins Load Balancer URL**

kubectl get svc -n jenkins

markdown
Copy code

Open the external IP in a browser to access Jenkins.

8. **Configure Jenkins Pipeline**

- Install required plugins (Git, Docker Pipeline, GitHub Branch Source, Credentials Binding, Pipeline)
- Add GitHub PAT credentials (`git-creds`)
- Add Azure SP JSON credentials (`AZURE_AUTH`)
- Create a **Multibranch Pipeline**
- Set repository URL and Jenkinsfile path:
  ```
  jenkins/Jenkinsfile
  ```
- Add GitHub Webhook:
  ```
  https://<jenkins-url>/github-webhook/
  ```

9. **Trigger CI/CD**

Jenkins will automatically:
- Checkout code
- Build container image using ACR:
  ```
  az acr build
  ```
- Update Helm chart with new image tag
- Deploy updated application to AKS

10. **Access Your Application**

 ```
 kubectl get svc
 ```

 Open the external IP of your application service in a browser.

11. **Delete All Azure Resources (Prevent Billing)**

 ```
 az group delete -n <RG_NAME> --yes --force-deletion
 ```

---

## Skills Demonstrated

This project demonstrates practical hands-on skills across Azure, Kubernetes, and DevOps:

- **Azure Kubernetes Service (AKS)** – Managed Kubernetes cluster setup and deployment  
- **Azure Container Registry (ACR)** – Secure image building using `az acr build`  
- **Kubernetes** – Deployments, Services, Namespaces, and Helm charts  
- **Jenkins CI/CD** – Multibranch pipeline, GitHub webhooks, automated deployments  
- **Service Principal Authentication** – Secure login from Jenkins to Azure  
- **Helm** – Environment-driven deployments and image versioning  
- **Troubleshooting** – Pod logs, events, Jenkins console debugging  
- **Git & Automation** – Clean repo structure, auto-commit pipelines  

