import json
import requests
import pymysql
from bs4 import BeautifulSoup as BS
from global_parametrs import *
from time import sleep

def scrape(link , id_store , id_subcat):
    try:
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
            html,
            features="html.parser"
        )

        items_cards = items.findAll("div", {"class": "item-inner"})

        for num, ic in enumerate(items_cards):
            item_brand = ic.find("span", {"class": "brand"}).get_text()
            item_ref = ic.find("span", {"class": "ref"}).get_text()
            item_price =  convert_item_price_to_double(
                (ic.find("span", {"class": "price"}).get_text()).strip()
            )
            item_name = "{} {}".format(item_brand, item_ref)
            item_link = ic.find("a" , {"class" : "product photo product-item-photo"}).get('href')
            image_item = ic.find('img' , {"class" : "product-image-photo"}).get('src')
            # item_stockage = find_device_stockage(item_ref)
            # item_color = find_device_color(item_ref)
            res2 = requests.get(item_link)
            sleep(5)
            html2 = res2.text
            new_page = BS(
                html2,
                features="html.parser"
            )
            item_specification = new_page.find('div' , {'class' : 'data item content'})


            print("================{}============".format(num+1))
            print("item_brand = {}".format(item_brand))
            print("item_ref = {}".format(item_ref))
            print("item_price = {}".format(item_price))
            print("item_name = {}".format(item_name))
            print("item_link = {}".format(item_link))
            print("image_item = {}".format(image_item))
            # print("item_stockage = {}".format(item_stockage))
            # print("item_color = {}".format(item_color))
            # print("item_specification = {}".format(item_specification))
            print("\n")

            try:
                myjson = dict()
                if item_brand != None:
                    myjson["brand"] = item_brand
                if item_ref != None:
                    myjson["item_ref"] = item_ref


                # if item_stockage != "UNKNOWN":
                #     myjson["stockage"] = item_stockage
                # if item_color != "UNKNOWN":
                #     myjson["color"] = item_color
                if item_specification != None:
                    myjson['specification_table'] = item_specification
                # if item_connexion_adapter != "UNKNOWN":
                #     myjson["connexion_adapter"] = item_connexion_adapter
                # if item_screen_size != "UNKNOWN":
                #     myjson["screen_size"] = item_screen_size
                # if item_garantie != "UNKNOWN":
                #     myjson["garantie"] = item_garantie
                # if item_ram != "UNKNOWN":
                #     myjson["ram"] = item_ram
                # if item_stockage_type != "UNKNOWN":
                #     myjson["stockage_type"] = item_stockage_type
                # if item_lenght != "UNKNOWN":
                #     myjson["length"] = item_lenght
                # if item_power != "UNKNOWN":
                #     myjson["power"] = item_power


                jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)

                sql = "select current_price from items where name_in_store = %s"
                val = (item_ref)
                mycursor.execute(sql, val)
                myresult = mycursor.fetchall()
                if(len(myresult) == 0):
                    # sql = "INSERT INTO items (name ,name_in_store,link, id_store ,id_subcategory ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                    sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                    val = (item_name, item_ref, item_link, id_store, id_subcat, jsonStringify, "", image_item, item_price,scraped_at)
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

                        sql = "select id from items where name_in_store = %s"
                        val = (item_ref,)
                        mycursor.execute(sql, val)
                        myresult = mycursor.fetchall()
                        id = myresult[0][0]

                        sql = "update items set current_price = %s , last_updated_at = %s where name_in_store = %s"
                        val = (item_price , scraped_at , item_name)
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
    except:
        pass




if __name__ == "__main__":
    for l in electroplanet_console:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(15)

