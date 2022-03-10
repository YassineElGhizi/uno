from typing import List
import sqlalchemy as db
from slugify import slugify
from sqlalchemy.orm import sessionmaker
import random
import datetime
import urllib.parse
#To update product_id_parent
from collections import defaultdict


from ..controllers.storeProductDetailsController import storeProductDetails
from ..controllers.product__storeController import storeProduct__store
from ..models.produit import Product

def generate_slug(title:str) -> str:
    return f"{slugify(title)}-{random.randrange(10000000, 99999999)}"

def get_products_parent_id(prod_name : str , session):
    res = session.query(Product.id_parent).filter(
        Product.name == prod_name,
        Product.id_parent != None
    ).first()
    if res is None:
        return res
    else:
        return res[0]

def update_id_parent(prod_list:List[Product] , session):
    groups = defaultdict(list)
    [groups[obj.name].append(obj) for obj in prod_list]
    names = groups.keys()
    names_and_thier_id = []
    for n in names:
        tmp_d = {}
        tmp = get_products_parent_id(n , session)
        if tmp != None:
            tmp_d[f'{n}'] = tmp
            names_and_thier_id.append(tmp_d)

    print('FININSHED With')
    [print(z) for z in names_and_thier_id]
    quit()
    dict_val_to_list = list(groups.values())
    big_list = []
    [big_list.append(x) for x in dict_val_to_list]
    [affect_parent_id_to_the_rest_of_items(yy) for yy in big_list]
    # [([print(f'{y}') for y in yy], print('=============\n')) for yy in big_list]
    session.commit()

def affect_parent_id_to_the_rest_of_items(items : List[Product]):
    rest_of_items = items[1:]
    id = items[0].id
    for i in rest_of_items:
        i.id_parent = id



default_apple_category = 5
uno_store_id = 1

async def storeProduct(website: str ,listProducts : List):
    engine = db.create_engine('mysql://root@localhost/exemple_supero2')
    ss = sessionmaker(bind=engine)
    s = ss()
    bulk_insert = []
    prices = []
    if website == 'uno':
        for item in listProducts:
            try:
                name = item['prod_name']
                title = item['name_in_store']
                slug = generate_slug(title)
                brand = item['brand_id']
                try:
                    category = item['category_in_store_to_id']
                except:
                    category = default_apple_category
                product_details = storeProductDetails(item['details'] , title)
                imgs = urllib.parse.quote_plus(item['image_url'])
                images = f"[\"{imgs}\"]"
                id_parent = None
                try:
                    options = str([str(i) for i in item['options']])
                except:
                    pass
                now = datetime.datetime.now()
                created_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
                p = Product(name , title , slug ,brand ,category, product_details, images, id_parent, options ,created_at)
                bulk_insert.append(p)
                d = {}
                d['slug'] = slug
                d['current_price'] = item['current_price']
                d['link'] = item['link']
                prices.append(d)
            except Exception as e:
                raise e
                pass

        s.add_all(bulk_insert)
        s.commit()
        update_id_parent(bulk_insert , s)
        print("SUCCESS BULK INSERT #1 (product_details & products)")
        #loping over the new created products recoreds in order to create product__store
        await storeProduct__store(uno_store_id ,bulk_insert, prices)



    return {"status" : 200 }