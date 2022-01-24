import requests
def getdata(url):
    r = requests.get(url)
    for i  in r.json()['results']:
        print(i['name'])
for j in range(10,101,10):
    url="https://spa3.scrape.center/api/movie/?limit=10&offset="+str(j)
    print(url)
    getdata(url)