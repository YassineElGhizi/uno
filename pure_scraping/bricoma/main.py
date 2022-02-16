import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random

list_of_cats_and_thier_links = list()
list_of_subcats_and_thier_links = list()
now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

def init():
    print("[+] Initialisation")
    res = requests.get("https://www.bricoma.ma/")
    items = BS(
        res.text,
        features="html.parser"
    )
    all_categories_toscrape = items.findAll('a' , {'class' : 'level-top'})
    for i in all_categories_toscrape:
        d = dict()
        d["link"] = i.get('href')
        d["category_in_site"] = i.find('span').get_text().strip()
        list_of_cats_and_thier_links.append(d)


def scrape():
    try:
        init()
    except Exception as e:
        print("Err in init() BRICOMA")
        print(e)
        return -1

    try:
        print("[+] Getting categories")
        for l in list_of_cats_and_thier_links :
            res = requests.get("{}".format(l["link"]))
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
            subcats = items.findAll('a' , {'class' : 'category-name'})
            print("     [+] Getting SubCategries")
            for s in subcats:
                dd = dict()
                dd["link"] = s.get('href')
                dd["subcategory_in_site"] = s.get_text().strip()
                list_of_subcats_and_thier_links.append(dd)

            print("         [+] Scraping Items")
            for item in list_of_subcats_and_thier_links:
                res2 = requests.get("{}{}".format(item["link"] ,"?product_list_limit=32"))
                sleep(random.randint(4 , 7))
                html2 = res2.text
                new_page2 = BS(
                    html2,
                    features="html.parser"
                )
                items_cards = new_page2.findAll('div' , {'class' : 'actions-primary'})
                mylist = list()
                for ihref in items_cards:
                    mylist.append(
                        ihref.find('a').get('href')
                    )
            print("             [+] Collecting data")
            for num, link in enumerate(mylist):
                res2 = requests.get(link)
                sleep(random.randint(4 , 7))
                html2 = res2.text
                new_page = BS(
                    html2,
                    features="html.parser"
                )

                item_name_instore = new_page.select_one(
                    '#maincontent > div.columns > div > div.product-info-main > div.page-title-wrapper.product > h1 > span'
                ).get_text()
                item_ref = new_page.select_one(
                    '#maincontent > div.columns > div > div.product-info-main > div.product-header-info > div > div'
                ).get_text()
                item_description = new_page.select_one(
                    '#maincontent > div.columns > div > div.product-info-main > div.product.attribute.overview > div >p'
                )
                item_specification = new_page.select_one('#product-attribute-specs-table > tbody')
                item_link = link
                image_item = new_page.find('img', {'class': 'gallery-placeholder__image'}).get('src')
                price = new_page.find('span' , {'data-price-type' : 'finalPrice'})
                price = price.find('span').get_text()
                price = price.replace('MAD', '')
                price = price.replace(',', '.')
                tmp = price.split()
                floatprice = "".join(tmp)
                tmp = float(floatprice)
                item_price = tmp

                print("item_name_instore = {}".format(item_name_instore))
                print("item_ref = {}".format(item_ref))
                print("item_description = {}".format(item_description))
                print("item_specification = {}".format(item_specification))
                print("item_link = {}".format(item_link))
                print("image_item = {}".format(image_item))
                print("item_price = {}".format(item_price))
                print("item_subcat_in_website = {}".format(item["subcategory_in_site"]))
                print("\n")

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
                        val = (item_name_instore, item_ref, item_link, 5, item["subcategory_in_site"], jsonStringify, item_description, image_item, item_price,scraped_at)
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
                    print(e.__traceback__.tb_lineno)
                    print(__file__)
                    print("Database conn error !")
                    pass

            mydb.close()
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_lineno)
        print(__file__)
        pass
    finally:
        mydb.close()


if __name__ == "__main__":
    scrape()