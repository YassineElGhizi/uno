import json
import logging
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random
import sys



def convertPrice(price):
    tmp = price.replace('MAD' , '')
    tmp = tmp.replace(',' , '.')
    tmp = tmp.split()
    return float("".join(tmp))

html = open('./a.html' , 'r' , encoding="utf8")

new_page = BS(html, features="html.parser")

item_name = new_page.select_one('#center_column > div.primary_block.row > div.pb-center-column.col-xs-12.col-sm-7.col-md-6 > h1').text.strip()
item_ref = new_page.select_one('#product_reference > span').text.strip()
item_price = new_page.select_one('#our_price_display').text.strip()
item_price = convertPrice(item_price)
item_description = new_page.select_one('#short_description_block').text.strip()
image_item = new_page.select_one('#bigpic').get('src')
try:
    item_specification = new_page.find('table')
except:
    item_specification = None

try:
    item_reviews = new_page.findAll('div' , {'class' : 'comment_details col-sm-10'})
except:
    item_reviews  = None


print(f"item_name = {item_name}")
print(f"item_ref = {item_ref}")
print(f"item_price = {item_price}")
print(f"item_description = {item_description}")
print(f"image_item = {image_item}")
print(f"item_specification = {item_specification}")
print(f"item_reviews = {item_reviews}")