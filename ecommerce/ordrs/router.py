from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ecommerce import db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from . import schema
from . import services

router = APIRouter(tags=['Orders'], prefix='/orders')

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.ShowOrder)
async def initialize_order_processing(database: Session = Depends(db.get_db)):
    result = await services.initiate_order(database)
    return result

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schema.ShowOrder])
async def order_list(database: Session = Depends(db.get_db)):
    result = await services.get_order_listing(database)
    return result
