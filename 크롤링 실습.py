import requests
import bs4

page = 1
url  = 'https://movie.naver.com/movie/point/af/list.naver?&page={}' # {} 페이지 변하니
real_url = url.format(page)
resp = requests.get(real_url)
movie_bs = bs4.BeautifulSoup(resp.text, features="html.parser")
movie_bs.find_all('td')


















td = movie_bs.find('td', class='title')
print(td.find('a').text)
print(td.find('em').text)

print(td.text.split('|n')[5])
find_all

for td in td_list:
    print(td.find('a').text)
    print(td.find('em').text)
    print(td.text.split('|n')[5])
    print('*'*60)

move_data = []
for td in td_list:
    temp = {}
    temp['title'] = td.find('a').text
    temp['score'] = td.find('em').text
    temp['review'] = td.text.split('|n')[5]
    move_data.append(temp)

pd.DataFrame( move_data )



jj = movie_bs.find_all('td', class='title')
