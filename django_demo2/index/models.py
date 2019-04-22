from django.db import models

# Create your models here.
# Django 允许省略自增主键的声明
class Publisher(models.Model):
    """
    创建一个实体类 Publisher(出版社信息)
    
    :name: 出版社名称 str
    :address: 出版社地址 str
    :city: 出版社所在城市 str
    :country: 出版社所在国家 str
    :website: 网址 str
    """
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    website = models.URLField()


class Author(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    age = models.IntegerField()
    email = models.EmailField(null=True)
    isActive = models.BooleanField(default=True)

class Book(models.Model):
    title = models.CharField(max_length=50)
    publicate_date = models.DateField()