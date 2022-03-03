import datetime


#Global varibales
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
    tmp = price.split("Dhs")[0]
    tmp = tmp.split()
    floatprice = "".join(tmp)
    floatprice = floatprice.replace("," , ".")
    return float(floatprice)
