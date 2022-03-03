import json
import logging
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random


logging.basicConfig(filename='iris.log', level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
list_of_cats_and_thier_links = list()
list_of_subcats_and_thier_links = list()
now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

def convertPrice(price):
    tmp = price.replace('MAD' , '')
    tmp = tmp.replace(',' , '.')
    tmp = tmp.split()
    return float("".join(tmp))

def init():
    print("[+] Initilialisation")
    res = requests.get("https://www.iris.ma/")
    items = BS(res.text, features="html.parser")
    uls = items.findAll('ul')
    for ul in uls:
        for li in ul.findAll('a'):
            titlestr = li.text.strip()
            if len(titlestr) < 30:
                if titlestr not in ["" , "Ajouter au panier" , "Imprimante & Scanner" , "Imprimante" , "Scanner" , "Consommables" , "Ordinateur portable" , "Accessoires & composants" , "Ordinateur fixe" , "Logiciel" , "Tablette tactile, Ipad" , "Onduleur" , "Stockage" , "Souris" , "Clavier" , "Pack Clavier/Souris" , "Vidéoprojecteur" , "Écran de projection" , "Appareil photo numérique" , "Haut-parleur" , "Switch" , "Serveur" , "Détails" , "Aperçu rapide"] :
                    d = dict()
                    d["link"] = li.get('href')
                    d["name_sub_cat"] = titlestr
                    list_of_subcats_and_thier_links.append(d)

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
        for item in list_of_subcats_and_thier_links[4:-17]:
            res2 = requests.get("{}".format(item["link"]))
            sleep(random.randint(4 , 7))
            new_page2 = BS(res2.text,features="html.parser")

            cards = new_page2.findAll('a', {'class': 'product-name'})
            mylist = []
            for card in cards:
                try:
                    mylist.append(card.get('href'))
                except:
                    pass

            print("             [+] Collecting data")
            for num, link in enumerate(mylist):
                res2 = requests.get(link)
                sleep(random.randint(4 , 7))
                new_page = BS(res2.text,features="html.parser")

                try:
                    item_name_instore = new_page.select_one(
                        '#center_column > div.primary_block.row > div.pb-center-column.col-xs-12.col-sm-7.col-md-6 > h1'
                    ).text.strip()

                    item_ref = new_page.select_one('#product_reference > span').text.strip()
                    item_description = new_page.select_one('#short_description_block').text.strip()
                    item_link = link
                    image_item = new_page.select_one('#bigpic').get('src')
                    item_price = new_page.select_one('#our_price_display').text.strip()
                    item_price = convertPrice(item_price)

                    try:
                        item_specification = new_page.find('table')
                    except:
                        item_specification = None

                    try:
                        item_reviews = new_page.findAll('div', {'class': 'comment_details col-sm-10'})
                    except:
                        item_reviews = None


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
                    print("something went wrong in parsing html")
                    print(e)
                    print(e.__traceback__.tb_lineno)
                    print(__file__)
                    continue
                try:
                    myjson = dict()
                    if item_specification != None:
                        myjson['specification_table'] = item_specification
                    if item_reviews != None:
                        myjson['reviews'] = item_reviews

                    jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)

                    sql = "select current_price from items where name_in_store = %s"
                    val = (item_ref)
                    mycursor.execute(sql, val)
                    myresult = mycursor.fetchall()
                    if(len(myresult) == 0):
                        sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                        val = (item_name_instore, item_ref, item_link, 10, item["name_sub_cat"], jsonStringify, item_description, image_item, item_price,scraped_at)
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

                except:
                    pass
        try:
            mydb.close()
        except:
            pass
    except:
        pass
    finally:
        mydb.close()


if __name__ == "__main__":
    scrape()