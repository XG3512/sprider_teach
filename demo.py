from __future__ import unicode_literals
import requests
import json
from bs4 import BeautifulSoup
def deal_json(name,categorie,time,area,long,star):
    mv = movie(name, categorie, time, area, long, star)
    js_data=json.dumps(mv.__dict__,ensure_ascii=False)
    return js_data
class movie:
    def __init__(self,name,categorie,time,area,long,star):
        self.name=name
        self.categorie=categorie
        self.time=time
        self.area=area
        self.long=long
        self.star=star
def categories(cont):
    data=[]
    for cge in cont.find_all('button',class_="el-button category el-button--primary el-button--mini"):
        data.append(cge.find('span').string)
    return data
def area_time_long(cont):
    data=[]
    for atl in cont.find_all('div',class_='m-v-sm info'):
        for atl_data in atl.find_all('span'):
            data.append(atl_data.string)
    return data
def getmessage(cont):
    name=cont.find('h2',class_="m-b-sm").string
    print(name)
    categorie=categories(cont)
    area=area_time_long(cont)[0]
    long=area_time_long(cont)[2]
    try:
        time=area_time_long(cont)[3]
    except BaseException:
        time="NAN"
    star=cont.find('p','score m-t-md m-b-n-sm').string[17:]
    mv=deal_json(name,categorie,time,area,long,star)
    return mv
def get_page(url):
    # url='https://ssr1.scrape.center/page/1
    response = requests.get(url)
    # print(response.text)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    move_data=[]
    for i in soup.find_all('div',class_="el-card item m-t is-hover-shadow"):
        move_data.append(getmessage(i))
    return move_data
if __name__ == '__main__':
    url='https://ssr1.scrape.center/page/1'
    get_page(url)