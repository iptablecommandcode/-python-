import requests

from bs4 import BeautifulSoup

naver_html = requests.get('https://www.naver.com/')

html = naver_html.text

print(html)