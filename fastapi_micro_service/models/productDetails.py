from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, LONGTEXT

Base = declarative_base()
metadata = Base.metadata


class ProductDetail(Base):
    __tablename__ = 'product_details'

    id = Column(BIGINT(20), primary_key=True)
    short_description = Column(LONGTEXT, nullable=False)
    description = Column(LONGTEXT)
    created_at = Column(TIMESTAMP)

    def __init__(self , short_description ,description, created_at ):
        self.short_description = short_description
        self.description = description
        self.created_at = created_at

