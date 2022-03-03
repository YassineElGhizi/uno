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
    tmp = price.replace(',' , '.')
    tmp = tmp.split()
    return float("".join(tmp))


item_name = new_page.select_one('#content > div.row > div:nth-child(2) > h1').get_text().strip()
item_model = new_page.select_one('#content > div.row > div:nth-child(2) > ul:nth-child(3) > li:nth-child(1)').get_text().strip().replace('Modèle :' , '')
item_price = new_page.select_one('#content > div.row > div:nth-child(2) > ul:nth-child(4) > li:nth-child(1) > h2').get_text().strip()
item_description = new_page.select_one('#content > div.row > div:nth-child(1)').get_text().strip()
image_item = new_page.select_one('#content > div.row > div:nth-child(1) > ul.thumbnails > li > a > img').get('src')
print("item_name = {}".format(item_name))
print("item_model = {}".format(item_model))
print("item_price = {}".format( convertPrice(item_price) ))
print("item_description = {}".format(item_description))
print("image_item = {}".format(image_item))