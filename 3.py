import requests
from bs4 import BeautifulSoup
header={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
url = "https://ssr1.scrape.center/page/1"

init_page = requests.get(url,headers = header).content
init_soup = BeautifulSoup(init_page, 'html.parser')

all_movies = init_soup.find('div', class_="el-col el-col-18 el-col-offset-3")
for each_movie in all_movies.find_all('div', class_="el-card"):
    all_a_tag = each_movie.find_all('h2')


movie_name = all_a_tag[1].text
print(movie_name)