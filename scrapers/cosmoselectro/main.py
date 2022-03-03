import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random

list_of_cats_and_thier_links = list()
list_of_subcats_and_thier_links = list()
now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

def formatPrice(price):
    tmp = price.replace('Dhs' , '')
    tmp = tmp.replace(',' , ' ')
    tmp =tmp.split()
    floatprice = "".join(tmp)
    return float(floatprice)

def getImageSrc(tags):
    for tag in tags:
        try:
            src = tag.get('src')
            if 'https://www.cosmoselectro.ma/storage/products' in src:
                return src
        except:
            pass

    return None

def init():
    print("[+] Initilialisation")
    res = requests.get("https://www.cosmoselectro.ma/")
    items = BS(res.text, features="html.parser")
    h4s = items.findAll('h4')
    for i in h4s:
        try:
            d = dict()
            d["link"] =i.find('a').get('href')
            d["subcat_name"] = i.find('a').get_text().strip()
            list_of_subcats_and_thier_links.append(d)
        except:
            pass

def scrape():
    try:
        init()

        mydb = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="datalake",
        )
        mycursor = mydb.cursor()

        print("         [+] Scraping Items")
        for item in list_of_subcats_and_thier_links:

            res2 = requests.get("{}".format(item["link"]))
            sleep(random.randint(4 , 7))
            new_page2 = BS(res2.text,features="html.parser")
            items_cards = new_page2.findAll('a', {'class': 'ps-product__title'})
            mylist = list()
            for ihref in items_cards:
                try:
                    mylist.append(ihref.get('href'))
                except:
                    pass

            print("             [+] Collecting data")
            for num, link in enumerate(mylist):
                res2 = requests.get(link)
                sleep(random.randint(4 , 7))
                new_page = BS(res2.text,features="html.parser")

                try:
                    item_name_instore = new_page.select_one(
                        '#product-page > div.ps-container > div > div.ps-page--product > div > div.ps-page__container > div.ps-page__left > div > div.ps-product__header > div.ps-product__info > h1'
                    ).get_text().strip()

                    item_ref = new_page.select_one('#product-sku').get_text().strip()
                    item_description = new_page.select_one('#tab-description > div').get_text().strip()
                    item_specification = new_page.select_one('#product-specs > tbody')
                    item_link = link
                    image_item = getImageSrc(new_page.findAll('img'))
                    item_price = new_page.select_one(
                        '#product-page > div.ps-container > div > div.ps-page--product > div > div.ps-page__container > div.ps-page__left > div > div.ps-product__header > div.ps-product__info > h4 > span'
                    ).get_text().strip()
                    item_price = formatPrice(item_price)

                    print("item_name_instore = {}".format(item_name_instore))
                    print("item_ref = {}".format(item_ref))
                    print("item_description = {}".format(item_description))
                    print("item_specification = {}".format(item_specification))
                    print("item_link = {}".format(item_link))
                    print("image_item = {}".format(image_item))
                    print("item_price = {}".format(item_price))
                    print("item_subcat_in_website = {}".format(item["subcat_name"]))
                    print("\n")
                except Exception as e:
                    print("something wroing in parsing html")
                    print(e)
                    print(e.__traceback__.tb_lineno)
                    print(__file__)
                    continue
                try:
                    myjson = dict()
                    if item_specification != None:
                        myjson['specification_table'] = item_specification
                    jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)

                    sql = "select current_price from items where name_in_store = %s"
                    val = (item_ref)
                    mycursor.execute(sql, val)
                    myresult = mycursor.fetchall()
                    if(len(myresult) == 0):
                        sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                        val = (item_name_instore, item_ref, item_link, 8, item["subcat_name"], jsonStringify, item_description, image_item, item_price,scraped_at)
                        mycursor.execute(sql, val)
                        print("id = {}".format(mycursor.lastrowid))
                        sql = "INSERT INTO prices (id_item ,price,created_at) VALUES (%s, %s, %s)"
                        val = (mycursor.lastrowid, item_price, scraped_at)
                        mycursor.execute(sql, val)
                        print("\n")
                        mydb.commit()
                    else:
                        if(myresult[0][0] != item_price ):
                            sql = "select id from items where name_in_store = %s"
                            val = (item_ref,)
                            mycursor.execute(sql, val)
                            myresult = mycursor.fetchall()
                            id = myresult[0][0]
                            sql = "update items set current_price = %s , last_updated_at = %s where name_in_store = %s"
                            val = (item_price , scraped_at , item_ref)
                            mycursor.execute(sql, val)
                            mydb.commit()

                            sql = "INSERT INTO prices (id_item ,price,created_at) VALUES (%s, %s, %s)"
                            val = (id, item_price, scraped_at)
                            mycursor.execute(sql, val)
                            mydb.commit()
                        else:
                            print("PRICES ARE STILL THE SAME")
                            print(" -> {} == {}".format(myresult[0][0] , item_price))

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
    finally:
        mydb.close()


if __name__ == "__main__":
    scrape()