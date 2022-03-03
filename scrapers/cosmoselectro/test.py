import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random

# res = requests.get("https://www.cosmoselectro.ma/")
# new_page = BS(res.text, features="html.parser")
#
# h4s = new_page.findAll('h4')
#
# for i in h4s:
#     try:
#         print(i.find('a').get('href'))
#         print(i.find('a').get_text())
#         print("\n")
#     except:
#         pass

html = open('./a.html' , 'r' , encoding='utf8')
new_page = BS(html, features="html.parser")


def formatPrice(price):
    tmp = price.replace('Dhs' , '')
    tmp =tmp.split()
    floatprice = "".join(tmp)
    return float(floatprice)

def getImageSrc(tags):
    for tag in tags:
        try:
            src = tag.get('src')
        except:
            pass
        if 'https://www.cosmoselectro.ma/storage/products' in src:
            return src
    return None


item_name_in_store = new_page.select_one('#product-page > div.ps-container > div > div.ps-page--product > div > div.ps-page__container > div.ps-page__left > div > div.ps-product__header > div.ps-product__info > h1').get_text().strip()
item_price = new_page.select_one('#product-page > div.ps-container > div > div.ps-page--product > div > div.ps-page__container > div.ps-page__left > div > div.ps-product__header > div.ps-product__info > h4 > span').get_text().strip()
item_price = formatPrice(item_price)
item_description = new_page.select_one('#tab-description > div').get_text().strip()
item_ref = new_page.select_one('#product-sku').get_text().strip()
item_specification = new_page.select_one('#product-specs > tbody')
image_item = getImageSrc(new_page.findAll('img'))


print("item_name_in_store = {}".format(item_name_in_store))
print("item_price = {}".format(item_price))
print("item_description = {}".format(item_description))
print("item_ref = {}".format(item_ref))
print("item_specification = {}".format(item_specification))
print("image_item = {}".format(image_item))


