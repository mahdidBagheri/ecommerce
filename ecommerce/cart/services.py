from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.products.models import Product
from ecommerce.user.models import User
from . models import Cart, CartItems
from . import schema

async def add_item(cart_id, product_id, database):
    cart_items = CartItems(cart_id=cart_id, product_id=product_id)
    database.add(cart_items)
    database.commit()
    database.refresh(cart_items)


async def add_to_cart(product_id, database):
    product_info = database.query(Product).get(product_id)
    if not product_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no product by id \"{product_id}\"")
    if product_info.quantity <= 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item out of stock")


    user_info = database.query(User).filter(User.email == "zahra@example.com").first()

    cart_info = database.query(Cart).filter(Cart.user_id == user_info.id).first()

    if not cart_info:
        new_cart = Cart(user_id=user_info.id)
        database.add(new_cart)
        database.commit()
        database.refresh(new_cart)
        await add_item(new_cart.id, product_info.id, database)
    else:
        await add_item(cart_info.id, product_info.id, database)
    return {"stats" : "item added"}


async def get_all_items(database) -> schema.ShowCart:
    user_info = database.query(User).filter(User.email == "zahra@example.com").first()
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()
    return cart


async def delete_item_by_id(id, database) -> None:
    user_info = database.query(User).filter(User.email == "zahra@example.com").first()
    cart_id = database.query(Cart).filter(User.id == user_info.id).first()
    database.query(CartItems).filter(CartItems.id == id, CartItems.cart_id == cart_id.id).delete()
    database.commit()
    return