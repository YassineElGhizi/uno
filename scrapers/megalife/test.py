import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random


# res = requests.get("https://megalife.ma/")
# new_page = BS(res.text, features="html.parser")

html = open('./a.html' , 'r' , encoding="utf8")
new_page = BS(html, features="html.parser")

item_name_in_store = new_page.find('h1' , {'class' : 'product_title wd-entities-title'}).get_text().strip()
item_price = new_page.find('p' , {'class' : 'price'}).get_text().strip()
numbers = [word for word in item_price.split() if word.isdigit()]
item_price = "".join(numbers)
item_description = new_page.find('div' , {'class' : 'woocommerce-product-details__short-description'}).get_text().strip()
item_specification = new_page.find('table' , {'class' : 'woocommerce-product-attributes shop_attributes'})
image_item = new_page.find('figure' , {'class' : 'woocommerce-product-gallery__image'})
image_item = image_item.find('a').get('href')

print("item_name_in_store = {}".format(item_name_in_store))
print("item_price  = {}".format(item_price ))
print("item_description = {}".format(item_description))
print("item_specification = {}".format(item_specification))
print("image_item = {}".format(image_item))
