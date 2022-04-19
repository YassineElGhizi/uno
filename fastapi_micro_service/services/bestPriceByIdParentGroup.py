from fastapi_micro_service.env.databaseConnexion import get, engine
import sqlalchemy as db
from fastapi_micro_service.models.produit import Product
from fastapi_micro_service.models.product__store import ProductStore
from sqlalchemy.orm import sessionmaker


def udpateBestPrice(id_parent, best_price):
    ss = sessionmaker(bind=engine)
    s = ss()
    p_list = get(
        db.select([Product.id]).where(
            db.or_(
                Product.id_parent == id_parent,
                Product.id == id_parent
            )))

    for p in p_list:
        s.query(Product).filter_by(id=p[0]).update({"best_price": f"{best_price}"})
    s.commit()


def performeUpdateBestPrice(list_of_id_parent_with_best_price):
    for i in list_of_id_parent_with_best_price:
        [ udpateBestPrice(k,v) for k, v in i.items()]


def bestPirceByIdParent():
    #Getting The Parents Ids
    parents = get(db.select([Product.id,]).where(Product.id_parent == None))


    # The Bellow Logic Groups Each Parent with the Best Price -> {id_parent(int): Decimal(best_price)}
    list_of_id_parent_with_best_price=[]
    for p in parents:
        children = get(
            db.select([Product.id,]).where(
            db.or_(
                Product.id_parent == p[0],
                Product.id == p[0]
            )))

        grouped_list=[]
        for c in children:
            prod_price = get(
                db.select([ProductStore.id_product, ProductStore.price]).where(ProductStore.id_product == c[0])
            )
            grouped_list.append(prod_price)

        d={}
        prices_tmp =[i[0][1] for i in grouped_list]
        d[grouped_list[0][0][0]] = min(prices_tmp)
        list_of_id_parent_with_best_price.append(d)
    return list_of_id_parent_with_best_price

# if __name__ == '__main__':
#     print( performeUpdateBestPrice(bestPirceByIdParent()))
