import sys
sys.path.append("..") # Adds higher directory to python modules path.
import datetime
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from models.productDetails import ProductDetail
from fastapi_micro_service.env.databaseConnexion import engine


ss = sessionmaker(bind=engine)
s = ss()

def storeProductDetails(details : str , short_des : str) -> int:
    now = datetime.datetime.now()
    created_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    pd = ProductDetail(short_des, details, created_at)
    s.add(pd)
    s.commit()
    return pd.id



