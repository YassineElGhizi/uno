from typing import List
import sqlalchemy as db
from slugify import slugify
from sqlalchemy.orm import sessionmaker
import random
import datetime
import urllib.parse

from ..controllers.storeProductDetailsController import storeProductDetails
from ..controllers.product__storeController import storeProduct__store

from ..models.produit import Product


def network_heart_beats(website : str ,nb_prods : int ):
    now = datetime.datetime.now()
    created_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    with open('../network_heart_beats.txt' , 'a' , encoding="utf8") as f:
        f.write(f'{website} : {nb_prods} : {created_at}\n')
        f.close()

def generate_slug(title:str) -> str:
    return f"{slugify(title)}-{random.randrange(10000000, 99999999)}"

engine = db.create_engine('mysql://root@localhost/exemple_supero2')
ss = sessionmaker(bind=engine)
s = ss()
default_brand_id = 1
default_apple_category = 5
uno_store_id = 1

async def storeProduct(website: str ,listProducts : List):
    bulk_insert = []
    prices = []
    if website == 'uno':
        try:
            network_heart_beats(website, len(listProducts))
        except:
            pass
        for item in listProducts:
            try:
                name = item['prod_name']
                title = item['name_in_store']
                slug = generate_slug(title)
                if 'brand_id' in item.keys():
                    brand = item['brand_id']
                else:
                    brand = default_brand_id
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
        print("SUCCESS BULK INSERT #1 (product_details -> products)")
        #loping over the new created products recoreds in order to create product__store
        await storeProduct__store(uno_store_id ,bulk_insert, prices)




    return {"status" : 200 }