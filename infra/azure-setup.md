# Azure setup log
Run date: <fill after running azure commands>

This file will contain the exact Azure CLI commands run and their output (redact secrets before committing).
Variables used:
$PREFIX = "srchan"
$RG = "${PREFIX}-rg"
$LOCATION = "eastus"
$ACR_NAME = "${PREFIX}acr01"    # adding 01 to guarantee unique name
$AKS_NAME = "${PREFIX}-aks"


---
# Resource group created

{
  "id": "/subscriptions/a3c751c7-e5ae-4625-8f30-2398d722fd10/resourceGroups/srchan-rg",
  "location": "eastus",
  "managedBy": null,
  "name": "srchan-rg",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": "Microsoft.Resources/resourceGroups"
}

---
# ACR created
Login server: 

