import requests


res = requests.get('http://192.168.1.3:8000/api/FeaturedAdsCard?page=1')

print(res.text)