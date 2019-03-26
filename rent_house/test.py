import requests
import re
from bs4 import BeautifulSoup
HEADERS = {
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

url = 'https://hz.lianjia.com/zufang/HZ2200458349433061376.html?nav=0'
response = requests.get(url, headers=HEADERS)

html = response.content.decode('utf-8')

# phone = re.search('<p class="content__aside__list--bottom oneline".*?>(.*?)</p>', html)
# phone = phone.group(1) 

soup = BeautifulSoup(html, 'lxml')
name = soup.select('.desc .name')[0].get_text()
phone = soup.select('.desc .phone')[0].get_text()

print(name)
print(phone)