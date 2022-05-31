import sys
sys.path.append("..") # Adds higher directory to python modules path.
from typing import List
from sqlalchemy.orm import sessionmaker

from models.product__store import ProductStore
from fastapi_micro_service.env.databaseConnexion import engine, myTempStamp
from fastapi_micro_service.models.produit import Product


def retraive_price(l : list , keyword : str):
    for i in l:
        if keyword == i["slug"]:
            return i["current_price"] , i['link']
        else:
            continue
    return 0.0 , None

async def storeProduct__store(store_id : int, prod_list : List[Product], prices :List):
    bulk_insert = []
    ss = sessionmaker(bind=engine)
    s = ss()
    for obj in prod_list:
        price , link = retraive_price(prices , obj.slug)
        created_at = myTempStamp()
        ps = ProductStore(obj.id, store_id ,obj.title, price, link, created_at)
        bulk_insert.append(ps)

    s.add_all(bulk_insert)
    s.commit()
    print("SUCCESS BULK INSERT #2 (ProductStore)")
    # loping over the new created products recoreds in order to create product_history
    # await store_price_hostory(prod_list, prices)



