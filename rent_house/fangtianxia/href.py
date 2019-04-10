'''
取出地区的url 并拼接
遍历所有的地区url
对于每个地区
    每个页面
        获取当前页的每个href
        获取下一页
        如果下一页就是当前页， 退出循环
'''

import time
import random
import requests
from bs4 import BeautifulSoup
from lxml import etree
from parse_house import HouseInfos


# 获取指定URL的HTML
def get_response(url):
    try:
        time.sleep(random.randint(1,3))
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception:
        return None

# {'/house-a0153/': '江干', ...} 地区URL
AREA = {}
# 获取所有地区的URL
def get_area():
    html = get_response("https://hz.zu.fang.com/house-a0151/")
    soup = BeautifulSoup(html, 'lxml')   
    l = soup.select("#rentid_D04_01 > dd > a")
    for a in l:
        href = a['href']
        area = a.get_text()
        AREA[href] = area

def parse_one_page(html, area):  
    '''
    解析当前列表页面
    解析列表页面
    得到当前列表页面所有房源URL, 并进行房源信息解析
    和 下一页的URL
    '''
    mytree = etree.HTML(html)
    href_list = get_house_href(mytree)
    for href in href_list:
        # 对每个房源进行解析
        href = "https://hz.zu.fang.com" + href 
        try:
            html = get_response(href)
            house = HouseInfos(html, area)
        except Exception as e:
            print(e)
        # print(href)
        # break
        html = get_response(href)
        HouseInfos(html, area)

        # print(href)
        # break

    next_url = get_next_page(mytree)
    return next_url

# 获取页面里的房源 URL
def get_house_href(mytree):
    href_list = mytree.xpath('//*[@class="info rel"]/p[@class="title"]/a/@href')
    return href_list
    
# 获取下一页的 url
def get_next_page(mytree):  
    next_page = mytree.xpath('//*[@id="rentid_D10_01"]/a[last()-1]/@href')
    # 获取当前页url    
    now_page = mytree.xpath('//*[@id="rentid_D10_01"]/a[@class="pageNow"]/@href')
    # 没有下一页了
    if next_page == now_page:
        return
    return next_page
    
def main():
    URL = "https://hz.zu.fang.com{}"
    get_area()
    for href, area in AREA.items():
        url = URL.format(href)  # 地区的URL
        html = get_response(url)
        # 一个地区
        # 通过获取下一页进行翻页
        while True:
            try:
                next_url = parse_one_page(html, area)
                html = get_response(next_url)
                if html is None:
                    break
            except Exception as e:
                print(e)


if __name__ == '__main__':
    # html = get_response("https://hz.zu.fang.com/house-a0151/i32/")
    # mytree = etree.HTML(html)
    # print(get_house_href(mytree))
    # print(get_next_page(mytree))
    # print(parse_one_page(html, 'xihu'))
    # get_area()
    # print(AREA)
    main()




