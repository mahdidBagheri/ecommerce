from sqlalchemy import String, Column, Integer, VARCHAR, Text, Float, ForeignKey
from ecommerce.db import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50))
    product = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50))
    quantity = Column(Integer)
    description = Column(Text)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"))
    category = relationship("Category", back_populates="product")
    cart_items = relationship("CartItems", back_populates="products")
    order_details = relationship("OrderDetails", back_populates="product_order_details")


