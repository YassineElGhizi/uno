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

def convertPrice(price):
    tmp = price.replace('MAD' , '')
    tmp = tmp.replace(',' , '.')
    tmp = tmp.split()
    return float("".join(tmp))

def init():
    print("[+] Initilialisation")
    res = requests.get("http://www.prixmaroc.ma/index.php?route=common/home")
    items = BS(res.text, features="html.parser")
    ul = items.findAll('ul' , {'class' : 'list-unstyled'})
    for tag in ul:
        lis = tag.findAll('a')
        for l in lis:
            try:
                link = l.get('href').replace('&amp;' , '')
                if '/category' in link:
                    d = dict()
                    d["link"] = link+"&limit=100"
                    d["name_sub_cat"] = l.get_text().strip()
                    list_of_subcats_and_thier_links.append(d)
            except:
                pass

def scrape():
    try:
        init()
        mydb = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="datalake",
        )
        mycursor = mydb.cursor()

        print("         [+] Scraping Items")
        for item in list_of_subcats_and_thier_links:
            res2 = requests.get("{}".format(item["link"]))
            sleep(random.randint(4 , 7))
            new_page2 = BS(res2.text,features="html.parser")
            divs = new_page2.select_one('#content > div:nth-child(7)')
            mylist = []
            for x in divs:
                try:
                    link = x.find('a').get('href').replace('&amp;', '')
                    mylist.append(link)
                except:
                    pass
            print("             [+] Collecting data")
            for num, link in enumerate(mylist):
                res2 = requests.get(link)
                sleep(random.randint(4 , 7))
                new_page = BS(res2.text,features="html.parser")

                try:
                    item_name_instore = new_page.select_one('#content > div.row > div:nth-child(2) > h1').get_text().strip()
                    item_ref = "Prixmaroc-{}".format(item_name_instore)
                    item_description = new_page.select_one('#content > div.row > div:nth-child(1)').get_text().strip()
                    if item_description != None:
                        item_specification = item_description
                    else:
                        item_specification = None
                    item_link = link
                    image_item = new_page.select_one('#content > div.row > div:nth-child(1) > ul.thumbnails > li > a > img').get('src')

                    item_price = new_page.select_one('#content > div.row > div:nth-child(2) > ul:nth-child(4) > li:nth-child(1) > h2').get_text().strip()
                    item_price = convertPrice(item_price)

                    print("item_name_instore = {}".format(item_name_instore))
                    print("item_ref = {}".format(item_ref))
                    print("item_description = {}".format(item_description))
                    print("item_specification = {}".format(item_specification))
                    print("item_link = {}".format(item_link))
                    print("image_item = {}".format(image_item))
                    print("item_price = {}".format(item_price))
                    print("item_subcat_in_website = {}".format(item["name_sub_cat"]))
                    print("\n")
                except Exception as e:
                    print("something went wrong in parsing html")
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
                        val = (item_name_instore, item_ref, item_link, 11, item["name_sub_cat"], jsonStringify, item_description, image_item, item_price,scraped_at)
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
                    pass
        try:
            mydb.close()
        except:
            pass
    except:
        pass
    finally:
        mydb.close()


if __name__ == "__main__":
    scrape()