from sqlalchemy import Numeric, Table, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


# Многие ко многим
product_category = Table('product_category', Base.metadata,
                         Column('product_id', ForeignKey('products.id'), primary_key=True),
                         Column('category_id', ForeignKey('categories.id'), primary_key=True)
                         )

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    description = Column(String(255), nullable=True)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key = True)
    name = Column(String(255), unique = True)
    img = Column(String(255), nullable=True)

    categories = relationship("Category", secondary="product_category", backref="products")

    
class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key = True)
    name = Column(String(255), unique = True)
    description = Column(String(255), unique = False)
    rating = Column(Integer, unique = False)