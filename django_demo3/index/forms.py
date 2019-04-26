from django import forms
from .models import *

# 为 level 控件准备初始化数据
LEVEL_CHOICE = (
    ('1', '好评'), ('2', '中评'), ('3', '差评'),
)

class RemarkForm(forms.Form):
    # 描述一个表示评论内容的表单类
    # 控件1 - 评论标题title - 文本框
    title = forms.CharField(
            label="标题",
            error_messages={
                "required": "Please enter your name"
                            })
    # 控件2 - 电子邮件email - 邮件框
    email = forms.EmailField(label="邮箱")
    # 控件3 - 评论内容message - 多行文本域
    message = forms.CharField(label="内容", widget=forms.Textarea)
    # 控件4 - 评论级别level - 下拉列表
    level = forms.ChoiceField(label="级别", choices=LEVEL_CHOICE,
                              widget=forms.RadioSelect)
    # 控件5 - 是否保存isSaved - 复选框
    isSaved = forms.BooleanField(label="保存")


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Users
#         # fields = "__all__"
#         fields = ["uname", "upwd"]
#         labels = {"uname": "用户名",
#                   "upwd": "登录密码"}


class InfoForm(forms.Form):
    uname = forms.CharField(
        label = "用户名称",
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "请输入用户名称",
            }
        )
    )
    upwd = forms.CharField(
        label = "用户密码",
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入用户密码",
            }
        )
    )
    uemail = forms.CharField(
        label="用户邮箱",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入用户邮箱",
            }
        )
    )


SAVE_CHOICE = (
    ('1', '不保存'), ('2', '一个月'), ('3', '六个月'), ('4', '一年'),
)

class LoginForm(forms.Form):
    uname = forms.CharField(label="用户名称",
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "请输入用户名"
                                }
                            ))
    upwd = forms.CharField(label="用户密码",
                           widget=forms.PasswordInput(
                               attrs={
                                   "placeholder": "请输入密码"
                               }
                           ))
    saveTime = forms.ChoiceField(label="保存时长",
                                 choices=SAVE_CHOICE,
                                 widget=forms.Select())


