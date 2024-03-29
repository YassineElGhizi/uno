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
    in_site_category = i.findAll('a', {'class' : 'sm_megamenu_nodrop'})
    for x in in_site_category:
        children = x.findChildren("span",{'class': 'sm_megamenu_title_lv-3'}, recursive=False)
        for child in children:
            d = {}
            d["subcategory_in_site"] = child.get_text()
            d["link"] = x.get('href')
            list_of_subcats_and_thier_links.append(d)

def scrape():
    try:
        print("     [+] starting scrap()")
        for l in list_of_subcats_and_thier_links:
            s = requests.session()
            res = s.get("{}{}".format(l["link"], '?product_list_limit=36') , headers=headers)

            #DB Connexion
            mydb = pymysql.connect( host="127.0.0.1", port=3306, user="root", password="", database="supero_datalake2",)
            mycursor = mydb.cursor()

            items = BS(res.text, features="html.parser")
            items_cards = items.findAll("div", {"class": "product-item-info"})

            for num, ic in enumerate(items_cards):
                image_item = ic.find('img', {'class': 'product-image-photo'}).get('src')
                item_link = ic.find('a', {'class': 'product photo product-item-photo'}).get('href')
                try:
                    res2 = s.get(item_link, headers=headers)
                except:
                    continue
                sleep(random.randint(1, 2))
                new_page = BS(res2.text, features="html.parser")
                item_name_in_store = new_page.find('span' , {"class" : "base"}).get_text()
                tmp = new_page.find('div' , {'class' : 'product-info-price'})
                item_price = convert_item_price_to_double(tmp.find("span", {"class": "price"}).get_text())
                ttmp = tmp.find('div', {'class': 'product attribute sku'})
                item_ref = ttmp.find('div' , {'class':'value'}).get_text().strip()

                print(f'link: {item_link}')
                print("item_name_in_store = {}".format(item_name_in_store))
                print("item_price = {}".format(item_price))
                print("item_ref = {}".format(item_ref))
                tmp = new_page.findAll('div', {'class': 'additional-attributes-wrapper'})
                item_description = tmp[0].get_text()
                item_specification = tmp[1]
                # print("item_description = {}".format(item_description))
                # print("item_specification = {}".format(item_specification))
                print("image_item = {}".format(image_item))
                item_short_name = ''

                try:
                    myjson = dict()
                    if item_specification != None:
                        myjson['specification_table'] = item_specification

                    jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)
                    sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,unique_id) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                    val = (item_short_name, item_name_in_store, item_link, 4, l["subcategory_in_site"], jsonStringify, item_description, image_item, item_price,item_ref)
                    mycursor.execute(sql, val)
                    mydb.commit()
                except Exception as e:
                    print(e)
            mydb.close()
    except Exception as e:
        print(f'Exception detetcted {e} !')
        pass

if __name__ == "__main__":
    start = time.time()
    scrape()
    print(f'Finished in {time.time() - start} seconds')