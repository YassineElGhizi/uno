import json
import pymysql
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
import random

big_parents = []
scrapped_links = []

def scrapped_ones():
    # DB Connexion
    mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_datalake2",)
    mycursor = mydb.cursor()
    sql = "select link from items where id_store = 13"
    mycursor.execute(sql, )
    scrapped_one = mycursor.fetchall()
    scrapped_one = [i[0] for i in scrapped_one]
    return scrapped_one

def convertPrice(price):
    price = price.split(' TTC ')[0]
    tmp = price.replace('Dh  TTC', '')
    tmp = tmp.replace('  TTC', '')
    tmp = tmp.replace('Dh', '')
    tmp = tmp.replace(' ', '')
    tmp = tmp.replace(',', '.')
    tmp = tmp.replace(' \n\n', '')
    return float("".join(tmp))

def init():
    print("[+] Initilialisation")
    s = requests.session()
    res = s.get("https://electrobousfiha.com/")
    items = BS(res.text, features="html.parser")
    a_tags = items.findAll('li', {'class': 'item-2'})
    for a in a_tags:
        try:
            big_parents.append(a.find('a').get('href'))
        except:
            pass


def scrape():
    try:
        init()
        scraped_links = scrapped_ones()
        mydb = pymysql.connect(host="127.0.0.1", port=3306 ,user="root", password="", database="supero_datalake2",)
        mycursor = mydb.cursor()
        print("         [+] Scraping Items")
        for link in big_parents:
            s = requests.session()
            res2 = s.get("{}".format(link))
            new_page2 = BS(res2.text, features="html.parser")
            sleep(random.randint(0, 1))

            pagination_exists = False
            try:
                x = new_page2.select_one('#js-product-list-top > nav')
                if x:
                    pagination_exists = True
            except:
                pass


            cards = new_page2.findAll('a', {'class': 'thumbnail product-thumbnail'})
            links_onyl = []
            for c in cards:
                links_onyl.append(c.get('href'))
            print(f'pagination_exists = {pagination_exists}')
            print(f'mylist len = {len(links_onyl)}')
            if pagination_exists:
                for i in range(13):
                    if i == 0 or i == 1:
                        continue
                    print(f'Paginiting NO{i}')
                    try:
                        res2 = s.get("{}?page={}".format(link, i))
                        sleep(random.randint(0, 1))
                        new_page2 = BS(res2.text, features="html.parser")
                        cards = new_page2.findAll('a', {'class': 'thumbnail product-thumbnail'})
                        for card in cards:
                            try:
                                links_onyl.append(card.get('href'))
                            except:
                                pass
                    except:
                        continue
                print(f'len AFTER = {len(links_onyl)}')


            print("             [+] Collecting data")
            for link in links_onyl:
                if link in scraped_links:
                    print('     [+] item already scraped')
                    continue
                res2 = s.get(link)
                sleep(random.randint(0, 1))
                new_page = BS(res2.text, features="html.parser")
                if link in scrapped_links:
                    print(link, 'already got scraped')
                    continue

                try:
                    print(link)
                    scrapped_links.append(link)
                    item_name_in_store = new_page.select_one('#main > div.clearfix > div.col-lg-7.col-sm-12.col-xs-12.pb-right-column > h1').text.strip()
                    try:
                        item_description = new_page.select_one('#description > div').text.strip()
                    except:
                        item_description = None
                        pass
                    item_link = link
                    image_item = new_page.select_one('#content > div > div.product-cover > img').get('src')
                    item_price = new_page.find('div' , {'class' : 'current-price'}).get_text().strip()
                    item_price = convertPrice(item_price)
                    if item_price == None:
                        continue
                    item_short_name = ''

                    try:
                        item_specification = new_page.select_one('#review > section > dl').text.strip()
                    except:
                        item_specification = None

                    item_ref = new_page.select_one('#main > div.clearfix > div.col-lg-7.col-sm-12.col-xs-12.pb-right-column > div.product-reference > span').text.strip()
                    item_subcat_in_website =new_page.select_one('#wrapper > div > nav > div > ul > li:nth-child(2) > a > span').text.strip()


                    # print(f'item_link = {item_link}')
                    print(f'item_name_in_store = {item_name_in_store}')
                    # print(f'item_description = {item_description}')
                    print(f'image_item = {image_item}')
                    print(f'item_price = {item_price}')
                    # print(f'item_specification = {item_specification}')
                    print(f'item_ref = {item_ref}')
                    print(f'item_subcat_in_website = {item_subcat_in_website}')
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
                    val = (item_short_name, item_name_in_store,  item_link, 13, item_subcat_in_website, jsonStringify, item_description, image_item, item_price,item_ref)
                    mycursor.execute(sql, val)
                    mydb.commit()
                except Exception as e:
                    print(f'Exeption {e}')
                    pass
    except Exception as e:
        print(f'Exception {e}')
        pass


if __name__ == "__main__":
    scrape()



