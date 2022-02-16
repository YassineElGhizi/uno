import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random

list_of_subcats_and_thier_links = list()
now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

def init():
    print("[+] Initialisation")
    res = requests.get("https://www.decathlon.ma/")
    items = BS(
        res.text,
        features="html.parser"
    )
    subcats = items.findAll('div', {'class': 'title'})

    for num, tag in enumerate(subcats):
        if num == 0:
            continue
        d = dict()
        tmp = tag.findChildren("a", recursive=False)
        for t in tmp:
            d["link"] = t.get('href')
            d["subcategory"] = t.get_text().strip()
            list_of_subcats_and_thier_links.append(d)

    # print(list_of_subcats_and_thier_links)



def scrape():
    try:
        init()
    except Exception as e:
        print("Err in init() Decathlon API")
        print(e)
        return -1

    try:
        # DB Connexion
        mydb = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="datalake",
        )
        mycursor = mydb.cursor()

        for item in list_of_subcats_and_thier_links:
            print("         [+] Preparing Request")
            numer_cat = item["link"].split('.ma/')[-1]
            numer_cat = numer_cat.split('-')[0]
            payload = {"requests": [{"indexName": "decathlon_prod_fr",
                                     "params": "ruleContexts=%5B%22category_3712%22%5D&clickAnalytics=true&distinct=true&filters=category%20%3D%20" + numer_cat + "&highlightPreTag=__ais-highlight__&highlightPostTag=__%2Fais-highlight__&page=0&maxValuesPerFacet=20&facets=%5B%22nature%22%2C%22practices%22%2C%22genders%22%2C%22generic_color%22%2C%22size%22%2C%22brand%22%2C%22available%22%2C%22sale%22%5D&tagFilters="}]}
            jsonStringify = json.dumps(payload, indent=4, sort_keys=True, default=str)
            sleep(random.randint(4,7))
            res = requests.post(
                "https://4kcwynnd8n-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.32.0;JS Helper (3.4.4);instantsearch.js (4.10.0);JS Helper (3.3.4)&x-algolia-application-id=4KCWYNND8N&x-algolia-api-key=105e997d8f51e3fd2bd8dd5ee7b03366"
                , headers={"Content-Type": "application/json"}
                , data=jsonStringify
                )
            json_data = json.loads(res.text)
            items = json_data["results"][0]
            print("             [+] Scraping items")
            for num, i in enumerate(items["hits"]) :
                item_brand = i["brand"]
                item_genders = i["genders"]
                item_ref = i["id_code_model"]
                image_item = i["image_url"]
                item_description = i["made_for"]
                item_price = i["prix"]
                item_name_instore = i["product_name"]
                item_teaser = i["teaser"]
                item_link = i["url"]
                item_specification = i["_highlightResult"]
                print("brand = {}".format(i["brand"])  )
                print("genders = {}".format(i["genders"])  )
                print("id_code_model = {}".format(i["id_code_model"])  )
                print("image_url = {}".format(i["image_url"])  )
                print("made_for = {}".format(i["made_for"])  )
                print("objectID = {}".format(i["objectID"])  )
                print("prix = {}".format(i["prix"])  )
                print("product_name = {}".format(i["product_name"])  )
                print("teaser = {}".format(i["teaser"])  )
                print("url = {}".format(i["url"])  )
                print("_highlightResult = {}".format(i["_highlightResult"])  )
                print("=============================={}============================".format(num+1))
                print("\n")

                try:
                    myjson = dict()
                    if item_specification != None:
                        myjson['specification_table'] = item_specification
                        myjson['item_brand'] =  item_brand
                        myjson['item_genders'] =  item_genders
                        myjson['item_teaser'] =  item_teaser
                    jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)

                    sql = "select current_price from items where name_in_store = %s"
                    val = (item_ref)
                    mycursor.execute(sql, val)
                    myresult = mycursor.fetchall()
                    if(len(myresult) == 0):
                        sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                        val = (item_name_instore, item_ref, item_link, 6, item["subcategory"], jsonStringify, item_description, image_item, item_price,scraped_at)
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
