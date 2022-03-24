from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import azure.functions as func

from routers import products
from utilities.exceptions import ApiException


description = """
This is a sample API based on Azure Functions and FastAPI.

This API is used to illustrate how a potential API with Azure Functions and FastAPI could look like, it is a demo API only.
I hope you like it and help you to build awesome projects based on these great frameworks!

## Products
* Add products
* Retrieve products
* Retrieve a specific product by ID
* Update existing products
* Delete products by ID
"""

app = FastAPI(
    title="Azure Function Demo FastAPI",
    description=description,
    version="0.1",
    contact={
        "name": "Manuel Kanetscheider",
        "url": "https://dev.to/manukanne",
        "email": "me@manuelkanetscheider.net"
    },
    license_info= {
        "name": "MIT License",
        "url": "https://github.com/manukanne/tutorial-az-func-fastapi/blob/main/LICENSE"
    }
)
app.include_router(products.router)
# Add additional api routers here


@app.exception_handler(ApiException)
async def generic_api_exception_handler(request: Request, ex: ApiException):
    """
    Generic API exception handler. 
    Ensures that all thrown excpetions of the custom type API Excpetion are returned 
    in a unified exception JSON format (code and description).    
    Args:
        request (Request): HTTP Request
        ex (ApiException): Thrown exception

    Returns:
        JSONResponse: Returns the exception in JSON format
    """
    return JSONResponse(
        status_code=ex.status_code,
        content={
            "code": ex.code,
            "description": ex.description
        }
    )


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """
    Azure function entry point.
    All web requests are handled by FastAPI.
    Args:
        req (func.HttpRequest): Request
        context (func.Context): Azure Function Context

    Returns:
        func.HttpResponse: HTTP Response
    """
    return func.AsgiMiddleware(app).handle(req, context)
