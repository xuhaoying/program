import urllib
import requests
from lxml import etree

name = input("请输入您要访问的贴吧: ")
page = int(input("请输入您要访问的页数: "))

url_start = "http://tieba.baidu.com/f?kw={name}&ie=utf-8&pn={offset}"

f =  open("title.csv", 'w')

for i in range(page):
    offset = i * 50
    url = url_start.format(name=name, offset=offset)
    response = requests.get(url)
    html = response.content.decode()
    tree = etree.HTML(html)
    titles = tree.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@title')
    for title in titles:
        f.write(title)
        f.write("\n")


f.close()
