# Azure CI/CD (Jenkins + Argo CD + Helm)

This repository contains a Todo app (Flask) and infra/pipeline artifacts prepared for deploying to Azure AKS via Jenkins CI and Argo CD GitOps.

Folders:
- `app/` - Flask app
- `docker/` - Dockerfile
- `helm/todo-chart/` - Helm chart for deployment
- `jenkins/` - Jenkinsfile (CI pipeline)
- `argocd/` - Argo CD application manifest (CD)
- `infra/` - infra setup logs & cleanup commands

## Quick local run
1. Create venv: `python3 -m venv venv && . venv/bin/activate`
2. `pip install -r requirements.txt`
3. `pytest` to run tests
4. `docker build -t local/flask-todo -f docker/Dockerfile .`
5. `docker run --rm -p 8000:8000 local/flask-todo` and visit `http://localhost:8000`

## Next steps to deploy to Azure
See `infra/azure-setup.md` for step-by-step Azure CLI commands to create ACR, AKS, install Argo CD and Jenkins, and push images.
