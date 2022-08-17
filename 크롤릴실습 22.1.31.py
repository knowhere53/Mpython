import requests
import bs4
page = 1
url  = 'https://news.daum.net/economic#1{}' # {} 페이지 변하니
real_url = url.format(page)
resp = requests.get(real_url)
movie_bs = bs4.BeautifulSoup(resp.text, features="html.parser")

