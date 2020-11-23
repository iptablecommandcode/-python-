import requests

from bs4 import BeautifulSoup

from datetime import datetime as dt

now = dt.now()

targetSite = 'https://www.melon.com/chart/index.htm'

print("{} 현재 Melon 실시간 차트 Top 100".format(now))

header = {'User-agent':'Mozilla/5.0(Windows NT 6.1: WOW64;Trident/7.0;rv:11.0) Like Gecko'}

request = requests.get(targetSite,headers = header)

html = request.text

soup = BeautifulSoup(html,'html.parser')

ranks = soup.findAll('div',{'class':'ellipsis rank01'})

artists = soup.findAll('span',{'class':'checkEllipsis'})

print(ranks)

print(artists)

for i in range(len(ranks)):
    artist = artists[i].text.strip().split('\n')[0]

    rank = ranks[i].text.strip().split('\n')[0]

    print('{0:3d}.{1} - {2}'.format(i+1,artist,rank))