import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import random

list_of_cats_and_thier_links = list()
list_of_subcats_and_thier_links = list()
scrapped_links = []

main_categories = [
    'https://www.bestmark.ma/tous-nos-produits/telephonie-et-tablettes/telephonie-portable.html',
    'https://www.bestmark.ma/tous-nos-produits/telephonie-et-tablettes/tablette.html',
    'https://www.bestmark.ma/tous-nos-produits/telephonie-et-tablettes/accessoires.html',
    'https://www.bestmark.ma/tous-nos-produits/ordinateur-bureau/pc-bureau.html',
    'https://www.bestmark.ma/tous-nos-produits/ordinateur-bureau/peripheriques-et-composants.html',
    'https://www.bestmark.ma/tous-nos-produits/ordinateur-bureau/logiciels-reseau.html',
    'https://www.bestmark.ma/tous-nos-produits/ordinateur-portable.html',
    'https://www.bestmark.ma/tous-nos-produits/ordinateur-portable/pc-portable.html',
    'https://www.bestmark.ma/tous-nos-produits/ordinateur-portable/accessoires-pc-portable.html',
    'https://www.bestmark.ma/tous-nos-produits/apple/macbook.html',
    'https://www.bestmark.ma/tous-nos-produits/apple/ipad.html',
    'https://www.bestmark.ma/tous-nos-produits/apple/accessoires.html',
    'https://www.bestmark.ma/tous-nos-produits/apple/imac.html',
    'https://www.bestmark.ma/tous-nos-produits/tendance-hi-tech/image.html',
    'https://www.bestmark.ma/tous-nos-produits/tendance-hi-tech/mobilite.html',
    'https://www.bestmark.ma/tous-nos-produits/tendance-hi-tech/accessoires.html',
    'https://www.bestmark.ma/tous-nos-produits/tendance-hi-tech/univers-3d.html',
    'https://www.bestmark.ma/tous-nos-produits/gaming/console-de-jeux.html',
    'https://www.bestmark.ma/tous-nos-produits/gaming/gaming-pc.html',
    'https://www.bestmark.ma/tous-nos-produits/gaming/accessoires-gaming.html',
    'https://www.bestmark.ma/tous-nos-produits/gaming/jeux-videos.html',
    'https://www.bestmark.ma/tous-nos-produits/imprimante-et-consommable/imprimante-et-copieur.html',
    'https://www.bestmark.ma/tous-nos-produits/imprimante-et-consommable/scanner-et-traceur.html',
    'https://www.bestmark.ma/tous-nos-produits/imprimante-et-consommable/consommables.html',
    'https://www.bestmark.ma/tous-nos-produits/image-et-son/tv.html',
    'https://www.bestmark.ma/tous-nos-produits/image-et-son/video-projecteur.html',
    'bestmark.ma/tous-nos-produits/image-et-son/photo-et-video.html',
    'https://www.bestmark.ma/tous-nos-produits/image-et-son/son.html',
    'https://www.bestmark.ma/tous-nos-produits/image-et-son/accessoires-photo-et-video.html',
    'https://www.bestmark.ma/tous-nos-produits/accessoires/ordinateur.html',
    'https://www.bestmark.ma/tous-nos-produits/accessoires/telephonie.html',
    'https://www.bestmark.ma/tous-nos-produits/accessoires/image-et-son.html',
    'https://www.bestmark.ma/tous-nos-produits/accessoires/stockage-et-sauvegarde.html',
    'https://www.bestmark.ma/tous-nos-produits/accessoires/apple.html',
    'https://www.bestmark.ma/tous-nos-produits/logiciels-reseau/logiciels.html',
    'https://www.bestmark.ma/tous-nos-produits/logiciels-reseau/reseau.html',
    'bestmark.ma/tous-nos-produits/offres-nouveautes.html',
]


def convertPrice(price):
    tmp = price.replace(' DH', '')
    tmp = tmp.replace(',', '.')
    tmp = tmp.replace(' ', '')
    return float("".join(tmp))

def init():
    print("[+] Initilialisation")
    res = requests.get("https://www.bestmark.ma/")
    items = BS(res.text, features="html.parser")
    uls = items.findAll('div', {'class': 'sm_megamenu_title'})
    for ul in uls:
        a_tags = ul.findAll('a')
        for a in a_tags:
            d = {}
            d["link"] = f"https://www.bestmark.ma{a.get('href')}"
            if d["link"] not in main_categories:
                d["name_sub_cat"] = a.get_text().strip()
                if d not in list_of_subcats_and_thier_links and d["name_sub_cat"] != '':
                    list_of_subcats_and_thier_links.append(d)

def scrape():
    try:
        init()
        mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_datalake2",)
        mycursor = mydb.cursor()
        print("         [+] Scraping Items")
        for item in list_of_subcats_and_thier_links:
            s = requests.session()
            res2 = s.get("{}?product_list_limit=30".format(item["link"]))
            new_page2 = BS(res2.text,features="html.parser")
            sleep(random.randint(0 , 1))
            cards = new_page2.findAll('a', {'class': 'product photo product-item-photo'})
            mylist = []
            for card in cards:
                try:
                    mylist.append(card.get('href'))
                except:
                    pass

            print("             [+] Collecting data")
            for num, link in enumerate(mylist):
                res2 = s.get(link)
                sleep(random.randint(0 , 1))
                new_page = BS(res2.text,features="html.parser")

                metas = new_page.findAll('meta')
                image_item = None
                for m in metas:
                    try:
                        if '.jpg' in m.get('content'):
                            image_item = m.get('content')
                    except:
                        pass
                if link in scrapped_links:
                    print(link, 'already got scraped')
                    continue

                try:
                    scrapped_links.append(link)
                    item_name_in_store = new_page.find('h1', {'class' : 'page-title'}).get_text().strip()
                    try:
                        item_description = new_page.find('div', {'class': 'product attribute overview'}).get_text().strip()
                    except:
                        pass
                    item_link = link
                    item_price = new_page.find('span' , {'class': 'price'}).get_text().strip()
                    item_price = convertPrice(item_price)
                    item_short_name = ''

                    try:
                        item_specification = new_page.find('table', {'class': 'data table additional-attributes'})
                    except:
                        item_specification = None
                        continue


                    try:
                        trs = item_specification.findAll('tr')
                        for z in trs:
                            key = z.findAll('th')[0].get_text().strip()
                            ref = z.findAll('td')[0].get_text().strip()
                            if key == 'Référence':
                                item_ref = ref
                    except:
                        continue



                    # print("item_name_in_store = {}".format(item_name_in_store))
                    # print("item_ref = {}".format(item_ref))
                    # print("item_description = {}".format(item_description))
                    # print("item_specification = {}".format(item_specification))
                    # print("image_item = {}".format(image_item))
                    # print("item_price = {}".format(item_price))
                    print("item_subcat_in_website = {}".format(item['name_sub_cat']))
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
                    val = (item_short_name, item_name_in_store,  item_link, 11, item['name_sub_cat'], jsonStringify, item_description, image_item, item_price,item_ref)
                    mycursor.execute(sql, val)
                    mydb.commit()
                except Exception as e:
                    print(f'Exeption {e}')
                    pass
    except Exception as e:
        print(f'Ecpetion {e}')
        pass


if __name__ == "__main__":
    scrape()