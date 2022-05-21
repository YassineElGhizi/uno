from bs4 import BeautifulSoup as BS
import json

from mappers.Helpers.electroplanet import extract_digits, electroplanet_storage
from mappers.Helpers.electroplanet_helprs.generale_purposed_functions import mydb


def extract_specification_json_brestmark(html_table : str) -> dict:
    soup = BS(html_table , features="html.parser")
    print(soup.prettify())
    quit()
    d = {}
    for tag in soup.find_all('tr'):
        try:
            d[tag.find('th').get_text().strip()] = tag.find('td').get_text().strip()
        except:
            pass
    return d



def get_category_id_saligon(cat_in_store:str) -> str:
    if cat_in_store == 'Machines à glaçons & Glacière':
        return '499'
    f = open('../mappeed_categories/saligon.json')
    data = json.load(f)
    f.close()
    for c in data:
        tmp =cat_in_store.replace('è', 'e')
        tmp =tmp.replace('È', 'E')
        tmp =tmp.replace('Ê', 'E')
        tmp =tmp.replace('é', 'e')
        tmp =tmp.replace('ê', 'e')
        tmp =tmp.replace('ç', 'c')
        tmp =tmp.replace('É', 'E')
        tmp = tmp.replace('à', 'a')
        tmp = tmp.replace('&', 'et')
        tmp = tmp.replace('â', 'a')
        if tmp in c.keys():
            prod_cat = c[str(tmp)]
            break
    else:
        prod_cat= '449'
        print(f'CAT 311 !! {cat_in_store}')
        quit()
    return prod_cat


def dictfetchall(cursor):
    """Returns all rows from a cursor as a list of dicts"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

def get_saligon_products():
    mycursor = mydb.cursor()
    sql = """SELECT * FROM ITEMS WHERE id_store = 12;"""
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results



def get_item_stockage_id(stockage:str):
    stockage_digit = extract_digits(stockage)[0]
    for c in electroplanet_storage:
        if int(c['value']) == stockage_digit:
            return c['id']
    return None