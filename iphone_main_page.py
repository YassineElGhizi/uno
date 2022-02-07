import pymysql
import requests
from bs4 import BeautifulSoup as BS
import datetime



#Global Varibales
all_iphones_list = list()


res = requests.get("https://uno.ma/iphone-maroc")
html = res.text

items = BS(
    html ,
    features="html.parser"
)

if __name__ == "__main__":
    items_cards = items.find('ul' , {'class' ,'list-cat' })
    for ic in items_cards.children:
        if ic.get_text() != "\n":
            all_iphones_dict = dict()
            item_name_main_page = ic.find('p', {'class', 'cat-name'}).get_text()
            item_link_main_page = ic.find('a', {'class', 'cat-link'}).get('href')
            all_iphones_dict['name'] = item_name_main_page
            all_iphones_dict['link'] = item_link_main_page
            all_iphones_list.append(
                all_iphones_dict
            )

    print(all_iphones_list)


