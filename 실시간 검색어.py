import requests
import bs4
web = 'https://signal.bz/'
reps = requests.get(web)
web_bs = bs4.BeautifulSoup(reps.text, features="html.parser")
web_bs
aa =   web_bs.find('div', class_="realtime-rank")
aa
??? 안 뽑힌다.
