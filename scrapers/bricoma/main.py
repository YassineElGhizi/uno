import json
import time

import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random

list_of_cats_and_thier_links = list()
list_of_subcats_and_thier_links = list()
now = datetime.datetime.now()


def init():
    print("[+] Initialisation")
    res = requests.get("https://www.bricoma.ma/")
    items = BS(res.text,features="html.parser")
    all_categories_toscrape = items.findAll('a' , {'class' : 'level-top'})
    for i in all_categories_toscrape:
        d = dict()
        d["link"] = i.get('href')
        d["category_in_site"] = i.find('span').get_text().strip()
        list_of_cats_and_thier_links.append(d)


def scrape():
    try:
        init()
    except Exception as e:
        print(f"Err in init() BRICOMA {e}")
        return -1

    try:
        print("[+] Getting categories")
        sess = requests.session()
        for l in list_of_cats_and_thier_links :
            res = sess.get("{}".format(l["link"]))

            #DB Connexion
            mydb = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="supero_datalake2",)
            mycursor = mydb.cursor()
            items = BS(res.text,features="html.parser")
            subcats = items.findAll('a' , {'class' : 'category-name'})
            print("     [+] Getting SubCategries")
            for s in subcats:
                dd = dict()
                dd["link"] = s.get('href')
                dd["subcategory_in_site"] = s.get_text().strip()
                list_of_subcats_and_thier_links.append(dd)

            print("         [+] Scraping Items")
            for item in list_of_subcats_and_thier_links:
                try:
                    res2 = sess.get("{}{}".format(item["link"] ,"?product_list_limit=32"), timeout=3)
                except Exception as e:
                    print(f'Exception = {e}')
                    continue
                sleep(random.randint(1 , 2))
                new_page2 = BS(res2.text,features="html.parser")
                items_cards = new_page2.findAll('div' , {'class' : 'actions-primary'})
                mylist = list()
                for ihref in items_cards:
                    mylist.append(ihref.find('a').get('href'))
            print("             [+] Collecting data")
            for num, link in enumerate(mylist):
                res2 = sess.get(link)
                sleep(random.randint(1 , 2))
                new_page = BS(res2.text,features="html.parser")

                item_name_in_store = new_page.select_one(
                    '#maincontent > div.columns > div > div.product-info-main > div.page-title-wrapper.product > h1 > span'
                ).get_text()
                item_ref = new_page.select_one(
                    '#maincontent > div.columns > div > div.product-info-main > div.product-header-info > div > div'
                ).get_text()
                item_description = new_page.select_one(
                    '#maincontent > div.columns > div > div.product-info-main > div.product.attribute.overview > div >p'
                )
                item_specification = new_page.select_one('#product-attribute-specs-table > tbody')
                item_link = link
                image_item = new_page.find('img', {'class': 'gallery-placeholder__image'}).get('src')
                price = new_page.find('span' , {'data-price-type' : 'finalPrice'})
                price = price.find('span').get_text()
                price = price.replace('MAD', '')
                price = price.replace(',', '.')
                tmp = price.split()
                floatprice = "".join(tmp)
                tmp = float(floatprice)
                item_price = tmp
                item_short_name = ''

                print("item_name_in_store = {}".format(item_name_in_store))
                print("item_ref = {}".format(item_ref))
                print("item_description = {}".format(item_description))
                print("item_specification = {}".format(item_specification))
                print("item_link = {}".format(item_link))
                print("image_item = {}".format(image_item))
                print("item_price = {}".format(item_price))
                print("item_subcat_in_website = {}".format(item["subcategory_in_site"]))
                print("\n")

                try:
                    myjson = dict()
                    if item_specification != None:
                        myjson['specification_table'] = item_specification
                    jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)


                    sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,unique_id) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                    val = (item_short_name, item_name_in_store, item_link, 5, item["subcategory_in_site"], jsonStringify, item_description, image_item, item_price,item_ref)
                    mycursor.execute(sql, val)
                    mydb.commit()


                except Exception as e:
                    print(e)
                    print(e.__traceback__.tb_lineno)
                    print(__file__)
                    print("Database conn error !")
                    pass

            mydb.close()
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_lineno)
        print(__file__)
        pass

if __name__ == "__main__":
    start = time.time()
    scrape()
    print(f'Finished in {time.time() -start} seconds')