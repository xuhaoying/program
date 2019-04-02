'''
遍历所有的地区
对于每个地区
    获取当前页的每个href
    获取下一页
    如果下一页就是当前页， 退出循环
'''

import requests
from bs4 import BeautifulSoup
from lxml import etree

# 获取指定URL的HTML
def get_response(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception:
        return None

# {'/house-a0153/': '江干', ...} 地区URL
AREA = {}
# 获取所有地区的URL
def area():
    html = get_response("https://hz.zu.fang.com/house-a0151/")
    soup = BeautifulSoup(html, 'lxml')   
    l = soup.select("#rentid_D04_01 > dd > a")
    for a in l:
        href = a['href']
        area = a.get_text()
        AREA[href] = area

def main():
    URL = "https://hz.zu.fang.com{}/"
    for href, area in AREA.items():
        url = URL.format(href)  # 地区的URL
        html = get_response(url)
        while True:
            html = parse_one_page(html)

def parse_one_page(html):  
    soup = BeautifulSoup(html, 'lxml')
    get_house_href(soup)
    get_next_page(soup)

# 获取页面里的房源 URL
def get_house_href(soup):
    href_list = soup.select('#info a')


# 获取下一页的 url
def get_next_page(soup):       
    mytree = etree.HTML(html)
    mytree.xpath('//*[@id="rentid_D10_01"]/a[last()-1]/@href')

    # 获取当前页url
    now_page = soup.select('#rentid_D10_01 > a.pageNow')
    # 没有下一页了
    if next_page == now_page:
        return
    return next_page
    


if __name__ == '__main__':
    html = get_response("https://hz.zu.fang.com/house-a0151/")
    soup = BeautifulSoup(html, 'lxml')   
    print(get_next_page(soup))



