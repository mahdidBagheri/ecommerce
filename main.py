from fastapi import FastAPI
import numpy as np
from ecommerce.user import router as user_router
from ecommerce.products import router as product_router
app = FastAPI(title= "ecommerce",
              description= "this is private doc",
              version= "1.0")

app.include_router(user_router.router)
app.include_router(product_router.router)

