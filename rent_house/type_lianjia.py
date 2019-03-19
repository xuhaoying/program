#-*- coding:utf-8 -*-
'''
解析链家租房详情信息
使用类封装
'''

import sys
import requests
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient


class HouseInfos(object):
    '''房源信息解析'''

    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(self.html, "lxml")
        self.get_infos()
        self.save_in_mongo()

    def get_house_title(self):
        # 获取房源标题
        title = self.soup.select_one(".content__title")
        # 没有这个类,换种方法
        if not title:
            return 
        # mongoDB 中 key 不能包含'.',此处用 # 暂替
        title = title.get_text()
        if '.' in title:
            title = title.replace(".", "#")
        self.house_title = title

    # 3.18 新增
    def get_house_name(self):
        # 获取小区名字, 得到的是列表
        self.name = re.findall("g_conf.name = '(.*?)'", self.html)
        if self.name:
            self.name = self.name[0]
            
    def get_descirbe(self):
        # 获取房源描述
        desc = self.soup.find(attrs={"data-el":"houseComment"})
        if not desc:
            desc = "暂无数据"
        else:
            desc = desc.get_text()
        self.infos["房源描述"] = desc

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
        self.get_house_title() # 标题
        self.infos = {}  # 信息字典
        # 房源信息 格式-->{addr:标题, infos:信息字典}
        # self.house_infos = {'addr':self.house_title, 'infos':self.infos}

        self.get_house_name()
        # 3.18 更改格式　{title, name, infos}
        self.house_infos = {'title':self.house_title, 
                            'name': self.name, 'infos':self.infos}

        self.get_basic_info()
        self.get_descirbe()
        self.get_house_pictures()
        self.get_main_infos()
        self.get_rent_price()

    def save_in_mongo(self):
        # 将信息存入mongoDB中
        client = MongoClient("localhost", 27017)
        db = client['house_info']
        myset1 = db['lianjia0318']
        myset1.save(self.house_infos)
        # 更新数据存储格式　{'addr':xx, 'infos':xx}
        # 见update_lianjia

        # 再次更新

    
if __name__ == "__main__":
    with open("house_content.html", 'r', encoding="utf-8") as f:
        html = f.read()
    house = HouseInfos(html)
    # print(house.house_infos)

