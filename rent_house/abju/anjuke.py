#-*- coding:utf-8 -*-

'''
解析安居客租房详情信息
使用类封装
'''

import requests
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient


class AnJuKe(object):
    '''房源信息解析'''

    def __init__(self, html, area):
        self.html = html
        self.area = area 
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

    def get_house_name(self):
        # 获取小区名字, 得到的是列表
        self.name = re.search("g_conf.name = '(.*?)'", self.html).group(1)
        if not self.name:
            self.name = "未知"

    def get_house_coord(self):
        # 获取房源经纬度 
        coord = re.search("g_conf.coord = {.*?longitude:.*?'(.*?)'.*?latitude:.*?'(.*?)'.*?};", 
                        self.html, re.S)
        self.longitude = str(coord.group(1))  # 经度
        self.latitude = str(coord.group(2))   # 维度
        self.coord = {"longitude": self.longitude, "latitude": self.latitude}

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

    def get_house_thumbnail(self):
        # 房源缩略图列表
        thumbnail_list = []
        data = self.soup.select(".content__thumb--box li img")
        for img in data:
            thumbnail_list.append(img['src'])
        self.infos["房源缩略图"] = thumbnail_list

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

    def get_contact(self):
        name = self.soup.select('.desc .name')[0].get_text()
        phone = self.soup.select('.desc .phone')[0].get_text()
      
        contact = {'name': name, 'phone':phone} 
        self.infos['联系方式'] = contact

    def get_infos(self):
        # 得到房源信息字典
        self.get_house_title() # 标题
        self.infos = {}  # 信息字典
        # 房源信息 格式-->{addr:标题, infos:信息字典}
        # self.house_infos = {'addr':self.house_title, 'infos':self.infos}

        self.get_house_name()
        self.get_house_coord()
        self.house_infos = {'title':self.house_title, 'name': self.name,
                            'coord': self.coord, 'area':self.area, 'infos':self.infos}

        self.get_basic_info()
        self.get_descirbe()
        self.get_house_pictures()
        self.get_main_infos()
        self.get_rent_price()

        self.get_contact()  

        self.get_house_thumbnail()
        

    def save_in_mongo(self):
        # 将信息存入mongoDB中
        client = MongoClient("localhost", 27017)
        db = client['house_info']
        myset1 = db['anjuke0326']
        myset1.save(self.house_infos)


    
if __name__ == "__main__":
    with open("anju", 'r', encoding="utf-8") as f:
        html = f.read()
    house = AnJuKe(html, "xihu")


