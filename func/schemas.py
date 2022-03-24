from pydantic import BaseModel, validator
from typing import Optional

"""
Contains all schemas alias domain models of the application.
For domain modelling, the library pydantic is used.
Pydantic allows to create versatile domain models and ensures data integrity and much more.
"""


class ProductBase(BaseModel):
    """
    Product base schema
    """
    title: Optional[str] = None
    description: Optional[str] = None
    purch_price: Optional[float] = None
    sales_price: Optional[float] = None

    class Config:
        fields = {
            "title": {"description": "Product name"},
            "description": {"description": "Product description"},
            "purch_price": {"description": "Purchase price of the product"},
            "sales_price": {"description": "Sales price of the product"}
        }


class ProductCreate(ProductBase):
    """
    Product create schema
    """
    title: str
    description: str
    purch_price: float
    sales_price: float


class ProductPartialUpdate(ProductBase):
    """
    Product update schema
    """
    ...


class Product(ProductBase):
    """
    Product schema, database representation
    """
    id: int

    class Config:
        fields = {
            "id": {"description": "Unique ID of the product"},
        }
