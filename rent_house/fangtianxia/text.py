from lxml import etree
import requests

url = "https://hz.zu.fang.com/house-a0151/"

# mytree = 

response = requests.get(url)
html = response.text
with open('sky.html', 'w') as f:
    f.write(html)


