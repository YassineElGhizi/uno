from sqlalchemy import Column, DECIMAL, TIMESTAMP, Text
from sqlalchemy.dialects.mysql import BIGINT, LONGTEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class ProductStore(Base):
    __tablename__ = 'product__stores'

    id = Column(BIGINT(20), primary_key=True)
    id_product = Column(BIGINT(20), nullable=False)
    store = Column(BIGINT(20), nullable=False)
    title = Column(Text(collation='utf8mb4_unicode_ci'))
    price = Column(DECIMAL(8, 2), nullable=False)
    link = Column(LONGTEXT, nullable=False)
    created_at = Column(TIMESTAMP)

    def __init__(self, id_product,store,title,price,link,created_at):
        self.id_product = id_product
        self.store = store
        self.title = title
        self.price = price
        self.link = link
        self.created_at = created_at


