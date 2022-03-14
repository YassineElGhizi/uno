import json
import time

import pymysql
import requests
from bs4 import BeautifulSoup as BS
from global_parametrs import *
from time import sleep
import random

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-US,en;q=0.9',
    'DNT': '1',
    'Referer': 'https://google.com'
}

list_of_subcats_and_thier_links = list()
print("[+] requesting kiteak.com")
res = requests.get("https://www.kitea.com/" , headers=headers)
items = BS(res.text,features="html.parser")
all_categories_toscrape = items.findAll('div' , {'class' : 'sm-megamenu-child sm_megamenu_dropdown_6columns'})
print("[+] preparing cats & subcats")
for i in all_categories_toscrape:
    in_site_category = i.findAll('a' , {'class' : 'sm_megamenu_nodrop'})
    for x in in_site_category:
        children = x.findChildren("span" ,{'class' : 'sm_megamenu_title_lv-3'}, recursive=False)
        for child in children:
            d = {}
            d["subcategory_in_site"] = child.get_text()
            d["link"] = x.get('href')
            list_of_subcats_and_thier_links.append(d)


def scrape():
    try:
        print("     [+] starting scrap()")
        for l in list_of_subcats_and_thier_links :
            s = requests.session()
            res = s.get("{}".format(l["link"]) , headers=headers)
            html = res.text

            #DB Connexion
            mydb = pymysql.connect(
                host="127.0.0.1",
                port=3306,
                user="root",
                password="",
                database="supero_datalake2",
            )
            mycursor = mydb.cursor()

            items = BS(html,features="html.parser")
            items_cards = items.findAll("div", {"class": "product-item-info"})

            for num, ic in enumerate(items_cards):
                image_item = ic.find('img' , {'class' : 'product-image-photo'}).get('src')
                item_link = ic.find('a' , {'class' : 'product photo product-item-photo'}).get('href')
                try:
                    res2 = s.get(item_link , headers=headers)
                except:
                    continue
                sleep(random.randint(1,3))
                html2 = res2.text
                new_page = BS(html2,features="html.parser")
                item_name_instore = new_page.find('span' , {"class" : "base"}).get_text()
                tmp = new_page.find('div' , {'class' : 'product-info-price'})
                item_price = convert_item_price_to_double(tmp.find("span", {"class": "price"}).get_text())
                item_ref = tmp.find("div", {"class": "value"}).get_text()
                print("item_name_instore = {}".format(item_name_instore))
                print("item_price = {}".format(item_price))
                print("item_ref = {}".format(item_ref))
                tmp = new_page.findAll('div' , {'class' : 'additional-attributes-wrapper'})
                item_description = tmp[0].get_text()
                item_specification = tmp[1]
                print("item_description = {}".format(item_description))
                print("item_specification = {}".format(item_specification))
                print("item_link = {}".format(item_link))
                print("image_item = {}".format(image_item))

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
                        # sql = "INSERT INTO items (name ,name_in_store,link, id_store ,id_subcategory ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                        sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                        val = (item_name_instore, item_ref, item_link, 4, l["subcategory_in_site"], jsonStringify, item_description, image_item, item_price,scraped_at)
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
                    print("Database conn error !")


            mydb.close()
    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    start = time.time()
    scrape()
    print(f'Finished in {time.time() - start} seconds')