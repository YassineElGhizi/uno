import json

import pymysql
import requests
from bs4 import BeautifulSoup as BS
import datetime

# res = requests.get("https://uno.ma/iphone-maroc/apple-iphone-13-mini-maroc/")
res = requests.get("https://uno.ma/iphone-maroc/apple-iphone-13-mini-maroc/?limit=100")
html = res.text

#DB Connexion
mydb = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="datalake",
)
mycursor = mydb.cursor()


#GLOBAL Vars
items_present_in_page = dict()
cards_links = list()
stockage_list = ['128 Gb','256 Gb','512 Gb','1 Tb' ]
now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

#Functions
def find_device_stockage(title):
    for st in stockage_list:
        if st in title:
            return st

    return "UNKNOWN"

def find_device_color(title , stockage):
    try:
        tmp = title.split("{} ".format(stockage))[-1]
        tmp = tmp.split("(")[0]
        return tmp
    except:
        return "UNKNOW"

def convert_item_price_to_double(price):
    tmp = price.split("MAD")[0]
    tmp = tmp.split()
    floatprice = "".join(tmp)
    floatprice = floatprice.replace("," , ".")
    return float(floatprice)



items = BS(
    html ,
    features="html.parser"
)

# print(items.prettify())
# quit()

if __name__ == "__main__":
    items_cards = items.findAll('li' , {'class' ,'item sale-product' }  )

    for num, ic in enumerate(items_cards):
        item_title_tag = (ic.find('h2' , {'class' ,'product-name' })).find('a')
        item_price = (((ic.find('p' , {'class' , 'special-price'}))).find('span' , {'class' , 'price'}).get_text()).strip()
        item_price = convert_item_price_to_double(item_price)
        item_title = item_title_tag.get_text()
        item_link = item_title_tag.get('href')
        item_stockage = find_device_stockage(item_title)
        item_color = find_device_color(item_title ,item_stockage)
        image_item = ic.find('img' , {'class' , 'regular_img'}).get('data-srcx2')
        print("================= #{} ============".format(num+1))
        print("item_title = {}".format(item_title))
        print("item_link = {}".format(item_link))
        print("item_price = {}".format(item_price))
        print("stockage = {}".format(item_stockage))
        print("item_color = {}".format(item_color))
        print("scraped_at = {}".format(scraped_at))
        print("image_item = {}".format(image_item))

        try:
            shoudl_I_insert_to_db = True
            myjson = dict()
            myjson["stockage"] = item_stockage
            myjson["color"] = item_color
            jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)

            sql = "select current_price from items where slug = %s"
            val = (item_title)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            if(len(myresult) == 0):
                sql = "INSERT INTO items (name ,slug,link, id_store ,id_category ,specification ,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                val = ("iPhone 13 Mini",item_title, item_link, 1, 1, jsonStringify, "", image_item, item_price,scraped_at)
                mycursor.execute(sql, val)
                print("id = {}".format(
                    mycursor.lastrowid
                ))
                sql = "INSERT INTO prices (id_item ,price,created_at) VALUES (%s, %s, %s)"
                val = (mycursor.lastrowid, item_price, scraped_at)
                mycursor.execute(sql, val)
                print("\n")
                mydb.commit()
            else:
                if(myresult[0][0] != item_price ):
                    sql = "update items set current_price = %s , last_updated_at = %s where slug = %s"
                    val = (item_price , scraped_at , item_title)
                    mycursor.execute(sql, val)
                    sql = "select id from items where slug = %s"
                    val = (item_title,)
                    myresult = mycursor.fetchall()
                    sql = "insert into prices (id_item ,price,created_at) VALUES (%s, %s, %s)"
                    val = (myresult[0][0], item_price, scraped_at)
                    mydb.commit()
                else:
                    print("PRICES ARE STILL THE SAME")
                    print(" -> {} == {}".format(myresult[0][0] , item_price))


        except Exception as e:
            print(e)
            print("Database conn error !")


    mydb.close()
