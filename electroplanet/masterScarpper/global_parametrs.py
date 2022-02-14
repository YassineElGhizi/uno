import datetime

#GLOBAL Vars
electroplanet_electromenager = [
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/batteur" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/blender" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/hache-viande" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/hachoir" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/kitchen-machine" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/mixeur-plongeant" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/moulinette" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/robot-de-cuisine" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/sorbetiere" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/preparation-culinaire/yaourtiere" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/bouilloire" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/centrifugeuse" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/extracteur-de-jus" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/grill-pain-toaster" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/presse-agrume" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/petit-dejeuner/set-petit-dejeuner" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/cafetiere-classique" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/expresso-a-capsule" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/expresso-avec-broyeur-a-cafe" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/machine-a-cafe-pression" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cafetiere-et-expresso/moulin-a-cafe" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/petit-electromenager/cuiseur/cuiseur-a-riz-et-a-vapeur" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cuiseur/cuiseur-a-vapeur" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cuiseur/cuiseur-classique" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/crepiere" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/gaufrier" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/grill-a-viande" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/grill-a-panini" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/cuisson-conviviale/appareil-a-croque-monsieur" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/petit-electromenager/four-et-micro-onde/four-posable" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/four-et-micro-onde/micro-onde" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/four-et-micro-onde/rechaud" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-biscuit" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-tarte" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-madeleine" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-pain" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/petit-electromenager/machine-a-gateaux/machine-a-popcake" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/gros-electromenager/refrigerateur/mini-bar" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/refrigerateur/petit-refrigerateur" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-4-portes" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-americain-duo-jumelable" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-americain-side-by-side" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-avec-congelateur-en-bas" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/refrigerateur/refrigerateur-avec-congelateur-en-haut" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/gros-electromenager/cuisiniere/cuisiniere-4-feux" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/cuisiniere/cuisiniere-5-feux" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/cuisiniere/cuisiniere-5-feux-cache-bouteille" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/gros-electromenager/encastrable/four-encastrable" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/encastrable/grand-four-encastrable" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/encastrable/lave-vaisselle-encastrable" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/encastrable/machine-a-laver-encastrable" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/encastrable/petit-four-encastrable" , "id_store" : 3,"subcategory" : 8},


    { "link" : "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-a-hublot" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-ouverture-en-haut" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-sechante" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-semi-automatique-avec-essorage" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/gros-electromenager/machine-a-laver/machine-a-laver-semi-automatique-sans-essorage" , "id_store" : 3,"subcategory" : 8},


    { "link" : "https://www.electroplanet.ma/entretien-de-la-maison/entretien-du-sol/aspirateur" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/entretien-de-la-maison/entretien-du-sol/aspirette" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/entretien-de-la-maison/entretien-du-sol/nettoyeur-a-vapeur" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/entretien-de-la-maison/entretien-du-sol/pack-aspirateur" , "id_store" : 3,"subcategory" : 8},

    { "link" : "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/housse-table-a-repasser" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/planches-a-repasser" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/centrale-vapeur" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/defroisseur" , "id_store" : 3,"subcategory" : 8},
    { "link" : "https://www.electroplanet.ma/entretien-de-la-maison/soin-du-linge/fer-a-repasser" , "id_store" : 3,"subcategory" : 8},

]


electroplanet_bebe = [
    { "link" : "https://www.electroplanet.ma/sante-beaute-bebe/coiffure/brosse-soufflante" , "id_store" : 3,"subcategory" : 9},
    { "link" : "https://www.electroplanet.ma/sante-beaute-bebe/coiffure/fer-a-coiffer" , "id_store" : 3,"subcategory" : 9},
    { "link" : "https://www.electroplanet.ma/sante-beaute-bebe/coiffure/lisseur" , "id_store" : 3,"subcategory" : 9},
    { "link" : "https://www.electroplanet.ma/sante-beaute-bebe/coiffure/seche-cheveux" , "id_store" : 3,"subcategory" : 9},

]


electroplanet_chaufage = [
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/chauffage-a-gaz" , "id_store" : 3,"subcategory" : 10},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/chauffage-soufflant" , "id_store" : 3,"subcategory" : 10},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/cheminee-electrique" , "id_store" : 3,"subcategory" : 10},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/convecteur" , "id_store" : 3,"subcategory" : 10},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffage/radiateur-bain-d-huile" , "id_store" : 3,"subcategory" : 10},

    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffe-eau/chauffe-eau-a-gaz" , "id_store" : 3,"subcategory" : 10},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffe-eau/chauffe-eau-electrique" , "id_store" : 3,"subcategory" : 10},
    { "link" : "https://www.electroplanet.ma/confort-de-la-maison/chauffe-eau/chauffe-eau-solaire" , "id_store" : 3,"subcategory" : 10},
]


electroplanet_climat = [
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/climatisation/climatiseur", "id_store": 3,"subcategory": 11},
    {"link": "https://www.electroplanet.ma/confort-de-la-maison/climatisation/ventilateur", "id_store": 3,"subcategory": 11},
]

electroplanet_tv = [
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/tous-les-televiseur", "id_store": 3,"subcategory": 6},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/smart-tv", "id_store": 3,"subcategory": 6},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/televiseurs-4k-uhd", "id_store": 3,"subcategory": 6},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/televiseurs-premium-4k-uhd", "id_store": 3,"subcategory": 6},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/televiseurs-8k", "id_store": 3,"subcategory": 6},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/oled", "id_store": 3,"subcategory": 6},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/nanocell", "id_store": 3,"subcategory": 6},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/qled", "id_store": 3,"subcategory": 6},
    {"link": "https://www.electroplanet.ma/tv-photo-video/televiseur/miniled-neoqled-qned", "id_store": 3,"subcategory": 6},
]

electroplanet_appareil_photo = [
    {"link": "https://www.electroplanet.ma/tv-photo-video/appareil-photo-numerique/appareil-photo-bridge", "id_store": 3,"subcategory": 12},
    {"link": "https://www.electroplanet.ma/tv-photo-video/appareil-photo-numerique/appareil-photo-compact", "id_store": 3,"subcategory": 12},
    {"link": "https://www.electroplanet.ma/tv-photo-video/appareil-photo-numerique/appareil-photo-instantane", "id_store": 3,"subcategory": 12},
    {"link": "https://www.electroplanet.ma/tv-photo-video/appareil-photo-numerique/appareil-photo-reflex", "id_store": 3,"subcategory": 12},
]

electroplanet_ecoteurs = [
    {"link": "https://www.electroplanet.ma/audio-hi-fi/ecouteurs/ecouteurs-avec-micro","id_store": 3, "subcategory": 5},
    {"link": "https://www.electroplanet.ma/audio-hi-fi/ecouteurs/ecouteurs-avec-micro-sans-fil","id_store": 3, "subcategory": 5},
    {"link": "https://www.electroplanet.ma/audio-hi-fi/ecouteurs/ecouteurs-sportifs-avec-micro","id_store": 3, "subcategory": 5},
    {"link": "https://www.electroplanet.ma/tv-photo-video/appareil-photo-numerique/appareil-photo-reflex","id_store": 3, "subcategory": 5},

    {"link": "https://www.electroplanet.ma/audio-hi-fi/casque-audio/casque-audio-avec-micro","id_store": 3, "subcategory": 5},
    {"link": "https://www.electroplanet.ma/audio-hi-fi/casque-audio/casque-audio-avec-micro-sans-fil","id_store": 3, "subcategory": 5},
]

electroplanet_informatique =[
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/macbook", "id_store": 3,"subcategory": 3},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/netbook", "id_store": 3,"subcategory": 13},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/notebook", "id_store": 3,"subcategory": 13},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/pc-gamer", "id_store": 3,"subcategory": 13},
    {"link": "https://www.electroplanet.ma/informatique/ordinateur-portable/ultrabook", "id_store": 3,"subcategory": 13},
]

electroplanet_smartphones = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/smartphone/iphone", "id_store": 3,"subcategory": 1},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/smartphone/telephone-android", "id_store": 3,"subcategory": 14},
]

electroplanet_tablete_android = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/tablettes/ipad", "id_store": 3,"subcategory": 2},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/tablettes/tablettes-android", "id_store": 3,"subcategory": 15},

    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/telephone/domestique", "id_store": 3, "subcategory": 15},
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/telephone/mobile", "id_store": 3, "subcategory": 15},

]

electroplanet_accessoires_smarphones = [
    {"link": "https://www.electroplanet.ma/smartphone-tablette-gps/accessoires-smartphone/cover-de-protection", "id_store": 3, "subcategory": 16},
]

electroplanet_accessoires_informatique = [
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/casques-gamers","id_store": 3, "subcategory": 5},
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/claviers","id_store": 3, "subcategory": 18},
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/manettes","id_store": 3, "subcategory": 18},
    {"link": "https://www.electroplanet.ma/jeux-consoles/accessoires-gaming/souris-gamers","id_store": 3, "subcategory": 18},
]

electroplanet_console = [
    {"link": "https://www.electroplanet.ma/jeux-consoles/consoles/consoles-play-station", "id_store": 3,"subcategory": 19},
    {"link": "https://www.electroplanet.ma/jeux-consoles/jeux-video/jeux", "id_store": 3,"subcategory": 19},
]

items_present_in_page = dict()
cards_links = list()

garantie_list = [
    '1 An de Garantie',
    '1 an de Garantie',
]

screen_size_list = [
    '12.9 pouces',
    '10.9 Pouces',
    '10.2 Pouces',
    '10.2 pouces',
    '11 Pouces',
    '11 pouces',
    '8.3 pouces',
    '13" Puce',
    '13" avec écran Rétina Puce',
    '16" avec écran Rétina Puce',
    '27" avec écran Retina 5K',
    '24" avec écran Retina 4.5K',
    '16" avec écran Rétina',
]

connextion_adapter = [
    'Wi-Fi + 4G',
    'Wi-Fi + Cellular',
    'Wi-Fi + 4G / Cellulaire',
    'Wi-Fi',
    'Wi-Fi',
]

power = [
    '30W',
    '12W',
    '20W',
    '5W',
]

stockage_list = [
                 '32 Go',
                 '32Go',
                 '32 Gb' ,
                 '32Gb' ,
                 '32b' ,
                 '32G' ,
                 '128 Gb',
                 '128Gb',
                 '128G',
                 '128 Go',
                 '128G',
                 '256 Gb',
                 '256 Go',
                 '256Go',
                 '256G',
                 '256Gb',
                 '256b',
                 '512 Gb',
                 '512Gb',
                 '512G',
                 '512 Go',
                 '512Go',
                 '1 Tb' ,
                 '1Tb' ,
                 '1T' ,
                 '1 To' ,
                 '2 Tb',
                 '2Tb',
                 '2T',
                 '2 To',
                 '64 Go' ,
                 '64 Gb',
                 '64Gb',
                 '64G',
        ]

colors = [
        'Violet',
        'Bleu Alpin',
        'Red',
        'Graphite',
        'Or' ,
        'Bleu Pacifique',
        'Argent',
        'Argent',
        'Rose',
        'Blue',
        'Bleu',
        'Minuit' ,
        'Noir' ,
        'NOIR' ,
        'Blanc' ,
        'Rouge',
        'Vert Nuit',
        'Vert',
        'Jaune',
        'Gold' ,
        'Silver',
        'Black',
        'Midnight',
        'Pacific Blu' ,
        'Green' ,
        'Pink' ,
        'Gris',
        'Lumière Stellaire',
        ]

ram = [
    '8 Go RAM',
    '8 Go',
    '16 Go RAM',
    '16 Go',
    '32 Go RAM',
    '32 Go',
    '64 Go RAM',
    '64 Go',
    '128 Go RAM',
    '128 Go',
    '4 Go RAM'
    '4 Go'
    '256 Go RAM',
    '256 Go',
]

stockage_type = [
    'SSD',
    'ssd',
    'HDD',
    'hdd',
]

device_lenght = [
    '2M',
    '1M',
    '3M',
    '4M',
    '2 m',
    '1 m',
    '3 m',
    '4 m',
]


now = datetime.datetime.now()
scraped_at = "{}-{}-{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)

#Functions

def find_device_power(title):
    for i in power:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_lenght(title):
    for i in device_lenght:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_stockage(title):
    for st in stockage_list:
        if st.upper() in title:
            return st

    for st in stockage_list:
        if st in title:
            return st

    return "UNKNOWN"

def find_device_color(title):
    for c in colors:
        if c in title:
            return c

    for c in colors:
        if c.upper() in title:
            return c

    return "UNKNOWN"

def find_device_garantie(title):
    for i in garantie_list:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_screen_size(title):
    for i in screen_size_list:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_connextion_adapter(title):
    for i in connextion_adapter:
        if i in title:
            return i
    return "UNKNOWN"


def find_device_ram(title):
    for i in ram:
        if i in title:
            return i
    return "UNKNOWN"

def find_device_type_stockage(title):
    for i in stockage_type:
        if i in title:
            return i
    return "UNKNOWN"

def convert_item_price_to_double(price):
    # tmp = price.split("MAD")[0]
    tmp = price.split()
    floatprice = "".join(tmp)
    floatprice = floatprice.replace("," , ".")
    return float(floatprice)
