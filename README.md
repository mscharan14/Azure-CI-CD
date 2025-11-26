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

