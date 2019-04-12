'''
对单个房源信息进行解析
并存入 mongoDB 数据库中

格式 {title, name, coord, area, infos}
'''
import re
from lxml import etree
from pymongo import MongoClient

class HouseInfos(object):
    def __init__(self, html, area):
        self.html = html
        self.area = area
        self.tree = etree.HTML(html)
        self.get_infos()
        self.save_in_mongo()
    
    def get_house_title(self):
        # 获取房源标题
        pass

    def get_house_name(self):
        # 获取小区名字
        pass

    def get_house_coord(self):
        '''获取房源经纬度, 暂未数据'''
        # "coord" : { "longitude" : "xxx", "latitude" : "xxx" }, 
        pass

    def get_descirbe(self):
        # 获取房源描述
        pass

    def get_house_pictures(self):
        # 房源大图列表
        pass

    def get_house_thumbnail(self):
        # 房源缩略图列表
        pass

    def get_basic_info(self):
        # 房源基本信息
        pass
       
    def get_rent_price(self):
        # 获取租金
        pass

    def get_main_infos(self):
        # 获取房源户型、朝向、面积、租赁方式
        pass

    def get_contact(self):
        # 获取经纪人联系方式
        pass

    def get_infos(self):
        # 得到房源信息字典
        self.get_house_title() # 标题
        self.infos = {}  # 信息字典
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
        

    def save_in_mongo(self, dbname, setname):
        # 将信息存入mongoDB中
        client = MongoClient("localhost", 27017)
        db = client[dbname]
        myset1 = db[setname]
        myset1.save(self.house_infos)


if __name__ == '__main__':
    pass




