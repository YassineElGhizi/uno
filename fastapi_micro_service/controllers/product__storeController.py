from typing import List

import datetime
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from .product_historyController import store_price_hostory
from ..models.product__store import ProductStore
from ..models.produit import Product

engine = db.create_engine('mysql://root@localhost/exemple_supero2')
ss = sessionmaker(bind=engine)
s = ss()

def retraive_price(l : list , keyword : str):
    for i in l:
        if keyword == i["slug"]:
            return i["current_price"] , i['link']
        else:
            continue
    return 0.0 , None

async def storeProduct__store(store_id : int, prod_list : List[Product], prices :List):
    bulk_insert = []
    for obj in prod_list:
        price , link = retraive_price(prices , obj.slug)
        now = datetime.datetime.now()
        created_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        ps = ProductStore(obj.id, store_id ,obj.title, price, link, created_at)
        bulk_insert.append(ps)

    s.add_all(bulk_insert)
    s.commit()
    print("SUCCESS BULK INSERT #2 (ProductStore)")
    # loping over the new created products recoreds in order to create product_history
    await store_price_hostory(prod_list, prices)


