from django.contrib import admin
from .models import *


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    # list_display 由属性名称组成的元组或列表
    list_display = ("name", "age", "email")

    # 定义在列表页上能够连接到详情页的字段们
    # 取值必须出现在 list_display 中
    list_display_links = ("name", "email")

    # 定义在列表页中允许被编辑的字段
    # 取值必须出现在 list_display中， 但不能出现在 list_display_links中
    list_editable = ("age",)

    # 定义在列表页的右侧增加过滤器实现快速筛选
    list_filter = ("isActive",)

    # 添加搜索字段
    search_fields = ("name", "email")

    # fields = ("name", "email", "age")
    # 在详情页中对字段进行分组
    # fieldsets 不能和 fields 属性共存
    fieldsets = (
        # 分组1  name age
        ("基本选项", {"fields":("name", "age")}),
        # 分组2  email, isActive   
        ("高级选项", {
            "fields":("email", "isActive"),
            "classes": ("collapse",),
            }),
    )


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "publicate_date")
    # 指定日期分层选择器
    # 取值必须为 DateField 
    date_hierarchy = "publicate_date"
    # 在详情页中指定要显示的字段以及显示的顺序
    # 由属性名组成的列表或元组，顺序决定了显示顺序
    fields = ("publicate_date", "title", "publisher")
    

class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "city")
    list_editable = ("address", "city")
    list_filter = ("city", "country")
    search_fields = ("name", "website")
    fieldsets = (
        ("基本选项", {
            "fields": ("name", "address", "city")
        }),
        ("高级选项", {
            "fields":("country", "website"),
            "classes": ("collapse",)
        })
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Wife)




