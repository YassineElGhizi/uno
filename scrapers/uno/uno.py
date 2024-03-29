import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from global_parametrs import *
from time import sleep
import random

def scrape(link , prod_name , id_store , id_subcat):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en;q=0.9',
        'DNT' : '1',
        'Referer' : 'https://google.com'
    }
    s = requests.session()
    res = s.get("{}".format(link), headers=headers)

    #DB Connexion
    mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_datalake2",)

    mycursor = mydb.cursor()
    items = BS(res.text, features="html.parser")

    items_cards = items.findAll('li', {'class', 'item sale-product'})

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

        res = s.get(item_link, headers=headers)
        sleep(random.randint(1, 2))
        items = BS(res.text, features="html.parser")
        try:
            item_ref = (items.prettify().split('"sku":"')[1]).split('","description"')[0]
            item_ref = item_ref.replace('\/' , '/')
        except:
            print(f'NO REF FOUND IN {item_link}')
            continue

        items_details = items.find('div', {'class', 'product-tabs-content tabs-content std'})

        # print(f'item_ref = {item_ref}')
        # print("item_title = {}".format(item_title))
        print("item_link = {}".format(item_link))
        # print("item_price = {}".format(item_price))
        # print("stockage = {}".format(item_stockage))
        # print("item_color = {}".format(item_color))
        # print("scraped_at = {}".format(scraped_at))
        # print("image_item = {}".format(image_item))
        # print("item_screen_size = {}".format(item_screen_size))
        # print("item_connexion_adapter = {}".format(item_connexion_adapter))
        # print("item_garantie = {}".format(item_garantie))
        # print("prod_name= {}".format(prod_name))
        # print("item_ram= {}".format(item_ram))
        # print("item_stockage_type= {}".format(item_stockage_type))
        # print("item_lenght= {}".format(item_lenght))
        # print("item_power= {}".format(item_power))

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

            sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,unique_id) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
            val = ("", item_title, item_link, 1, id_subcat, jsonStringify, "", image_item,item_price, item_ref)
            mycursor.execute(sql, val)
            mydb.commit()
        except Exception as e:
            print(f'EXCEPTION {e}')
            continue

    mydb.close()


if __name__ == "__main__":
    for l in uno_iphones_links:
        scrape( "{}".format(l['link']), "{}".format(l['product_name']) ,l["id_store"] , l["subcategory"])
        sleep(random.randint(1,2))

    for l in uno_ipads_links:
        scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
        sleep(random.randint(1,2))

    for l in uno_mac_links:
        scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
        sleep(random.randint(1,2))

    for l in uno_watches_links:
        scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
        sleep(random.randint(1,2))

    for l in uno_tvs_links:
        scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
        sleep(random.randint(1,2))

    for l in uno_accessoires_links:
        scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
        sleep(random.randint(1,2))

    for l in uno_headphones_links:
        scrape("{}".format(l['link']), "{}".format(l['product_name']), l["id_store"], l["subcategory"])
        sleep(random.randint(1,2))