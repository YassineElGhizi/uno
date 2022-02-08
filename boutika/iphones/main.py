import json

import pymysql
import requests
from bs4 import BeautifulSoup as BS
import datetime


res = requests.get("http://www.boutika.co.ma/3-telephones-portables-maroc")
html = res.text

print(html)