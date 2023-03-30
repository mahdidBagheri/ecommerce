from sqlalchemy import String, Column, Integer, VARCHAR
from sqlalchemy.orm import relationship
from ecommerce.db import Base
from ecommerce.user import hashing



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50))
    email = Column(VARCHAR(255), unique=True)
    password = Column(VARCHAR(255))
    cart = relationship("Cart", back_populates="user_cart")

    def __init__(self, name, email, password, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = hashing.get_password_hasing(password)

    def ckeck_password(self, password):
        return hashing.verify_password(self.password, password)