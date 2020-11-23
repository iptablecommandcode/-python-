import requests

from bs4 import BeautifulSoup

from datetime import datetime as dt

now = dt.now()

print("{} 현재 Naver 실시간 검색어 Top 20".format(now))

naver_html = requests.get('https://datalab.naver.com/')

html = naver_html.text

soup = BeautifulSoup(html,'html.parser')

words = soup.findAll('span',{'class':'title'})

for i in range(10):
    print('{0:2d}위 => {1}'.format(i + 1, words[i].text))