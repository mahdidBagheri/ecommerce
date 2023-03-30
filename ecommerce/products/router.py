from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from ecommerce import db
from . import schema
from . import services
from . import validator

router = APIRouter(tags=["Products"], prefix='/products')

@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: schema.Category, database: Session = Depends(db.get_db)):
    return await services.create_new_category(request, database)

@router.get('/category', response_model=List[schema.ListCategory])
async def get_all_categories(database: Session = Depends(db.get_db)):
    categories = await services.get_all_categories(database)
    return categories

@router.get('/category/{id}', response_model=schema.DisplayCategory)
async def get_category_by_id(id:int, database: Session = Depends(db.get_db)):
    category = await services.get_category_by_id(id, database)
    return category

@router.delete('/category/{id}', status_code=status.HTTP_204_NO_CONTENT, response_class= Response)
async def delete_category_by_id(id: int, database: Session = Depends(db.get_db)):
    return await services.delete_category_by_id(id, database)