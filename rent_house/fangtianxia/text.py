import requests
from lxml import etree
from bs4 import BeautifulSoup

# with open('sky.html') as f:
#     html = f.read()

# mytree = etree.HTML(html)

# 倒数第二个
# print(mytree.xpath('//*[@id="rentid_D10_01"]/a[last()-1]/@href'))

# soup = BeautifulSoup(html, 'lxml')
# # next_page = soup.select('#rentid_D10_01 > a:nth-last-child(2)')
# next_page = soup.select('#rentid_D10_01 > a:nth-child(7)')
# print(next_page)

response = requests.get('https://hz.zu.fang.com/chuzu/3_247517340_1.htm?channel=1,2')

html = response.text
with open('house.html', 'w') as f:
    f.write(html)