from fastapi import FastAPI
import numpy as np
from ecommerce.user import router as user_router
from ecommerce.products import router as product_router
from ecommerce.cart import router as cart_router
from ecommerce.ordrs import router as order_router
from ecommerce.auth import router as auth_router

app = FastAPI(title= "ecommerce",
              description= "this is private doc",
              version= "1.0")

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)

