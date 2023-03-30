from typing import Optional
from . models import Category

async def verify_category_exist(category_id, database) -> Optional[Category]:
    return database.query(Category).filter(Category.id == category_id).first()
