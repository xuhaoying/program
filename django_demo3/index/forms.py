from django import forms


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
    level = forms.ChoiceField(label="级别", choices=LEVEL_CHOICE)
    # 控件5 - 是否保存isSaved - 复选框
    isSaved = forms.BooleanField(label="保存")


class RegisterForm(forms.Form):
    uname = forms.CharField(label="用户名")
    upwd = forms.CharField(label="密码")
    uage = forms.IntegerField(label="年龄")
    uemial = forms.EmailField(label="邮箱")

