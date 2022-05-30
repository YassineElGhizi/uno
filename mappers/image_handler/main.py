from helpers import dictfetchall
import requests
from datetime import datetime
import logging
import boto3
from botocore.exceptions import ClientError
import pymysql
from time import sleep
from random import randint

#GLOBAL PARAMS
ABSOLUTE_IMAGES_PATH = r'C:\Users\yassine_el_ghizi\PycharmProjects\unoScrapping\mappers\image_handler\tmp_downloaded_images'
RELATIVE_IMAGES_PATH = r'./tmp_downloaded_images/'
NOT_FOUND_IMAGE = '[https://supero.s3.eu-west-3.amazonaws.com/images/404.png]'
BUCKET = 'supero'
s3_client = boto3.client('s3')
s = requests.session()
mydb = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="supero_api", )
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-US,en;q=0.9',
    'DNT': '1',
    'Referer': 'https://google.com'
}

def get_product_images():
    mycursor = mydb.cursor()
    sql = """SELECT id,images FROM products;"""
    mycursor.execute(sql, )
    results = dictfetchall(mycursor)
    return results

def download_image(link):
    response = s.get(link, headers=headers)
    sleep(randint(0, 1))
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'{RELATIVE_IMAGES_PATH}{current_time}.png', 'wb') as image:
        image.write(response.content)
    return f'{current_time}.png'

def save_current_status(id):
    with open('current_status.txt', 'a', encoding='utf8') as f:
        f.write(f'{id}\n')

def upload_file(file_name, file_name_in_s3):
    try:
        s3_client.upload_file(file_name, BUCKET, 'images/'+file_name_in_s3)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def update_product_image(format_image_from_s3, id):
    mycursor = mydb.cursor()
    sql = f"update products set images = %s where id = %s"
    val = (format_image_from_s3, int(id))
    mycursor.execute(sql, val)
    mydb.commit()

if __name__ == '__main__':
    for num, i in enumerate(get_product_images()):
        print(f'num : {num}')
        if i['images'] == '["None"]':
            update_product_image(NOT_FOUND_IMAGE, i['id'])
            save_current_status(i['id'])
            continue
        if 'supero.s3.eu-west-3.amazonaws.com' in i['images']:
            continue
        res = i['images'].strip('][').split(",")
        print(res[0].replace('"', ''))
        downloded_image_path = ABSOLUTE_IMAGES_PATH + '\\' + download_image(res[0].replace('"', ''))
        downloded_image_path = downloded_image_path.replace(' ', '')
        file_name_in_s3 = downloded_image_path.split('\\')[-1]
        if upload_file(downloded_image_path, file_name_in_s3):
            image_from_s3 = 'https://supero.s3.eu-west-3.amazonaws.com/images/'+file_name_in_s3
            format_image_from_s3 = f'["{image_from_s3}"]'
            update_product_image(format_image_from_s3, i['id'])
            save_current_status(i['id'])
        else:
            update_product_image(NOT_FOUND_IMAGE, i['id'])
            save_current_status(i['id'])

