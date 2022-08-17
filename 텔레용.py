import telegram
import pandas as pd
token = "2023310856:AAGGtZfexPl2CJkHry1vxrrQoQ-3Nv8gWo0"
bot = telegram.Bot(token)

import requests
import bs4
wx = 'https://m.search.naver.com/search.naver?where=m&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&sm=mtb_she&qdt=0'
#ct > section.sc.csm.cs_weather_new._cs_weather > div > div.content_wrap > div.content_area > div > div > div.list_box > ul
# > li.week_item.today > div > div.cell_date > span
url = requests.get(wx)
wx_bs = bs4.BeautifulSoup(url.text, features='html.parser')

week_ls = wx_bs.find('ul', class_="week_list").text.split('   ')
temp = wx_bs.find('ul', class_="week_list").find_all('li')
wx_ls = []
for tt in temp:
    wx_ls.append('날씨' + tt.text.replace('     ','').replace('최저기온','  기온 : ').replace('최고기온',''))
wx_ls
for wx in wx_ls[:3]:
    bot.sendMessage(chat_id=1986401011, text=wx)


webpage = requests.get("https://finance.naver.com/marketindex/")
web = webpage.text
soup = bs4.BeautifulSoup(web, "html.parser")
print(soup)
usd = soup.select("a.head.usd")
usd = usd[0].text.replace("\n", " ")
bot.sendMessage(chat_id=1986401011, text=usd)



webpage = requests.get("https://finance.naver.com/")
web = webpage.text
soup = bs4.BeautifulSoup(web, "html.parser")
print(soup)
tem = soup.select("div.kospi_area.group_quot.quot_opn > div.heading_area")
a = tem[0].text.replace("\n"," ")
a = a[:16] + "||" + a[21:]
bot.sendMessage(chat_id=1986401011, text=a)

kodex200 = "kodex200 : "
b = soup.select("span.num")
b1 = b[2].text
kodex200 = kodex200 + b1 +" || "
b = soup.select("span.num3")
b1 = b[2].text
kodex200 = kodex200 + b1
if b1[0] == "-":
    kodex200 = kodex200+" 하락"
else:
    kodex200 = kodex200 + " 상승"

bot.sendMessage(chat_id=1986401011, text=kodex200)
