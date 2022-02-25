import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from statistics import mean
import datetime
from typing import List

from fastapi_micro_service.models.product__store import ProductStore
from fastapi_micro_service.models.produit import Product

engine = db.create_engine('mysql://root@localhost/exemple_supero2')

connection = engine.connect()
metadata = db.MetaData()
pht = db.Table('price_histories', metadata,
              db.Column('id_product', db.Integer(), nullable=False),
              db.Column('Date', db.DateTime, nullable=False),
              db.Column('Average', db.Float(), nullable=False),
              db.Column('Best_price', db.Float, nullable=False)
)



ss = sessionmaker(bind=engine)
s = ss()

def retraive_price_only(l : list , keyword : str) -> float:
    for i in l:
        if keyword == i["slug"]:
            return i["current_price"]
        else:
            continue
    return 0.0

async def store_price_hostory(prod_list : List[Product], prices :List):
    bulk_insert2 = []
    for obj in prod_list:
        connection = engine.connect()
        metadata = db.MetaData()
        options = db.Table('price_histories', metadata, autoload=True, autoload_with=engine)
        query = db.select([
            options.columns.Best_price,
        ]).where(
                options.columns.id_product == obj.id,
        )
        ResultProxy = connection.execute(query)
        r = ResultProxy.fetchall()

        #list of all the prices from price history table (query based )
        l = [i[0] for i in r]
        l.append(retraive_price_only(prices , obj.slug))
        #calcuting the mean after adding the new price into acount
        m = mean(l)

        #fetching all variants and finding the best price -> (min)
        pd_prices = s.query(ProductStore.price).where(ProductStore.id_product == obj.id).all()
        pd_prices_from_tuple_to_list = list(pd_prices[0])
        pd_prices_from_tuple_to_list.append(retraive_price_only(prices , obj.slug))
        min_var = min(pd_prices_from_tuple_to_list)
        now = datetime.datetime.now()
        created_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        d = {}
        d['id_product'] = obj.id
        d['Date'] = created_at
        d['Average'] = m
        d['Best_price'] = min_var
        s.query(Product).filter_by(id=obj.id).update({"best_price": f"{min_var}"})
        s.commit()
        bulk_insert2.append(d)

    query = db.insert(pht)
    connection.execute(query, bulk_insert2)


    print("SUCCESS BULK INSERT #3 (price History)")


