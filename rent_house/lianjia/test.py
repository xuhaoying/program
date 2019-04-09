import requests
import re
from bs4 import BeautifulSoup
HEADERS = {
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

url = 'https://hz.zu.anjuke.com/fangyuan/xiaoshan/'
response = requests.get(url, headers=HEADERS)

html = response.content.decode('utf-8')

with open('anju', 'w') as f:
	f.write(html)

soup = BeautifulSoup(html, 'lxml')

