import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from global_parametrs import *
from time import sleep


def scrape(link , prod_name , id_store , id_subcat):
    res = requests.get("{}".format(link))
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
        item_screen_size = find_device_screen_size(item_title)
        item_connexion_adapter = find_device_connextion_adapter(item_title)
        item_garantie = find_device_garantie(item_title)
        item_ram = find_device_ram(item_title)
        item_stockage_type = find_device_type_stockage(item_title)
        item_lenght = find_device_lenght(item_title)
        item_power = find_device_power(item_title)
        print("================= #{} ============".format(num+1))
        print("item_title = {}".format(item_title))
        print("item_link = {}".format(item_link))
        print("item_price = {}".format(item_price))
        print("stockage = {}".format(item_stockage))
        print("item_color = {}".format(item_color))
        print("scraped_at = {}".format(scraped_at))
        print("image_item = {}".format(image_item))
        print("item_screen_size = {}".format(item_screen_size))
        print("item_connexion_adapter = {}".format(item_connexion_adapter))
        print("item_garantie = {}".format(item_garantie))
        print("prod_name= {}".format(prod_name))
        print("item_ram= {}".format(item_ram))
        print("item_stockage_type= {}".format(item_stockage_type))
        print("item_lenght= {}".format(item_lenght))
        print("item_power= {}".format(item_power))

        try:
            myjson = dict()
            if item_stockage != "UNKNOWN":
                myjson["stockage"] = item_stockage
            if item_color != "UNKNOWN":
                myjson["color"] = item_color
            if item_connexion_adapter != "UNKNOWN":
                myjson["connexion_adapter"] = item_connexion_adapter
            if item_screen_size != "UNKNOWN":
                myjson["screen_size"] = item_screen_size
            if item_garantie != "UNKNOWN":
                myjson["garantie"] = item_garantie
            if item_ram != "UNKNOWN":
                myjson["ram"] = item_ram
            if item_stockage_type != "UNKNOWN":
                myjson["stockage_type"] = item_stockage_type
            if item_lenght != "UNKNOWN":
                myjson["length"] = item_lenght
            if item_power != "UNKNOWN":
                myjson["power"] = item_power


            jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)

            sql = "select current_price from items where slug = %s"
            val = (item_title)
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            if(len(myresult) == 0):
                sql = "INSERT INTO items (name ,slug,link, id_store ,id_subcategory ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                val = (prod_name, item_title, item_link, id_store, id_subcat, jsonStringify, "", image_item, item_price,scraped_at)
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
    #Uno Iphone
    # for l in uno_iphones_links:
    #     scrape( "{}".format(l['link']), "{}".format(l['product_name']) ,l["id_store"] , l["subcategory"])
    #     sleep(20)

    # for l in uno_ipads_links:
    #     scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
    #     sleep(20)

    # for l in uno_mac_links:
    #     scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
    #     sleep(20)

    # for l in uno_watches_links:
    #     scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
    #     sleep(20)

    # for l in uno_tvs_links:
    #     scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
    #     sleep(20)

    for l in uno_accessoires_links:
        scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
        sleep(20)