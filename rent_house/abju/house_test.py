#-*- coding:utf-8 -*-

import sys
import time
import requests
from bs4 import BeautifulSoup
from config import *
from anjuke import AnJuKe


class HouseSpider(object):
	'''爬取网页信息'''
	def __init__(self, url):
		self.url = url

	def get_response(self, url):
		'''发送请求并获取数据'''
		try:
			time.sleep(1)
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

		list_item = soup.select(".zu-info a")
		# 提取房源详情页url
		house_href = []
		for house in list_item:
			href = house['href']
			if 'fangyuan' in href:
				house_href.append(href)
		return house_href

	# 给数据库传入地区名， 按地区存储
	def get_one_page(self, url, area):
		# 获取一个列表页面
		html = self.get_response(url)
		house_href = self.get_href(html)
		# print(house_href)

		for href in house_href:
			html = self.get_response(href)
			house = AnJuKe(html, area)
	
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





