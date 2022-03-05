import requests
from bs4 import BeautifulSoup as BS

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
s = requests.session()
res = s.get('https://www.electroplanet.ma/marques/' , headers=headers)
soup = BS(res.text , features="html.parser")
brands = []
[ brands.append(item.get_text().strip().title()) for item in soup.find_all('li' , {'class' : 'brand-name'}) if item.get_text().strip().title() not in ['10.or','Acer','Adcom','Airtel','Alcatel','Alpha','Amazon','AOC','Apple','Aqua','Archos','Asus','Benq','Billion','Black Shark','BlackBerry','Blu','BQ','Byond','Cat','Celkon','Centric','Champion Computers','ChampOne','Cherry Mobile','Comio','Coolpad','Creo','Croma','Datawind','Detel','Dizo','Docoss','Elari','Elephone','Energizer','Essential','Evercoss','Fairphone','Flash','Fly','GeeksPhone','General Mobile','Gionee','Google','Homtom','Honor','HP','HTC','Huawei','Hyve','i-mobiles','iBall','iBerry','Idea','Infinix','InFocus','Intex','iQOO','Itel','iVoomi','Jio','Jivi','Jolla','Josh Mobile','Karbonn','Kestrel','Kodak','Kult','Kyocera','Land Rover','Lava','LeEco','Leica','Lemon','Lenovo','Lephone','LG','Lumigon','Lyf','M-tech','Mafe Mobile','Magicon','MarQ by Flipkart','Marshall','Maxx Mobile','Meizu','Mercury','Micromax','Microsoft','Mitashi','Mito','Mobiistar','Motorola','mPhone','MTS','MyPhone','Namotel','Neffos','Nexian','Nextbit','Nokia','Nubia','Nuu Mobile','Obi','Obi Worldphone','OnePlus','Onida','Oplus','Oppo','Oukitel','Panasonic','Pantel','Pepsi','Phicomm','Philips','Poco','Polaroid','Porsche Design','QiKU','QMobile','Razer','Reach','Realme','Reliance','Ringing Bells','Rio','Royole','Salora','Samsung','Sansui','Saygus','Sharp','Sikur','Silent Circle','Simmtronics','Sirin','Smartisan','Smartron','Sony','Spice','Sunstrike','Swipe','Symphony','Tambo','TCL','Tecno','Tonino Lamborghini','Turing','Umi','Unihertz','Vaio','Vertu','Viaan','Videocon','Vivo','Vodafone','Wickedleak','Wiio','Xiaomi','Xolo','Yamada Denki','Yandex','Yota Devices','Yu','Zen','Ziox','Zopo','ZTE','Zuk','Zync']]

[print(f"insert into brands(name, description, logo) values ('{x}'  , '' , '');") for x in brands]





