import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
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


list_of_cats_and_thier_links = list()
list_of_subcats_and_thier_links = list()
now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
list_of_cats_and_thier_links.append({"name" : "Meubles" , "link" : "https://www.ikea.com/ma/fr/cat/meubles-fu001/"})
list_of_cats_and_thier_links.append({"name" : "Cuisine et électroménager" , "link" : "https://www.ikea.com/ma/fr/cat/cuisine-et-electromenager-ka001/"})
list_of_cats_and_thier_links.append({"name" : "Lits et matelas" , "link" : "https://www.ikea.com/ma/fr/cat/lits-et-matelas-bm001/"})
list_of_cats_and_thier_links.append({"name" : "Rangement" , "link" : "https://www.ikea.com/ma/fr/cat/rangement-st001/"})
list_of_cats_and_thier_links.append({"name" : "Travailler de la maison" , "link" : "https://www.ikea.com/ma/fr/cat/travailler-de-la-maison-700291/"})
list_of_cats_and_thier_links.append({"name" : "Linge de maison et textile" , "link" : "https://www.ikea.com/ma/fr/cat/linge-de-maison-et-textile-tl001/"})
list_of_cats_and_thier_links.append({"name" : "Décoration" , "link" : "https://www.ikea.com/ma/fr/cat/decoration-de001/"})
list_of_cats_and_thier_links.append({"name" : "Salle de bain" , "link" : "https://www.ikea.com/ma/fr/cat/salle-de-bain-ba001/"})
list_of_cats_and_thier_links.append({"name" : "Mobilier et accessoires d'extérieur" , "link" : "https://www.ikea.com/ma/fr/cat/mobilier-et-accessoires-dexterieur-od001/"})
list_of_cats_and_thier_links.append({"name" : "Luminaires et éclairage" , "link" : "https://www.ikea.com/ma/fr/cat/luminaires-et-eclairage-li001/"})
list_of_cats_and_thier_links.append({"name" : "Tapis et paillasson" , "link" : "https://www.ikea.com/ma/fr/cat/tapis-et-paillasson-rm001/"})
list_of_cats_and_thier_links.append({"name" : "Bébé et enfant" , "link" : "https://www.ikea.com/ma/fr/cat/bebe-et-enfant-bc001/"})


def scrape():
    try:
        mydb = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="supero_datalake2",
        )
        mycursor = mydb.cursor()
        s = requests.session()

        print("[+] Getting subCategories")
        for l in list_of_cats_and_thier_links :
            print(l['name'])
            res = s.get("{}".format(l["link"]), headers=headers)
            items = BS(res.text,features="html.parser")
            links = items.findAll('a', {'class': 'vn-link vn__nav__link vn-6-grid-gap'})
            for link in links:
                d = dict()
                d["link"] = link.get('href')
                d["name"] = link.get_text().strip()
                list_of_subcats_and_thier_links.append(d)

            print("         [+] Scraping Items")
            for item in list_of_subcats_and_thier_links:

                res2 = s.get("{}".format(item["link"]), headers=headers)
                sleep(random.randint(0 , 1))
                new_page2 = BS(res2.text,features="html.parser")

                items_cards = new_page2.findAll('a' , {'class' : 'pip-product-compact__wrapper-link'})
                mylist = list()
                for ihref in items_cards:
                    try:
                        mylist.append(ihref.get('href'))
                    except:
                        pass

                print(f"             [+] Collecting data from {len(mylist)} Items")
                for num, link in enumerate(mylist):
                    res2 = s.get(link, headers=headers)
                    sleep(random.randint(0 , 1))
                    new_page = BS(res2.text,features="html.parser")
                    try:
                        item_name_instore = new_page.select_one(
                            '#content > div > div.pip-page-container__inner > div > div.pip-product__subgrid.product-pip.js-product-pip > div.pip-product__buy-module-container > div > div.js-price-package.pip-pip-price-package > div > div.pip-pip-price-package__content-left > h1 > span.pip-header-section__title--big.notranslate'
                        ).get_text().strip()

                        item_ref = new_page.select_one(
                            '#content > div > div.pip-page-container__inner > div > div.pip-product__subgrid.product-pip.js-product-pip > div.pip-product__buy-module-container > div > div.js-price-package.pip-pip-price-package > div > div.pip-pip-price-package__content-left > h1 > span.pip-header-section__description'
                        ).get_text().strip()

                        item_description = new_page.select_one(
                            '#content > div > div.pip-page-container__inner > div > div.pip-product__subgrid.product-pip.js-product-pip > div.pip-product__left-bottom > div.pip-product-summary > p'
                        ).get_text().strip()

                        item_specification = new_page.select_one(
                            '#content > div > div.pip-page-container__inner > div > div.pip-product__subgrid.product-pip.js-product-pip > div.pip-product__buy-module-container > div > div.js-price-package.pip-pip-price-package > div > div.pip-pip-price-package__content-left > h1 > span.pip-header-section__description'
                        ).get_text().strip()
                        item_link = link

                        image_item = new_page.select_one(
                            '#content > div > div > div > div.pip-product__subgrid.product-pip.js-product-pip > div.pip-product__left-top > div > div.pip-media-grid__grid > div:nth-child(3) > button > span > img'
                        ).get('src')

                        item_price = new_page.select_one(
                            '#content > div > div > div > div.pip-product__subgrid.product-pip.js-product-pip > div.pip-product__buy-module-container > div > div.js-price-package.pip-pip-price-package > div > div.pip-pip-price-package__price-wrapper > div > span > span.pip-price__integer'
                        ).get_text().strip()
                        tmp = item_price.split()
                        floatprice = "".join(tmp)
                        item_price = float(floatprice)

                        # print("item_name_instore = {}".format(item_name_instore))
                        # print("item_ref = {}".format(item_ref))
                        # print("item_description = {}".format(item_description))
                        # print("item_specification = {}".format(item_specification))
                        # print("item_link = {}".format(item_link))
                        # print("image_item = {}".format(image_item))
                        # print("item_price = {}".format(item_price))
                        # print("item_subcat_in_website = {}".format(item["name"]))
                        # print("\n")
                    except Exception as e:
                        print("something wroing in html parsing")
                        print(e)
                        print(e.__traceback__.tb_lineno)
                        print(__file__)
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
                            val = (item_name_instore, item_ref, item_link, 7, item["name"], jsonStringify, item_description, image_item, item_price,scraped_at)
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
                        print(e)
                        print(e.__traceback__.tb_lineno)
                        print(__file__)
                        print("Database conn error !")
                        pass

    except Exception as e:
        print(e)
        print(e.__traceback__.tb_lineno)
        print(__file__)
        pass


if __name__ == "__main__":
    scrape()