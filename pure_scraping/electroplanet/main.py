import json
import requests
import pymysql
from bs4 import BeautifulSoup as BS
from global_parametrs import *
from time import sleep
import logging
import random

logging.basicConfig(filename='electroplanet.log', level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

def scrape(link , id_store , id_subcat):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en;q=0.9',
    }

    try:
        res = requests.get("{}".format(link) , headers=headers)

        #DB Connexion
        mydb = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="supero_datalake",
        )
        mycursor = mydb.cursor()

        items = BS(res.text,features="html.parser")
        items_cards = items.findAll("div", {"class": "item-inner"})

        for num, ic in enumerate(items_cards):
            item_brand = ic.find("span", {"class": "brand"}).get_text()
            item_ref = ic.find("span", {"class": "ref"}).get_text()
            item_price =  convert_item_price_to_double(
                (ic.find("span", {"class": "price"}).get_text()).strip()
            )
            item_name = "{} {}".format(item_brand, item_ref)
            item_link = ic.find("a" , {"class" : "product photo product-item-photo"}).get('href')
            image_item = ic.find('img' , {"class" : "product-image-photo"}).get('src')
            # item_stockage = find_device_stockage(item_ref)
            # item_color = find_device_color(item_ref)
            res2 = requests.get(item_link ,headers=headers)
            sleep(random.randint(4,7))
            new_page = BS(res2.text,features="html.parser")
            item_specification = new_page.find('div' , {'class' : 'data item content'})


            print("================{}============".format(num+1))
            print("item_brand = {}".format(item_brand))
            print("item_ref = {}".format(item_ref))
            print("item_price = {}".format(item_price))
            print("item_name = {}".format(item_name))
            print("item_link = {}".format(item_link))
            print("image_item = {}".format(image_item))
            # print("item_stockage = {}".format(item_stockage))
            # print("item_color = {}".format(item_color))
            # print("item_specification = {}".format(item_specification))
            print("\n")

            try:
                myjson = dict()
                if item_brand != None:
                    myjson["brand"] = item_brand
                if item_ref != None:
                    myjson["item_ref"] = item_ref


                # if item_stockage != "UNKNOWN":
                #     myjson["stockage"] = item_stockage
                # if item_color != "UNKNOWN":
                #     myjson["color"] = item_color
                if item_specification != None:
                    myjson['specification_table'] = item_specification
                # if item_connexion_adapter != "UNKNOWN":
                #     myjson["connexion_adapter"] = item_connexion_adapter
                # if item_screen_size != "UNKNOWN":
                #     myjson["screen_size"] = item_screen_size
                # if item_garantie != "UNKNOWN":
                #     myjson["garantie"] = item_garantie
                # if item_ram != "UNKNOWN":
                #     myjson["ram"] = item_ram
                # if item_stockage_type != "UNKNOWN":
                #     myjson["stockage_type"] = item_stockage_type
                # if item_lenght != "UNKNOWN":
                #     myjson["length"] = item_lenght
                # if item_power != "UNKNOWN":
                #     myjson["power"] = item_power


                jsonStringify = json.dumps(myjson, indent=4, sort_keys=True, default=str)

                sql = "select current_price from items where name_in_store = %s"
                val = (item_ref)
                mycursor.execute(sql, val)
                myresult = mycursor.fetchall()
                if(len(myresult) == 0):
                    # sql = "INSERT INTO items (name ,name_in_store,link, id_store ,id_subcategory ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                    sql = "INSERT INTO items (prod_name ,name_in_store,link, id_store ,category_in_store ,specification,details ,image_url,current_price,last_updated_at) VALUES (%s, %s, %s, %s, %s ,%s ,%s,%s ,%s, %s)"
                    val = (item_name, item_ref, item_link, id_store, id_subcat, jsonStringify, "", image_item, item_price,scraped_at)
                    mycursor.execute(sql, val)
                    print("id = {}".format(
                        mycursor.lastrowid
                    ))
                    sql = "INSERT INTO prices (id_item ,price,created_at) VALUES (%s, %s, %s)"
                    val = (mycursor.lastrowid, item_price, scraped_at)
                    mycursor.execute(sql, val)
                    print("\n")
                    mydb.commit()
                else:
                    if(myresult[0][0] != item_price ):

                        sql = "select id from items where name_in_store = %s"
                        val = (item_ref,)
                        mycursor.execute(sql, val)
                        myresult = mycursor.fetchall()
                        id = myresult[0][0]

                        sql = "update items set current_price = %s , last_updated_at = %s where name_in_store = %s"
                        val = (item_price , scraped_at , item_name)
                        mycursor.execute(sql, val)
                        mydb.commit()

                        sql = "INSERT INTO prices (id_item ,price,created_at) VALUES (%s, %s, %s)"
                        val = (id, item_price, scraped_at)
                        mycursor.execute(sql, val)
                        mydb.commit()
                    else:
                        print("PRICES ARE STILL THE SAME")
                        print(" -> {} == {}".format(myresult[0][0] , item_price))


            except Exception as e:
                print(e)
                print("Database conn error !")


        mydb.close()
    except:
        pass




if __name__ == "__main__":
    for l in electroplanet_console:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_préparation_culinaire:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_petit_dejeuner:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_accessoires_electromenager:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_balance_de_cuisine:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_cafetière_et_expresso:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_cuiseurs:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_cuisson_conviviale:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_cuisson_festive:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_four_et_micro_ondes:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_friteuses:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_Machine_a_gateaux:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_Pack_preparation_culinaire:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_Barbecue_et_plancha:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_refrigerateur:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_accessoires_electromenager2:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_congelateur:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_cuisiniere:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_encastrable:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_hotte_aspirante:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_lave_vaisselle:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_machine_a_laver:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_plaque_de_cuisson:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_sèche_linge:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_accessoires_electromenager3:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_Entretien_du_sol:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_soin_du_ligne:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_bebe:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_coiffure:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_epilation_pour_elle:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_pack_beaute:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_rasage_pour_lui:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_Sante_et_bien_etre:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_soin_beaute:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_chaufage:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_chaufage_eau:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_climatisation:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_traitement_de_air:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_tv:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_accessoires_tv_video:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_appareil_photo:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_recepteur_et_abonnement:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_ecoteurs:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_Barres_de_son:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_casques_audio:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_ordinateur_bureau:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_imprimantes_et_scanner:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_accessoires_informatique:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_bagagerie:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_smartphones:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_tablete_android:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_telephones:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_accessoires_smarphones:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_accessoires_tablettes:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_alimenttion_et_charge:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_objet_connectes:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_accessoires_de_cuisine:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_article_de_boisson:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_conservation_alimentaire:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_cuisson_sur_feux:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_filtration_d_eau:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_moules_et_plats:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

    for l in electroplanet_accessoires_gaming:
        scrape("{}".format(l['link']), l["id_store"], l["subcategory"])
        sleep(random.randint(4,7))

