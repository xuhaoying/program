#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
使用 request 模块请求猫眼电影排行100数据
用正则表达式提取主要信息
并存储到 MySQL 数据库中
'''

import requests
from requests.exceptions import RequestException
import re
import pymysql

# 猫眼电影排行榜的URL
URL = "https://maoyan.com/board/4?offset={}"

# 获取单个页面源码
def get_one_page(url):
    try:
        response = requests.get(url)
        # 获取成功，返回数据
        if response.status_code == 200:
            return response.content.decode("utf8")
        return None
    except RequestException:
        return None

# 使用正则解析页面信息, 获取具体数据
def parse_one_page(html):
    # 标题 图片 主演 上映时间 评分
    pattern_string = '<dd>.*?title="(.*?)".*?data-src="(.*?)".*?' + \
        'star">(.*?)</p>.*?releasetime">(.*?)</p>.*?' + \
        'integer">(.*?)</i><i .*?fraction">(.*?)</i>.*?</dd>'
    pattern = re.compile(pattern_string, re.S)
    # 信息列表
    data_list = re.findall(pattern, html)
    return data_list

# 摘取一个的信息
def get_one_info(lst):
    for data in lst:
        # print(data)
        infos = [data[i].strip() for i in range(len(data)-2)]
        infos += [data[-2]+data[-1]]
        save_data(info)
        

# 保存电影信息至 MySQL
def save_data(info):
    # 连接数据库
    db = pymysql.connect("localhost", 3306, "root", "123456", "test", charset="utf8")

def main():
    for page in range(0, 10, 10):
        url = URL.format(page)
        html = get_one_page(url)
        lst = parse_one_page(html)
        get_one_info(lst)


if __name__ == "__main__":
    main()
