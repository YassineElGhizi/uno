import json

import requests

import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import datetime
import random






html = open("./main.html" , 'r' , encoding="utf8")
items = BS(html, features="html.parser")

item_name = items.select_one('#content > div > div.range-revamp-page-container__inner > div > div.range-revamp-product__subgrid.product-pip.js-product-pip > div.range-revamp-product__buy-module-container > div > div.js-price-package.range-revamp-pip-price-package > div > div.range-revamp-pip-price-package__content-left > h1 > div.range-revamp-header-section__title--big.notranslate').get_text().strip()
item_price = items.select_one('#content > div > div.range-revamp-page-container__inner > div > div.range-revamp-product__subgrid.product-pip.js-product-pip > div.range-revamp-product__buy-module-container > div > div.js-price-package.range-revamp-pip-price-package > div > div.range-revamp-pip-price-package__price-wrapper > div > span > span.range-revamp-price__integer').get_text().strip()
item_details = items.select_one('#content > div > div.range-revamp-page-container__inner > div > div.range-revamp-product__subgrid.product-pip.js-product-pip > div.range-revamp-product__buy-module-container > div > div.js-price-package.range-revamp-pip-price-package > div > div.range-revamp-pip-price-package__content-left > h1 > div.range-revamp-header-section__description > span').get_text().strip()
image_item = items.select_one('#content > div > div.range-revamp-page-container__inner > div > div.range-revamp-product__subgrid.product-pip.js-product-pip > div.range-revamp-product__left-top > div > div.range-revamp-media-grid__grid > div:nth-child(1) > span > img').get('src')
items_description = items.select_one('#content > div > div.range-revamp-page-container__inner > div > div.range-revamp-product__subgrid.product-pip.js-product-pip > div.range-revamp-product__left-bottom > div.range-revamp-product-summary > p').get_text().strip()
item_ref = items.select_one('#content > div > div.range-revamp-page-container__inner > div > div.range-revamp-product__subgrid.product-pip.js-product-pip > div.range-revamp-product__left-bottom > div.range-revamp-product-summary > span > span.range-revamp-product-identifier__value').get_text().strip()


print("item_name = {}".format(item_name))
print("item_price = {}".format(item_price))
print("item_details = {}".format(item_details))
print("image_item = {}".format(image_item))
print("items_description = {}".format(items_description))
print("item_ref = {}".format(item_ref))
