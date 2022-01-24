import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit' +
            '/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }
    res = requests.get("https://spa3.scrape.center/", headers=headers)
    print(res.status_code)
    soup = BeautifulSoup(res.text, 'lxml')
    targets = soup.find_all("div", class_="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16")
    for each in targets:
        print(each.a.h2.text)