"""
实现 users 程序包的初始化操作
"""

from flask import Blueprint

users = Blueprint("users", __name__)

from . import views