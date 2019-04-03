'''
对单个房源信息进行解析
并存入 mongoDB 数据库中

格式 {title, name, coord, area, infos}
'''
import re
from lxml import etree

class HouseInfos(object):
    def __init__(self, html, area):
        self.html = html
        self.area = area
        self.tree = etree.HTML(html)
    
    def get_house_title(self):
        # 获取房源标题
        title = self.tree.xpath('//*[@class="tab-cont clearfix"]/h1[@class="title"]/text()')
        # print(title)
        if not title:
            title = "未知"
        title = title[0]
        print(title)
        self.house_title = title

    def get_house_name(self):
        # 获取小区名字
        self.name = re.search("houseInfo.*?projname: '(.*?)'", self.html, re.S).group(1)
        if not self.name:
            self.name = "未知"

    def get_house_coord(self):
        '''获取房源经纬度, 暂未数据'''
        pass

    def get_descirbe(self):
        # 获取房源描述
        desc = self.tree.xpath('//*[@class="fyms_con floatl gray3"]/text()')
        if not desc:
            desc = "暂无数据"
        desc = '\n'.join(desc)
        # self.infos["房源描述"] = desc
        print(desc)

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
        # 3.26 获取联系方式
      
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
        # 3.18 更改格式　{title, name, infos}
        # self.house_infos = {'title':self.house_title, 
        #                     'name': self.name, 'infos':self.infos}
        # 3.21 更改格式 {title, name, coord, area, infos}
        self.get_house_coord()
        self.house_infos = {'title':self.house_title, 'name': self.name,
                            'coord': self.coord, 'area':self.area, 'infos':self.infos}

        self.get_basic_info()
        self.get_descirbe()
        self.get_house_pictures()
        self.get_main_infos()
        self.get_rent_price()

        self.get_contact()  # 3.26增加联系方式

        # 3.21 添加房源缩略图，
        self.get_house_thumbnail()
        

    def save_in_mongo(self):
        # 将信息存入mongoDB中
        client = MongoClient("localhost", 27017)
        db = client['house_info']
        myset1 = db['lianjia0326']
        myset1.save(self.house_infos)
        # 更新数据存储格式　{'addr':xx, 'infos':xx}
        # 见update_lianjia

        # 再次更新


if __name__ == '__main__':
    with open('house.html') as f:
        html = f.read()
    house_infos = HouseInfos(html, '西湖')
    house_infos.get_house_title()
    house_infos.get_house_name()
    house_infos.get_descirbe()
    print(house_infos.name)




