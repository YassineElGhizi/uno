import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random


html = open('./a.html' , 'r' , encoding="utf8")

new_page = BS(html, features="html.parser")



def convertPrice(price):
    tmp = price.replace('MAD' , '')
    tmp = tmp.replace(',' , '.')
    tmp = tmp.split()
    return float("".join(tmp))

item_name = new_page.select_one('#page-columns > div > div.product-view.nested-container > div.product-primary-column.product-shop.grid12-5 > div.product-name > h1').text.strip()
item_description = new_page.select_one('#page-columns > div > div.product-view.nested-container > div.product-primary-column.product-shop.grid12-5 > div.short-description').text.strip()
item_price = new_page.find('span' , {'class' : 'price'}).text.strip()
item_price = convertPrice(item_price)
item_specification = new_page.select_one('#product-tabs > div')
image_item = new_page.select_one('#zoom1').get('href')


print(f"item_name = {item_name}")
print(f"item_description = {item_description}")
print(f"item_price = {item_price}")
print(f"item_specification = {item_specification}")
print(f"image_item = {image_item}")


