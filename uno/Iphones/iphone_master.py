import pymysql
import requests
from bs4 import BeautifulSoup as BS
from global_parametrs import *

def scrape(link , iphone_name):
    res = requests.get("https://uno.ma/iphone-maroc/{}-maroc/?limit=100".format(link))
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

    items = BS(
        html ,
        features="html.parser"
    )

    items_cards = items.findAll('li' , {'class' ,'item sale-product' }  )

    for num, ic in enumerate(items_cards):
        item_title_tag = (ic.find('h2' , {'class' ,'product-name' })).find('a')
        item_price = (((ic.find('p' , {'class' , 'special-price'}))).find('span' , {'class' , 'price'}).get_text()).strip()
        item_price = convert_item_price_to_double(item_price)
        item_title = item_title_tag.get_text()
        item_link = item_title_tag.get('href')
        item_stockage = find_device_stockage(item_title)
        item_color = find_device_color(item_title )
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
            sql = "select current_price from items where slug = %s"
            val = (item_title)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            if(len(myresult) == 0):
                sql = "INSERT INTO items (name ,slug,link, id_store ,id_category ,color,stockage ,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s,%s ,%s,%s ,%s, %s)"
                val = (iphone_name, item_title, item_link, 1, 1, item_color, item_stockage, "", image_item, item_price,scraped_at)
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

                    sql = "select id from items where slug = %s"
                    val = (item_title,)
                    mycursor.execute(sql, val)
                    myresult = mycursor.fetchall()
                    id = myresult[0][0]

                    sql = "update items set current_price = %s , last_updated_at = %s where slug = %s"
                    val = (item_price , scraped_at , item_title)
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
            print("Database conn error !")


    mydb.close()



if __name__ == "__main__":
    # scrape( "iphone-11-pro-max", "iPhone 11 PRO MAX")
    # scrape( "iphone-11-pro", "iPhone 11 PRO")
    # scrape( "iphone-11", "iPhone 11")


    # scrape( "iphone-12-pro-max", "iPhone 12 PRO MAX")
    # scrape( "iphone-12-pro", "iPhone 12 PRO")
    # scrape( "iphone-12", "iPhone 12")
    # scrape( "iphone-12-mini", "iPhone 12 Mini")

    # scrape( "iphone-8-plus", "iPhone 8 PLUS")
    # scrape( "iphone-7", "iPhone 7")
    # scrape( "iphone-se", "iPhone Se")

    # scrape( "apple-iphone-13-pro", "iPhone 13 PRO")
    # scrape( "apple-iphone-13", "iPhone 13")
    # scrape( "apple-iphone-13-mini", "iPhone 13 Mini")

    scrape( "iphone-xr", "iPhone Xr")

