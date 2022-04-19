from sqlalchemy import Column, DateTime, Float, PrimaryKeyConstraint, DECIMAL
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
import pymysql


Base = declarative_base()
metadata = Base.metadata

class PriceHistory(Base):
    __tablename__ = 'price_histories'

    id = Column(BIGINT(20), primary_key=True)
    id_product = Column(BIGINT(20), nullable=False)
    average = Column(DECIMAL(8, 2), nullable=False)
    best_price = Column(DECIMAL(8, 2), nullable=False)


    def __init__(self, id_product,Average,Best_price):
        self.id_product = id_product
        self.average = Average
        self.best_price = Best_price
