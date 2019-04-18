"""
实现 topic 程序包的初始化操作
"""
from flask import Blueprint


topic = Blueprint("topic", __name__)

from . import views

