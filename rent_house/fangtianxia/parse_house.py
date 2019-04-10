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
        title = self.tree.xpath('//*[@class="tab-cont clearfix"]/h1[@class="title"]/text()')
        # print(title)
        if not title:
            title = "未知"
        title = title[0]
        # print(title)
        self.house_title = title

    def get_house_name(self):
        # 获取小区名字
        self.name = re.search("houseInfo.*?projname: '(.*?)'", self.html, re.S).group(1)
        if not self.name:
            self.name = "未知"

    def get_house_coord(self):
        '''获取房源经纬度, 暂未数据'''
        # "coord" : { "longitude" : "xxx", "latitude" : "xxx" }, 
        coord = re.search("houseInfo = {.*?codex:.*?'(.*?)'.*?codey:.*?'(.*?)'.*?};", 
                        self.html, re.S)
        self.longitude = str(coord.group(1))  # 经度
        self.latitude = str(coord.group(2))   # 维度
        self.coord = {"longitude": self.longitude, "latitude": self.latitude}
        # print(self.coord)

    def get_descirbe(self):
        # 获取房源描述
        desc = self.tree.xpath('//*[@class="fyms_con floatl gray3"]/text()')
        if not desc:
            desc = "暂无数据"
        desc = '\n'.join(desc)
        self.infos["房源描述"] = desc
        # print(desc)

    def get_house_pictures(self):
        # 房源大图列表
        picture_list = self.tree.xpath('//*[@class="bigImg"]/img/@src')
        # print(picture_list)
        # 添加至信息字典
        self.infos["房源图片"] = picture_list

    def get_house_thumbnail(self):
        # 房源缩略图列表
        thumbnail_list = self.tree.xpath('//*[@class="litImg"]/li/img/@src')
        # print(thumbnail_list)
        self.infos["房源缩略图"] = thumbnail_list

    def get_basic_info(self):
        # 房源基本信息
        basic_info = {}
        basic_info['楼层'] = re.search('<div class="trl-item1 w182">.*?"tt">(.*?)</div>.*?楼层.*?</div>', self.html, re.S).group(1) 

        basic_info['租期']  = "暂无数据"
        basic_info['发布日期'] = self.tree.xpath('//*[@class="gray9 fybh-zf"]/span/text()')[1]
        basic_info['燃气'] = "暂无数据"
        basic_info['车位'] = "暂无数据"
        basic_info['用水'] = "民水"
        basic_info['用电'] = "民电"
        basic_info['入住'] = "随时入住"
        basic_info['电梯'] = "暂无数据"
        basic_info['采暖'] = "暂无数据"
        basic_info['看房'] = "需提前预约"
        # print(basic_info)
        # 添加至信息字典
        self.infos.update(basic_info)

    def get_rent_price(self):
        # 获取租金
        price_group = re.search('<div class="trl-item sty1"><i>(.*?)</i>(.*?)</div>', self.html, re.S) 
        price = price_group.group(1) + price_group.group(2)
        # 添加至信息字典
        self.infos["租金"] = price

    def get_main_infos(self):
        # 获取房源户型、朝向、面积、租赁方式
        main_infos = {}
        main_infos['typ'] = re.search('<div class="trl-item1 w182">.*?"tt">(.*?)</div>.*?户型.*?</div>', self.html, re.S).group(1)  # 户型
        main_infos['house'] = re.search('<div class="trl-item1 w146">.*?"tt">(.*?)</div>.*?出租方式.*?</div>', self.html, re.S).group(1)  # 租赁方式
        main_infos['orient'] = re.search('<div class="trl-item1 w146">.*?"tt">(.*?)</div>.*?朝向.*?</div>', self.html, re.S).group(1)  # 朝向
        main_infos['area']  = re.search('<div class="trl-item1 w132".*?"tt">(.*?)</div>.*?建筑面积</div>', self.html, re.S).group(1) # 面积      
        # 添加至信息字典
        self.infos.update(main_infos)

    def get_contact(self):
        # 获取经纪人联系方式
        re_con = re.search("houseInfo = {.*?agentName:.*?'(.*?)'.*?agentMobile:.*?'(.*?)'.*?};", self.html, re.S)
        name = re_con.group(1)
        phone = re_con.group(2)
        contact = {'name': name, 'phone':phone} 
        # print(contact)
        self.infos['联系方式'] = contact

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
        

    def save_in_mongo(self):
        # 将信息存入mongoDB中
        client = MongoClient("localhost", 27017)
        db = client['house_info']
        myset1 = db['fangtianxia']
        myset1.save(self.house_infos)


if __name__ == '__main__':
    with open('house.html') as f:
        html = f.read()
    house_infos = HouseInfos(html, '西湖')
    # house_infos.get_house_title()
    # house_infos.get_house_name()
    # house_infos.get_descirbe()
    # print(house_infos.name)
    # house_infos.get_house_pictures()
    # house_infos.get_house_thumbnail()
    # house_infos.get_house_coord()
    # house_infos.get_basic_info()
    # house_infos.get_contact()
    # house_infos.save_in_mongo()




