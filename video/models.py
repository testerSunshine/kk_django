from django.db import models

# Create your models here.


class library(models.Model):
    """
    视频存取库
    """
    video_length = models.CharField("视频时长", max_length=32, default=None, null=True)
    video_title = models.CharField("视频标题", max_length=256, default="", )
    video_path = models.CharField("视频存取路径", max_length=128, default="")
    video_author = models.CharField("视频作者", max_length=64)
    video_author_id = models.IntegerField("视频作者id",)
    video_author_v_id = models.CharField("视频作者wx_id,如果是别的来源，则无此id", max_length=64, null=True)
    video_channel = models.IntegerField("视频来源渠道， 1为糗百，2为b站， 3为其他", null=True)
    video_create_time = models.DateTimeField("视频创建时间", auto_now=False, auto_now_add=True)
    video_update_time = models.DateTimeField("视频更新时间", auto_now=True, auto_now_add=False)