from django.db import models

# Create your models here.
class Users(models.Model):
    uname = models.CharField(max_length=30, verbose_name="姓名")
    upwd = models.CharField(max_length=30, verbose_name="密码")
    uage = models.IntegerField(verbose_name="年龄")
    uemial = models.EmailField(max_length=200, verbose_name="邮箱")

    def __str__(self):
        return self.uname
