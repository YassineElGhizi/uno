import sys
sys.path.append("..") # Adds higher directory to python modules path.
from typing import List
import pymysql
from slugify import slugify
from sqlalchemy.orm import sessionmaker
import random

from controllers.storeProductDetailsController import storeProductDetails
from controllers.product__storeController import storeProduct__store
from fastapi_micro_service.env.databaseConnexion import engine, myTempStamp
from fastapi_micro_service.models.produit import Product

default_not_mapped_category = 449
def generate_slug(title:str) -> str:
    return f"{slugify(title)}-{random.randrange(10000000, 99999999)}"

def get_products_parent_id(unique_id : str, session):
    res = session.query(Product.id_parent).filter(
            Product.unique_id == unique_id,
            Product.id_parent != None).first()
    if res is None:
        return res
    return res[0]

def get_website_id(website_name:str)-> int:
    if website_name == 'uno':
        return 1
    if website_name == 'electroplanet':
        return 3
    if website_name == 'kitea':
        return 4
    if website_name == 'bricoma':
        return 5
    if website_name == 'decathlon':
        return 6
    if website_name == 'ikea':
        return 7
    if website_name == 'cosmoseelectro':
        return 8
    if website_name == 'bestmark':
        return 11
    if website_name == 'iris':
        return 10
    if website_name == 'saligon':
        return 12
    if website_name == 'electrobousfiha':
        return 13



async def storeProduct(website: str,listProducts : List):
    ss = sessionmaker(bind=engine)
    s = ss()
    bulk_insert = []
    prices = []
    store_id = get_website_id(website)

    for item in listProducts:
        try:
            if item['name_in_store'] and item['prod_title'] and item['unique_id'] and item['current_price'] and item['link']:
                name = item['name_in_store']
                title = item['prod_title']
                slug = generate_slug(title)
                brand = item['brand_id']
                unique_id = item['unique_id']
                try:
                    category = item['category_in_store_to_id']
                except:
                    category = default_not_mapped_category
                product_details = storeProductDetails(item['details'], title)
                imgs = item['image_url']
                images = f"[\"{imgs}\"]"
                id_parent = None
                try:
                    options = str([i for i in item['options']])
                except:
                    pass

                created_at = myTempStamp()
                p = Product(name, title, slug, brand, category, product_details, images, id_parent, options, unique_id, created_at)
                bulk_insert.append(p)

                d = {}
                d['slug'] = slug
                d['current_price'] = item['current_price']
                d['link'] = item['link']

                prices.append(d)
            else:
                print('IMPORTANT WARNING !! FIELDS ARE MISSING !!')
                continue
        except Exception as e:
            raise e
            pass

    s.add_all(bulk_insert)
    s.commit()
    print("SUCCESS BULK INSERT #1 (product_details & products)")
    await storeProduct__store(store_id, bulk_insert, prices)
    return {"status": 200}


def update_id_parent():
    #PART 1:
    mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_api",)
    mycursor = mydb.cursor()
    sql = "select unique_id from products group by unique_id having count(*) > 1;"
    mycursor.execute(sql,)
    myresult = mycursor.fetchall()
    l = []
    for t in myresult:
        l.append(t[0])
    #l : Contains list of same prodcuts

    #PART 2:
    for refrerance in l:
        sql = f"select id ,id_parent from products where unique_id = '{refrerance}';"
        mycursor.execute(sql, )
        myresult = mycursor.fetchall()
        found = False
        id_parent = None
        for r in myresult:
            if r[1] == None:#ida kan id_parent null ==> parent found !
                found = True
                id_parent = r[0]

        if not found:#ida malqina ta xi ud_parent null ==> parent howa first produit
            parent_id = myresult[0][0]
            for item in myresult[1::]:
                sql = f"update products set id_parent = {parent_id} where id = '{item[0]}';"
                mycursor.execute(sql, )
        else:#ida deja kayn produit parent ==> for each prduit id dialo != id_parent , we will give it id_parent = id_parent
            for item in myresult:
                if item[0] != id_parent:
                    sql = f"update products set id_parent = {id_parent} where id = '{item[0]}';"
                    mycursor.execute(sql, )



    mydb.commit()