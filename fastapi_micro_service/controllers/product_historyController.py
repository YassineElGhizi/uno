import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from statistics import mean
from typing import List
import statistics


from fastapi_micro_service.models.product__store import ProductStore
from fastapi_micro_service.env.databaseConnexion import engine
from fastapi_micro_service.env.databaseConnexion import get
from fastapi_micro_service.models.produit import Product
from fastapi_micro_service.models.price_history import PriceHistory


connection = engine.connect()
metadata = db.MetaData()
pht = db.Table('price_histories', metadata,
          db.Column('id_product', db.Integer(), nullable=False),
          db.Column('Date', db.DateTime, nullable=False),
          db.Column('Average', db.Float(), nullable=False),
          db.Column('Best_price', db.Float, nullable=False))

def get_price_only(l : list , keyword : str) -> float:
    for i in l:
        if keyword == i["slug"]:
            return i["current_price"]
        else:
            continue
    return 0.0

async def store_price_hostory(prod_list : List[Product], prices :List):
    ss = sessionmaker(bind=engine)
    s = ss()
    bulk_insert2 = []
    connection = engine.connect()
    metadata = db.MetaData()
    price_histories = db.Table('price_histories', metadata, autoload=True, autoload_with=engine)

    for obj in prod_list:
        query = db.select([price_histories.columns.best_price,]).where(price_histories.columns.id_product == obj.id,)
        ResultProxy = connection.execute(query)
        r = ResultProxy.fetchall()


        #list of all the prices from price history table (query based )
        l = [i[0] for i in r]
        l.append(get_price_only(prices , obj.slug))
        #calcuting the mean after adding the new price into acount
        m = mean(l)

        #fetching all variants and finding the best price -> (min)
        pd_prices = s.query(ProductStore.price).where(ProductStore.id_product == obj.id).all()

        pd_prices_from_tuple_to_list = list(pd_prices[0])
        pd_prices_from_tuple_to_list.append(get_price_only(prices , obj.slug))
        min_var = min(pd_prices_from_tuple_to_list)

        d = {}
        d['id_product'] = obj.id
        d['Average'] = m
        d['best_price'] = min_var

        bulk_insert2.append(d)

    s.commit()
    query = db.insert(pht)
    connection.execute(query, bulk_insert2)
    s.commit()

    print("SUCCESS BULK INSERT #3 (price History)")

def price_history():
    ss = sessionmaker(bind=engine)
    s = ss()
    list_price_history_models=[]
    # Getting The Parents Ids
    parents = get(db.select([Product.id, ]).where(Product.id_parent == None))
    # The Bellow Logic Groups Each Parent with the Best Price -> {id_parent(int): Decimal(best_price)}
    list_of_id_parent_with_best_price = []
    for p in parents:
        children = get(
            db.select([Product.id, ]).where(
                db.or_(
                    Product.id_parent == p[0],
                    Product.id == p[0]
                )))

        grouped_list = []
        for c in children:
            prod_price = get(
                db.select([ProductStore.id_product, ProductStore.price]).where(ProductStore.id_product == c[0])
            )
            grouped_list.append(prod_price)

        d = {}
        prices_tmp = [i[0][1] for i in grouped_list]
        d[grouped_list[-1][0][0]] =prices_tmp
        list_of_id_parent_with_best_price.append(d)

    for x in list_of_id_parent_with_best_price:
        key = int(*x)
        best_price = min(x[key])
        average = statistics.mean(x[key])
        ph = PriceHistory(key, average, best_price)
        list_price_history_models.append(ph)


    s.add_all(list_price_history_models)
    s.commit()
