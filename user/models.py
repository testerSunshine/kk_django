from django.db import models

# Create your models here.


class user(models.Model):
    """
    用户表
    """
    third_id = models.IntegerField("第三方来源产生的id,e.g:微信", null=True)
    third_type = models.IntegerField("0:未知，1:微信， 2:支付宝", null=True)
    mobile = models.CharField("手机号码", max_length=64, null=True)
    email = models.CharField("邮箱", max_length=64, null=True)
    user_name = models.CharField("用户名", max_length=64, default="看看")
    password = models.CharField("密码", max_length=64, )
    level = models.IntegerField("等级", default=0)
    icon_url = models.CharField("头像", max_length=64, default="")
    user_status = models.IntegerField("0：正常 1：冻结",)
    sex = models.IntegerField("性别 0：女 1：男 2：保密",)
    autograph = models.TextField("个性签名", max_length=2500, null=True)
    birthday = models.CharField("生日", max_length=256, null=True)
    user_create_time = models.DateTimeField("视频创建时间", auto_now=False, auto_now_add=True)
    user_update_time = models.DateTimeField("视频更新时间", auto_now=True, auto_now_add=False)
