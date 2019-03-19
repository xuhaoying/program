#-*- coding:utf-8 -*-
'''
解析链家租房详情信息
使用类封装
'''

import sys
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

class HouseInfos(object):
    '''房源信息解析'''

    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, "lxml")
        self.get_house_title() # 标题
        self.infos = {}  # 信息字典
        # 房源信息 格式-->{标题:信息字典}
        self.house_infos = {self.house_title: self.infos}
        self.get_infos()

    def get_house_title(self):
        # 获取房源标题
        title = self.soup.select_one(".content__title")
        # 没有这个类,换种方法
        if not title:
            return
        self.house_title = title.get_text()

    def get_house_pictures(self):
        # 房源大图列表
        picture_list = []
        picture = self.soup.select(".content__article__slide__item img")
        for div in picture:
            picture_list.append(div['src'])
        # 添加至信息字典
        self.infos["房源图片"] = picture_list

    def get_basic_info(self):
        # 房源基本信息
        basic_info = {}
        info_list = self.soup.select(".content__article__info li")
        for info in info_list:
            info = info.get_text()
            if "：" in info:
                tmp = info.split("：")
                basic_info[tmp[0]] = tmp[1]
        # 添加至信息字典
        self.infos.update(basic_info)

        
    def get_rent_price(self):
        # 获取租金
        price = self.soup.select_one(".content__aside--title")
        price = price.get_text()
        # 添加至信息字典
        self.infos["租金"] = price

    def get_main_infos(self):
        # 获取房源户型、朝向、面积、租赁方式
        info = self.soup.select(".content__article__table span")
        main_infos = {}
        for lst in info:
            main_infos[lst.select_one("i")["class"][0]] = lst.get_text()
        # 添加至信息字典
        self.infos.update(main_infos)
 
    def get_infos(self):
        # 得到房源信息字典
        self.get_basic_info()
        self.get_house_pictures()
        self.get_main_infos()
        self.get_rent_price()

    def save_mongoDB(self):
        # 将房源信息存入MongoDB中
        pass


    
if __name__ == "__main__":
    with open("house_content.html", 'r', encoding="utf-8") as f:
        html = f.read()
    house = HouseInfos(html)
    print(house.house_infos)