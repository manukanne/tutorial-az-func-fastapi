# Tutorial: Azure Function with FastAPI
This project is a demonstration of how Azure Functions can be used in combination with FastAPI.

## Description
Demo API with the following endpoints:

- Product
    - Create
    - Read all products
    - Read a specific product
    - Patch product data
    - Delete a product

It should be noted that this is only a demo API. This API does not use a real database and therefore only uses a very simplified database manager with an "InMemory" database.

# Getting started
## Prerequisites
- Install the [Azure Function Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash#install-the-azure-functions-core-tools)
- Python 3.9.0
- Azure Subscription (optional)

After that, create  a python virtual environment, activate it and install the requirements.



## Start the function 
```
func start --python
```

> In order to start the Azure Function via the Azure Function Core Tools (CLI) a activated virtual environment is required.

After starting Azure Functions you can access the documentation via this link:
```
http://localhost:7071/docs
```

## Deploy to Azure:
> This step requires an Azure Account. In case you do not have an Azure Account you can go ahead and create an account for free [here](https://azure.microsoft.com/en-us/free/).

Deploy ARM template to a existing resource group:
```
az deployment group create --resource-group <resource-group> --template-file .\az-func-template.json --parameters appName='<your_app_name>' storageAcctName='<your_storage_account_name>' hostingPlanName='<your_hosting_plan_name>'

func azure functionapp publish <your_function_app_name>
```

The original ARM template can be obtained from this [blog](https://benalexkeen.com/automated-deployment-of-serverless-python-web-apis-using-azure-functions-and-azure-devops/) by Ben Keen.

You can also skip the "az deployment group create" command and create the function directly from here:

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fazure-quickstart-templates%2Fmaster%2Fquickstarts%2Fmicrosoft.storage%2Fstorage-account-create%2Fazuredeploy.json" target="_blank">
  <img src="https://aka.ms/deploytoazurebutton"/>
</a>