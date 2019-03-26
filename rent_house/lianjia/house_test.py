#-*- coding:utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup

from type_lianjia import *
import time


HEADERS = {
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

# area:page  地区：页数
AREA = {'xihu':100, 'xiacheng':69, 'jianggan':100, 'gongshu':100, 
		'shangcheng':39, 'binjiang':73, 'yuhang':100, 'xiaoshan':100}
URL = "https://hz.lianjia.com/zufang/{}/pg{}/"


class HouseSpider(object):
	'''爬取网页信息'''
	def __init__(self, url):
		self.url = url

	def get_response(self, url):
		'''发送请求并获取数据'''
		try:
			# time.sleep(1)
			response = requests.get(url, headers=HEADERS)

			if response.status_code != 200:
				# sys.exit("失败,未得到响应")
				return 
			html = response.content.decode("utf-8")
			return html
		except Exception as e:
			print("error", e)

	def get_href(self, html):
		'''获取房源详情页的链接'''
		soup = BeautifulSoup(html, "lxml")

		list_item = soup.select(".content__list--item--aside")
		# 提取房源详情页url
		house_href = []
		for house in list_item:
			house_href.append(house["href"])
		return house_href

	# 给数据库传入地区名， 按地区存储
	def get_one_page(self, url, area):
		# 获取一个列表页面
		html = self.get_response(url)
		house_href = self.get_href(html)
		# print(house_href)

		for href in house_href:
			if "apartment" in href:
				# print("尚未解析")
				continue
			href = "https://hz.lianjia.com" + href
			html = self.get_response(href)
			house = HouseInfos(html, area)
	
	def start(self):
		for area, page in AREA.items():
			for i in range(1, page+1):
				url = self.url.format(area, i)
				try:
					self.get_one_page(url, area)
				except Exception as e:
					print("error", e)


if __name__ == "__main__":
	house = HouseSpider(URL)
	house.start()



