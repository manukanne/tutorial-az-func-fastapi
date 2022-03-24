from abc import ABC, abstractmethod
from typing import Optional, List

import schemas


class DatabaseManagerBase(ABC):
    """
    Example implementation of a database manager.
    In a productive application, SQLAlchemy or another ORM framework could be used here (depending on the database used). 
    This is a very simplified database manager for demonstration purposes.
    """

    @abstractmethod
    def add_product(self, product: schemas.ProductCreate) -> schemas.Product:
        """
        Adds a product to the database
        Args:
            product (schemas.ProductCreate): Product to be added

        Returns:
            schemas.Product: Inserted product
        """
        ...

    @abstractmethod
    def get_products(self) -> Optional[List[schemas.Product]]:
        """
        Returns all products from the database
        Returns:
            Optional[List[schemas.Product]]: List of products
        """
        ...

    @abstractmethod
    def get_product(self, id: int) -> Optional[schemas.Product]:
        """
        Returns a specific product by id
        Args:
            id (int): Id of the product

        Returns:
            Optional[schemas.Product]: Returns the specified product
        """
        ...

    @abstractmethod
    def update_product(self, product_id: int, product: schemas.ProductPartialUpdate) -> schemas.Product:
        """
        Updates a product
        Args:
            product_id (int): Product ID of the product to be updated
            product (schemas.Product): Product to update

        Returns:
            schemas.Product: Updated product
        """
        ...

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        """
        Deletes a product by id
        Args:
            id (int): Id of the to be deleted product
        """
        ...


class FakeDataBaseManager(DatabaseManagerBase):

    def __init__(self) -> None:
        super().__init__()

        self._products = [
            schemas.Product(
                id=1,
                title="Product 1",
                description="Desc 1",
                purch_price=10,
                sales_price=20
            ),
            schemas.Product(
                id=2,
                title="Product 2",
                description="Desc 2",
                purch_price=20,
                sales_price=30
            ),
            schemas.Product(
                id=3,
                title="Product 3",
                description="Desc 3",
                purch_price=40,
                sales_price=65
            )
        ]

    def add_product(self, product: schemas.ProductCreate) -> schemas.Product:
        # Normally, this step would be handled by the database
        idx = max([p.id for p in self._products]) + 1

        product_insert = schemas.Product(id=idx, **product.dict())
        self._products.append(product_insert)

        return product_insert

    def get_products(self) -> Optional[List[schemas.Product]]:
        return self._products

    def get_product(self, id: int) -> Optional[schemas.Product]:
        return next(iter([p for p in self._products if p.id == id]), None)

    def update_product(self, product_id: int, product: schemas.ProductPartialUpdate) -> schemas.Product:
        for idx, p in enumerate(self._products):
            if p.id == product_id:
                db_product = self._products[idx]
                update_data = product.dict(exclude_unset=True)
                updated_product = db_product.copy(update=update_data)
                self._products[idx] = updated_product
                return updated_product
        return None
    
    def delete_product(self, product_id: int) -> None:
        for p in self._products:
            if p.id == product_id:
                product_del = p
                break
        
        if product_del:
            self._products.remove(product_del)
