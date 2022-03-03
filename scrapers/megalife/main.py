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

def init():
    print("[+] Initilialisation")
    res = requests.get("https://megalife.ma/")
    items = BS(res.text, features="html.parser")
    h5s = items.findAll(['h5', 'h6'])
    for h in h5s:
        try:
            d = dict()
            d["link"] = h.find('a').get('href')
            d["name_sub_cat"] = h.find('a').get_text().strip()
            list_of_subcats_and_thier_links.append(d)
        except:
            pass

    panaux_sol = items.findAll('h3' , {'class' : 'elementor-image-box-title'})
    for x in panaux_sol:
        try:
            d = dict()
            d["link"] = x.find('a').get('href')
            d["name_sub_cat"] = x.find('a').get_text().strip()
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
            items = new_page2.findAll('a', {'class': 'product-image-link'})
            try:
                mylist = [tag.get('href') for tag in items]
            except:
                mylist=[]

            print("             [+] Collecting data")
            for num, link in enumerate(mylist):
                res2 = requests.get(link)
                sleep(random.randint(4 , 7))
                new_page = BS(res2.text,features="html.parser")

                try:
                    item_name_instore = new_page.find('h1',{'class': 'product_title wd-entities-title'}).get_text().strip()
                    item_ref = "Megalife-{}".format(item_name_instore)
                    item_description =new_page.find('div' , {'class' : 'woocommerce-product-details__short-description'}).get_text().strip()
                    item_specification = new_page.find('table' , {'class' : 'woocommerce-product-attributes shop_attributes'})
                    item_link = link
                    image_item = new_page.find('figure', {'class': 'woocommerce-product-gallery__image'})
                    image_item = image_item.find('a').get('href')

                    item_price = new_page.find('p', {'class': 'price'}).get_text().strip()
                    numbers = [word for word in item_price.split() if word.isdigit()]
                    item_price = "".join(numbers)
                    print("item_name_instore = {}".format(item_name_instore))
                    print("item_ref = {}".format(item_ref))
                    print("item_description = {}".format(item_description))
                    print("item_specification = {}".format(item_specification))
                    print("item_link = {}".format(item_link))
                    print("image_item = {}".format(image_item))
                    print("item_price = {}".format(item_price))
                    print("item_subcat_in_website = {}".format(item["name_sub_cat"]))
                    print("\n")
                except Exception as e:
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
                        val = (item_name_instore, item_ref, item_link, 8, item["name_sub_cat"], jsonStringify, item_description, image_item, item_price,scraped_at)
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
                    pass
        try:
           mydb.close()
        except:
            pass
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_lineno)
        print(__file__)
        pass
    finally:
        mydb.close()


if __name__ == "__main__":
    scrape()