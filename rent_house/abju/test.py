
import re
import requests
from bs4 import BeautifulSoup

with open('anju') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

data = soup.select()
# for h in data:
#     href = h['href']
#     print(href)

print(len(data))


