from sqlalchemy import Column, DateTime, Float, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
import pymysql


Base = declarative_base()
metadata = Base.metadata

class PriceHistory(Base):
    __tablename__ = 'price_histories'

    id_product = Column('id_product', INTEGER(11), nullable=False, primary_key=True),
    Date = Column('Date', DateTime, nullable=False, primary_key=True),
    Average = Column('Average', Float, nullable=False, primary_key=True),
    Best_price = Column('Best_price', Float, nullable=False, primary_key=True)

    def __init__(self, id_product,Date,Average,Best_price):
        self.id_product = id_product
        self.Date = Date
        self.Average = Average
        self.Best_price = Best_price

    def __store_to_db__(self):
        # DB Connexion
        mydb = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="exemple_supero2",
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO price_histories (id_product,date,average,best_price) VALUES (%s,%s,%s,%s)"
        val = (self.id_product , self.Date , self.Average , self.Best_price)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()