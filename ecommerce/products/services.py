from typing import List, Optional
from fastapi import HTTPException, status
from . import models

async def create_new_category(request, database):
    new_category = models.Category(name=request.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category


async def get_all_categories(database) -> List[models.Category]:
    categories = database.query(models.Category).all()
    return categories


async def get_category_by_id(id, database) -> Optional[models.Category]:
    category = database.query(models.Category).get(id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="category not found")

    return category


async def delete_category_by_id(id, database):
    database.query(models.Category).filter(models.Category.id == id).delete()
    database.commit()


async def create_new_product(request, database):
    new_product = models.Product(name=request.name,
                                 quantity=request.quantity,
                                 description=request.description,
                                 price=request.price,
                                 category_id=request.category_id)

    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


async def get_all_products(database) -> List[models.Product]:
    products = database.query(models.Product).all()
    return products