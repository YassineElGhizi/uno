import pymysql
import requests
from bs4 import BeautifulSoup as BS
import datetime


res = requests.get("https://uno.ma/iphone-maroc/iphone-12-pro-maroc/?limit=100")
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
            item_stockage = st
            return item_stockage

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
        print("================= #{} ============".format(num+1))
        print("item_title = {}".format(item_title))
        print("item_link = {}".format(item_link))
        print("item_price = {}".format(item_price))
        print("stockage = {}".format(item_stockage))
        print("item_color = {}".format(item_color))
        print("scraped_at = {}".format(scraped_at))


        try:
            sql = "INSERT INTO items (name ,slug,link, id_store ,id_category ,specification ,details ,created_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s ,%s)"
            val = ("iPhone 12 Pro",item_title, item_link, 1, 1, "stocakge: {} color: {}".format(item_stockage, item_color), "some dummy data",  scraped_at)
            mycursor.execute(sql, val)
            print("id = {}".format(
                mycursor.lastrowid
            ))
            sql = "INSERT INTO prices (id_item ,price,created_at) VALUES (%s, %s, %s)"
            val = (mycursor.lastrowid, item_price, scraped_at)
            mycursor.execute(sql, val)
            print("\n")
            mydb.commit()
        except Exception as e:
            print(e)
            print("Database conn error !")


    mydb.close()
