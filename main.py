import requests
from bs4 import BeautifulSoup as BS
from time import sleep

# FITS PART
cards_links = list()
items = BS(
    requests.get('https://uno.ma/iphone-maroc/').text ,
    features="html.parser"
)

all_tags = items.findAll('a' , {'class' ,'toggle-list' } )
for card in all_tags:
    tmp = BS( str(card) , features="html.parser")
    try:
        link = tmp.find('a')['href']
        cards_links.append(link)
    except:
        pass

#Second part
stockage_list = ['128 Gb','256 Gb','512 Gb','1 Tb' ]
def check_stockage(mystr):
    for i in stockage_list:
        if i in mystr:
            return i
        return 0

for card_link in cards_links:
    items = BS(
        requests.get(str(card_link)).text,
        features="html.parser"
    )

    target_item = items.findAll('h2' , {'class' , 'product-name'})
    for i in target_item:
        tmp = BS( str(i) , features="html.parser" )
        lien = tmp.find('a')['href']
        print(
            lien
        )
        print(
            tmp.text
        )
        stockage = check_stockage(tmp.text)
        print(
            stockage
        )
        try:
            color = ((tmp.text).split(stockage)[-1]).split('(')[0].strip()
        except:
            color = 0
        print(color)

        details_item_page = BS(
            requests.get(str(lien)).text,
            features="html.parser"
        )
        price = details_item_page.find('span' , {'class' , 'price'}).text
        print(
            price.strip()
        )

        quit()
