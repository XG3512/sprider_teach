import requests
import json
url = "https://spa3.scrape.center/api/movie/?limit=10&offset=40"
r = requests.get(url)

print(r.json()['results'][0]['categories'])
for i  in r.json()['results'][0]['categories']:
    print(i)