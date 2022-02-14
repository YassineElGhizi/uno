import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from global_parametrs import *
from time import sleep

list_of_subcats_and_thier_links = list()
res = requests.get("https://www.kitea.com/")
items = BS(
    res.text,
    features="html.parser"
)
all_categories_toscrape = items.findAll('div' , {'class' : 'sm-megamenu-child sm_megamenu_dropdown_6columns'})
for i in all_categories_toscrape:
    in_site_category = i.findAll('a' , {'class' : 'sm_megamenu_nodrop'})
    for x in in_site_category:
        children = x.findChildren("span" ,{'class' : 'sm_megamenu_title_lv-3'}, recursive=False)
        for child in children:
            d = {}
            d["subcategory_in_site"] = child.get_text()
            d["link"] = x.get('href')
            list_of_subcats_and_thier_links.append(d)

print("list_of_subcats_and_thier_links = {}".format(list_of_subcats_and_thier_links))

def scrape():
    try:
        for l in list_of_subcats_and_thier_links :
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
            items_cards = items.findAll("div", {"class": "product-item-info"})

            for num, ic in enumerate(items_cards):
                item_link = ic.find('a' , {'class' : 'product photo product-item-photo'}).get('href')
                res2 = requests.get(item_link)
                sleep(5)
                html2 = res2.text
                new_page = BS(
                    html2,
                    features="html.parser"
                )


                item_name_instore = new_page.find('span' , {"class" : "base"}).get_text()
                tmp = new_page.find('div' , {'class' : 'product-info-price'})
                item_price = convert_item_price_to_double(
                    tmp.find("span", {"class": "price"}).get_text()
                )
                item_ref = tmp.find("div", {"class": "value"}).get_text()
                print("item_name_instore = {}".format(item_name_instore))
                print("item_price = {}".format(item_price))
                print("item_ref = {}".format(item_ref))
                tmp = new_page.findAll('div' , {'class' : 'additional-attributes-wrapper'})
                item_description = tmp[0].get_text()
                item_specification = tmp[1]
                print("item_description = {}".format(item_description))
                print("item_specification = {}".format(item_specification))
                quit()



                print("================{}============".format(num+1))
                # print("item_brand = {}".format(item_brand))
                print("item_ref = {}".format(item_ref))
                print("item_price = {}".format(item_price))
                # print("item_name = {}".format(item_name))
                print("item_link = {}".format(item_link))
                # print("image_item = {}".format(image_item))
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
                        # sql = "INSERT INTO items (name ,name_in_store,link, id_store ,id_subcategory ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                        sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                        # val = (item_name, item_ref, item_link, id_store, id_subcat, jsonStringify, "", image_item, item_price,scraped_at)
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
                            # val = (item_price , scraped_at , item_name)
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
    #Uno Iphone
    scrape()