import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import random

list_of_cats_and_thier_links = list()
list_of_subcats_and_thier_links = list()

def scrapped_ones():
    # DB Connexion
    mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_datalake2",)
    mycursor = mydb.cursor()
    sql = "select link from items where id_store = 10"
    mycursor.execute(sql, )
    scrapped_one = mycursor.fetchall()
    scrapped_one = [i[0] for i in scrapped_one]
    return scrapped_one

def convertPrice(price):
    tmp = price.replace('MAD', '')
    tmp = tmp.replace(',', '.')
    tmp = tmp.split()
    return float("".join(tmp))

def init():
    print("[+] Initilialisation")
    res = requests.get("https://istyle.ma/")
    items = BS(res.text, features="html.parser")
    uls = items.findAll('a' , {'class' : 'nav-category-link'})
    [print(a.get_text().strip(), a.get('href')) for a in uls]
    quit()
    for ul in uls:
        for li in ul.findAll('a'):
            titlestr = li.text.strip()
            if len(titlestr) < 30:
                if titlestr not in ["", "Ajouter au panier", "Imprimante & Scanner", "Imprimante", "Scanner", "Consommables", "Ordinateur portable", "Accessoires & composants", "Ordinateur fixe", "Logiciel", "Tablette tactile, Ipad", "Onduleur", "Stockage" , "Souris" , "Clavier" , "Pack Clavier/Souris" , "Vidéoprojecteur" , "Écran de projection" , "Appareil photo numérique" , "Haut-parleur" , "Switch" , "Serveur" , "Détails" , "Aperçu rapide"] :
                    d = dict()
                    d["link"] = li.get('href')
                    d["name_sub_cat"] = titlestr
                    list_of_subcats_and_thier_links.append(d)

def scrape():
    try:
        init()
        quit()
        scraped_links = scrapped_ones()
        mydb = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="",database="supero_datalake2")
        mycursor = mydb.cursor()

        print("         [+] Scraping Items")
        for item in list_of_subcats_and_thier_links[4:-17]:
            s = requests.session()
            res2 = s.get("{}".format(item["link"]))
            sleep(random.randint(0, 1))
            new_page2 = BS(res2.text, features="html.parser")

            pagination_exists = False
            try:
                x = new_page2.select_one('#pagination_next')
                if x:
                    pagination_exists = True
            except:
                pass

            cards = new_page2.findAll('a', {'class': 'product-name'})
            mylist = []
            for card in cards:
                try:
                    mylist.append(card.get('href'))
                except:
                    pass
            print(f'mylist len = {len(mylist)}')
            if pagination_exists:
                for i in range(4):
                    if i == 0 or i == 1:
                        continue
                    print(f'Paginiting NO{i}')
                    try:
                        res2 = s.get("{}#/page-{}".format(item["link"] , i))
                        sleep(random.randint(0, 1))
                        new_page2 = BS(res2.text, features="html.parser")
                        cards = new_page2.findAll('a', {'class': 'product-name'})
                        for card in cards:
                            try:
                                mylist.append(card.get('href'))
                            except:
                                pass
                    except:
                        continue
                print(f'len AFTER = {len(mylist)}')

            print("             [+] Collecting data")
            for num, link in enumerate(mylist):
                if link in scraped_links:
                    print('     [+] item already scraped')
                    continue
                res2 = s.get(link)
                sleep(random.randint(0, 1))
                new_page = BS(res2.text, features="html.parser")

                try:
                    item_name_in_store = new_page.select_one(
                        '#center_column > div.primary_block.row > div.pb-center-column.col-xs-12.col-sm-7.col-md-6 > h1'
                    ).text.strip()

                    item_ref = new_page.select_one('#product_reference > span').text.strip()
                    try:
                        item_description = new_page.select_one('#short_description_block').text.strip()
                    except:
                        pass
                    item_link = link
                    image_item = new_page.select_one('#bigpic').get('src')
                    item_price = new_page.select_one('#our_price_display').text.strip()
                    item_price = convertPrice(item_price)
                    item_short_name = ''

                    try:
                        item_specification = new_page.find('table')
                    except:
                        item_specification = None

                    try:
                        item_reviews = new_page.findAll('div', {'class': 'comment_details col-sm-10'})
                    except:
                        item_reviews = None

                    # print("item_name_in_store = {}".format(item_name_in_store))
                    print("item_ref = {}".format(item_ref))
                    # print("item_description = {}".format(item_description))
                    # print("item_specification = {}".format(item_specification))
                    print("item_link = {}".format(item_link))
                    # print("image_item = {}".format(image_item))
                    # print("item_price = {}".format(item_price))
                    print("item_subcat_in_website = {}".format(item["name_sub_cat"]))
                    print("\n")

                except Exception as e:
                    print(e)
                    print(e.__traceback__.tb_lineno)
                    continue
                try:
                    myjson = dict()
                    if item_specification != None:
                        myjson['specification_table'] = item_specification
                    if item_reviews != None:
                        myjson['reviews'] = item_reviews
                    jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)
                    sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,unique_id) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                    val = (item_short_name, item_name_in_store,  item_link, 10, item["name_sub_cat"], jsonStringify, item_description, image_item, item_price,item_ref)
                    mycursor.execute(sql, val)
                    mydb.commit()
                except Exception as e:
                    print(f'Exeption {e}')
                    pass
    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":
    scrape()