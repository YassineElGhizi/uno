import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import random

big_parents = []
scrapped_links = []

def convertPrice(price):
    tmp = price.replace(' DH' , '')
    return float("".join(tmp))

def init():
    print("[+] Initilialisation")
    s = requests.session()
    res = s.get("https://saligon.com/")
    items = BS(res.text, features="html.parser")
    a_tags = items.findAll('a', {'class': 'vertical-nav__link'})
    for a in a_tags:
        try:
            big_parents.append(a.get('href'))
        except:
            pass


def scrape():
    try:
        init()
        mydb = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="supero_datalake2",)
        mycursor = mydb.cursor()
        print("         [+] Scraping Items")
        for link in big_parents:
            s = requests.session()
            res2 = s.get("{}".format(link))
            new_page2 = BS(res2.text, features="html.parser")
            sleep(random.randint(0, 1))
            cards = new_page2.findAll('div', {'class': 'product-loop-title'})
            links_onyl = []
            for c in cards:
                links_onyl.append(c.find('a').get('href'))

            print("             [+] Collecting data")
            for link in links_onyl:
                res2 = s.get(link)
                sleep(random.randint(0 , 1))
                new_page = BS(res2.text, features="html.parser")

                if link in scrapped_links:
                    print(link, 'already got scraped')
                    continue

                try:
                    scrapped_links.append(link)
                    item_name_in_store = new_page.select_one('#main > div.pc-product-single__summary-wrapper > div.pc-product-single__summary > div > div.pc-product-summary__header > h1').text.strip()
                    try:
                        item_description = new_page.select_one('#main > div.pc-product-single__summary-wrapper > div.pc-product-single__summary > div > div.pc-product-summary__footer > div.short-description.typo.typo--small').text.strip()
                    except:
                        item_description = None
                        pass
                    item_link = link
                    image_item = None
                    item_price = new_page.select_one('#main > div.pc-product-single__summary-wrapper > div.pc-product-single__summary > div > div.pc-product-summary__body > div > div.pc-product-purchase__header > div > span').text.strip()
                    item_price = convertPrice(item_price)
                    item_short_name = ''

                    try:
                        item_specification = new_page.find('div', {'class': 'attributes-table shop_attributes'})
                    except:
                        item_specification = None

                    item_ref = new_page.select_one('#main > div.pc-product-single__summary-wrapper > div.pc-product-single__summary > div > div.pc-product-summary__header > div > span > span').text.strip()
                    item_subcat_in_website =new_page.select_one('#main > div.pc-product-single__summary-wrapper > div.pc-product-single__summary > div > div.pc-product-summary__header > div > div > span > a').text.strip()


                    # print(f'item_name_in_store = {item_name_in_store}')
                    # print(f'item_description = {item_description}')
                    print(f'item_link = {item_link}')
                    # print(f'image_item = {image_item}')
                    # print(f'item_price = {item_price}')
                    # print(f'item_specification = {item_specification}')
                    # print(f'item_ref = {item_ref}')
                    print(f'item_subcat_in_website = {item_subcat_in_website}')
                    print("\n")
                except Exception as e:
                    print(e)
                    print(e.__traceback__.tb_lineno)
                    continue
                try:
                    myjson = dict()
                    if item_specification != None:
                        myjson['specification_table'] = item_specification
                    jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)
                    sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,unique_id) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                    val = (item_short_name, item_name_in_store,  item_link, 12, item_subcat_in_website, jsonStringify, item_description, image_item, item_price,item_ref)
                    mycursor.execute(sql, val)
                    mydb.commit()
                except Exception as e:
                    print(f'Exeption {e}')
                    pass
    except Exception as e:
        print(f'Exception {e}')
        pass


if __name__ == "__main__":
    scrape()



