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
    name = models.CharField(max_length=30, verbose_name="出版社名称")
    address = models.CharField(max_length=100, verbose_name="地址")
    city = models.CharField(max_length=50, verbose_name="城市")
    country = models.CharField(max_length=30, verbose_name="国家")
    website = models.URLField(verbose_name="网址")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField(
            max_length=50, db_index=True,
            verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(null=True,
            verbose_name="邮箱")
    isActive = models.BooleanField(default=True,
            verbose_name="激活")
    
    publishers = models.ManyToManyField(Publisher)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name="书籍名称")
    publicate_date = models.DateField(verbose_name="出版日期")
    publisher = models.ForeignKey(Publisher, None, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name


class Wife(models.Model):
    wname = models.CharField(max_length=30, verbose_name="姓名")
    wage = models.IntegerField(verbose_name="年龄")
    author = models.OneToOneField(Author, None, verbose_name="丈夫")
 

    def __str__(self):
        return self.wname
    class Meta:
        db_table = 'wife'
        verbose_name = "夫人"
        verbose_name_plural = verbose_name


