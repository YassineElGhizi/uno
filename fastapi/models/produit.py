from sqlalchemy import Column, Integer, String
from sqlalchemy.ext import declarative
from sqlalchemy.dialects import mysql


base = declarative.base()

class products(base):
    __tablename__ = 'products'

    id = Column('id' , Integer , primary_key=True)
    name = Column('name' ,mysql.VARCHAR(length=255))
    title = Column('title' , mysql.TEXT)
    slug =Column('slug' , mysql.TEXT)
    best_price = Column('best_price' ,mysql.DECIMAL)
    brand = Column('brand' , mysql.DECIMAL)
    category = Column('category' , mysql.BIGINT)
    product_details = Column('product_details', mysql.BIGINT)
    images = Column('images' , mysql.TEXT)
    id_parent = Column('id_parent' , mysql.TEXT)

