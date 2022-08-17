import pandas as pd
import requests
import bs4


page = 1
url  = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&PageNumber={}' # {} 페이지 변하니
real_url = url.format(page)
resp = requests.get(real_url)
movie_bs = bs4.BeautifulSoup(resp.text, features="html.parser")

td = movie_bs.find('td', class_ = "goodsTxtInfo")
td.find('a').text
td.find('div', class_='aupu').text.split('\n')[1].replace('\r','').replace('  ','')
td.find('div', class_='aupu').text.split('\n')[4].replace('\r','').replace('  ','').replace('| ','')
td.find('div', class_='aupu').text.split('\n')[6].replace('\r','').replace('  ','').replace('| ','')
td.find(class_='priceB').text

movie_bs.find('p', class_ = "read").text.replace('  ','').replace('\r\n\t\t\t','')

td_list = movie_bs.find_all('td', class_ = "goodsTxtInfo")


book_data = []
for td in td_list:
    temp = {}
    temp['title'] = td.find('a').text
    temp['author'] = td.find('div', class_='aupu').text.split('\n')[1].replace('\r', '').replace('  ', '')
    temp['pub'] = td.find('div', class_='aupu').text.split('\n')[4].replace('\r', '').replace('  ', '').replace('| ', '')
    temp['month'] = td.find('div', class_='aupu').text.split('\n')[6].replace('\r', '').replace('  ', '').replace('| ', '')
    temp['price'] = td.find(class_='priceB').text
    print(temp)
    book_data.append(temp)

book_data
book_data_df = pd.DataFrame(book_data)
book_data_df['pub']


book_data = []
for page in range(1, 11):
    url  = 'http://www.yes24.com/24/category/bestseller?CategoryNumber=001001025&sumgb=06&PageNumber={}' # {} 페이지 변하니
    real_url = url.format(page)
    resp = requests.get(real_url)
    movie_bs = bs4.BeautifulSoup(resp.text, features="html.parser")

    for td in td_list:
        temp = {}
        temp['title'] = td.find('a').text
        temp['author'] = td.find('div', class_='aupu').text.split('\n')[1].replace('\r', '').replace('  ', '')
        temp['pub'] = td.find('div', class_='aupu').text.split('\n')[4].replace('\r', '').replace('  ', '').replace('| ', '')
        temp['month'] = td.find('div', class_='aupu').text.split('\n')[6].replace('\r', '').replace('  ', '').replace('| ', '')
        temp['price'] = td.find(class_='priceB').text
        print(temp)
        book_data.append(temp)


# book_data_df.to_excel('data_data.xlsx')  # 안됨. openpyxl 있어야 한다고 나옴.

yes24_bs = bs4.BeautifulSoup(resp.text, features="html.parser")
ul = yes24_bs.find('ul', class_='')
ul
div = ul.find('div', class_='goods_info')
book_name = div.find('a').text
auth = div.find('sapn', class_='goods_auth').text.strip()


if div.find('em', class = 'yes_b').text:
    rate = div.find('span', class_='gd_rating').find('em', class='yes_b').text


