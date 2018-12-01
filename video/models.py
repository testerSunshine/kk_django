# coding=utf-8
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
    video_author_id = models.IntegerField("视频作者id", )
    video_author_v_id = models.CharField("视频作者wx_id,如果是别的来源，则无此id", max_length=64, null=True)
    video_channel = models.IntegerField("视频来源渠道， 1为糗百，2为b站， 3为其他", null=True)
    video_create_time = models.DateTimeField("视频创建时间", auto_now=False, auto_now_add=True)
    video_update_time = models.DateTimeField("视频更新时间", auto_now=True, auto_now_add=False)


class boxOfficeDay(models.Model):
    """
    单日票房表
    """
    box_office_id = models.IntegerField("影片id", )
    box_office_id_end = models.IntegerField("影片id2", default=0, null=True)
    top = models.IntegerField("排名", null=True)
    video_name = models.CharField("影片名称", max_length=64, default=None)
    top_change = models.IntegerField("影片排名变化", null=True)
    tickets_week = models.CharField("单周票房", max_length=64, null=True)
    tickets_day = models.CharField("单周票房", max_length=64, null=True)
    sequential_update = models.CharField("环比变化", max_length=64, null=True)
    sum_box_office = models.CharField("累计票房", max_length=64, null=True)
    avg_box_office = models.IntegerField("平均票价", null=True)
    avg_show_people = models.IntegerField("场均人数", null=True)
    audience_count = models.IntegerField("人数总和", null=True)
    show_count = models.IntegerField("场次", null=True)
    mouth_index = models.IntegerField("口碑指数", null=True)
    release_days = models.IntegerField("上映天数", null=True)
    box_office_time = models.DateTimeField("影片当天时间", auto_now=True, auto_now_add=False, null=True)
    attendance = models.IntegerField("上座率", null=True)
    offer_seat_percent = models.IntegerField("排座占比", null=True)
    offer_video_percent = models.IntegerField("排片占比", null=True)
    box_percent = models.IntegerField("票房占比", null=True)
    data_channel = models.CharField("数据来源", max_length=32, default="艺恩", null=True)
    box_office_create_time = models.DateTimeField("采集时间", auto_now=True, auto_now_add=False)


class boxOfficeWeek(models.Model):
    """
    单周票房表
    """
    box_office_id = models.IntegerField("影片id", )
    top = models.IntegerField("排名", null=True)
    video_name = models.CharField("影片名称", max_length=64, default=None)
    top_change = models.IntegerField("影片排名变化", null=True)
    tickets_week = models.CharField("单周票房", max_length=64, null=True)
    sequential_update = models.CharField("环比变化", max_length=64, null=True)
    sum_box_office = models.CharField("累计票房", max_length=64, null=True)
    avg_box_office = models.IntegerField("平均票价", null=True)
    avg_show_people = models.IntegerField("场均人数", null=True)
    mouth_index = models.IntegerField("口碑指数", null=True)
    release_days = models.IntegerField("上映天数", null=True)
    attendance = models.IntegerField("上座率", null=True)
    offer_seat_percent = models.IntegerField("排座占比", null=True)
    offer_video_percent = models.IntegerField("排片占比", default="", null=True)
    data_channel = models.CharField("数据来源", max_length=32, default="艺恩", null=True)
    box_office_create_time = models.DateTimeField("采集时间", auto_now=True, auto_now_add=False)


class boxOfficeMonth(models.Model):
    """
    单月票房表
    """
    box_office_id = models.IntegerField("影片id", )
    top = models.IntegerField("排名", null=True)
    video_name = models.CharField("影片名称", max_length=64, default=None, null=True)
    top_change = models.IntegerField("影片排名变化", null=True)
    tickets_week = models.CharField("单周票房", max_length=64, null=True)
    sequential_update = models.CharField("环比变化", max_length=64, null=True)
    sum_box_office = models.CharField("累计票房", max_length=64, null=True)
    avg_box_office = models.IntegerField("平均票价", null=True)
    avg_show_people = models.IntegerField("场均人数", null=True)
    mouth_index = models.IntegerField("口碑指数", null=True)
    release_days = models.IntegerField("上映天数", null=True)
    attendance = models.IntegerField("上座率", null=True)
    offer_seat_percent = models.IntegerField("排座占比", null=True)
    offer_video_percent = models.IntegerField("排片占比", default="", null=True)
    data_channel = models.CharField("数据来源", max_length=32, default="艺恩", null=True)
    box_office_create_time = models.DateTimeField("采集时间", auto_now=True, auto_now_add=False)


class boxOfficeYear(models.Model):
    """
    年度票房表
    """
    box_office_id = models.IntegerField("影片id", null=True)
    top = models.IntegerField("排名", null=True)
    video_name = models.CharField("影片名称", max_length=64, default=None, null=True)
    top_change = models.IntegerField("影片排名变化", null=True)
    tickets_week = models.CharField("单周票房", max_length=64, null=True)
    sequential_update = models.CharField("环比变化", max_length=64, null=True)
    sum_box_office = models.CharField("累计票房", max_length=64, null=True)
    avg_box_office = models.IntegerField("平均票价", )
    avg_show_people = models.IntegerField("场均人数", )
    mouth_index = models.IntegerField("口碑指数", null=True)
    release_days = models.IntegerField("上映天数", null=True)
    attendance = models.IntegerField("上座率", null=True)
    offer_seat_percent = models.IntegerField("排座占比", null=True)
    offer_video_percent = models.IntegerField("排片占比", default="", null=True)
    data_channel = models.CharField("数据来源", max_length=32, default="艺恩")
    box_office_create_time = models.DateTimeField("采集时间", auto_now=True, auto_now_add=False)
    box_office_time = models.DateTimeField("上映天数", auto_now=True, auto_now_add=False)


class videoData(models.Model):
    """
    电影数据
    """
    video_name = models.CharField("影片名称", max_length=64, default=None, )
    video_name_en = models.CharField("影片英文名称", max_length=64, default=None, null=True)
    video_cost = models.IntegerField("制片成本", null=True)
    sum_box_office = models.IntegerField("累计票房", null=True)
    point_box_office = models.IntegerField("点映票房", null=True)
    first_day_box_office = models.IntegerField("首映日票房", null=True)
    first_week_box_office = models.IntegerField("首周票房", null=True)
    first_week_end_box_office = models.IntegerField("首周末票房", null=True)
    video_type = models.CharField("制片类型", max_length=128, null=True)
    video_language = models.CharField("影片语言", max_length=32, null=True )
    video_run_time = models.CharField("片长", max_length=32, null=True)
    director = models.CharField("导演", max_length=32, null=True)
    writers = models.CharField("编剧", max_length=32, null=True)
    actor = models.CharField("演员", max_length=32, null=True)
    actors = models.TextField("演员列表", max_length=50000, null=True)
    summary = models.TextField("剧情简介", max_length=50000, null=True)
    record_company = models.TextField("制作公司", max_length=5000, null=True)
    company_name = models.CharField("发行方", max_length=256, null=True)
    country_name = models.CharField("国家", max_length=256, null=True)
    release_date = models.CharField("发行日期", max_length=32, null=True)
    data_channel = models.CharField("数据来源", max_length=32, default="艺恩")
    box_office_create_time = models.DateTimeField("采集时间", auto_now=True, auto_now_add=False)
    record_id = models.CharField("影片发行记录id", max_length=128, default=None)
    record_area = models.CharField("影片制作区域", max_length=128, default=None)
    record_date = models.CharField("影片制作日期", max_length=32, default=None)
    video_img = models.CharField("影片封面图", max_length=256, default=None)
    video_see_type = models.CharField("影片观看类型", max_length=16, default=None)


class row_piece(models.Model):
    """
    排片数据  地区，认知指数，购票指数，口碑指数，数据来源，采集时间
    """
    video_name = models.CharField("影片名称", max_length=64, default=None)
    buy_ticket_index = models.CharField("购票指数", max_length=32, null=True)
    ren_zhi_index = models.CharField("认知指数", max_length=32, null=True)
    rap_index = models.CharField("口碑指数", max_length=32, null=True)
    weibo_topic_name = models.CharField("微博热门话题", max_length=128, default=None, null=True)
    weibo_topic_red = models.CharField("阅读量", max_length=16, default=None, null=True)
    weibo_topic_forwarding = models.CharField("转发", max_length=16, default=None, null=True)
    weibo_topic_comment = models.CharField("评论数", max_length=16, default=None, null=True)
    data_channel = models.CharField("数据来源", max_length=32, default="艺恩", null=True)
    box_office_create_time = models.DateTimeField("采集时间", auto_now=True, auto_now_add=False, null=True)


class marketing_data(models.Model):
    """
    营销数据 每日物料总数、物料播放量、微博指数、微信指数、百度指数，数据来源，采集时间
    """
    video_name = models.CharField("影片名称", max_length=64, default=None)
    weibo_index = models.CharField("微博指数", max_length=128, null=True)
    weichat_index = models.CharField("微博指数", max_length=128, null=True)
    network_index = models.CharField("网络指数", max_length=128, null=True)
    news_index = models.CharField("网络指数", max_length=128, null=True)
    posters_index = models.CharField("海报指数", max_length=128, null=True)
    trailers_index = models.CharField("片花指数", max_length=128, null=True)
    video_man_num = models.IntegerField("性别男", null=True)
    video_woman_num = models.IntegerField("性别女", null=True)
    video_woman_num_tgl = models.IntegerField("性别偏好度女", null=True)
    video_man_num_tgl = models.IntegerField("性别偏好度男", null=True)
    age_distribution = models.TextField("年龄分布情况", max_length=50000, default=None, null=True)
    province_distribution = models.TextField("地区分布情况", max_length=50000, default=None, null=True)
    data_channel = models.CharField("数据来源", max_length=32, default="艺恩")
    box_office_create_time = models.DateTimeField("采集时间", auto_now=True, auto_now_add=False)


class mouth_word(models.Model):
    """
    口碑数据 电影数据对应的的观众评分，评分人数，短评内容，长评内容，评论时间，评分等级，数据来源，采集时间
    """
    video_name = models.CharField("影片名称", max_length=64, default=None)
    video_type = models.CharField("影片类型", max_length=256, default=None)
    video_release_time = models.CharField("影片上映日期", max_length=64, null=True)
    director = models.CharField("导演", max_length=64, default=None, null=True)
    fra = models.CharField("属于国家", max_length=64, default=None, null=True)
    video_rate = models.CharField("影片评分", max_length=64, default=None, null=True)
    comment_rate = models.CharField("观众评分", max_length=64, default=None, null=True)
    comment_num = models.CharField("评分人数", max_length=64, default=None, null=True)
    comment_content = models.TextField("短评内容", max_length=64, default=None, null=True)
    comment_content_long = models.CharField("长评内容", max_length=64, default=None, null=True)
    comment_content_time = models.CharField("评论时间", max_length=64, default=None, null=True)
    comment_content_lev = models.CharField("评分等级", max_length=64, default=None, null=True)
    comment_id = models.IntegerField("评论id", null=True)
    gender = models.IntegerField("性别", null=True)
    nick_name = models.CharField("评论者名字", max_length=64, default=None, null=True)
    city_name = models.CharField("城市", max_length=64, default=None, null=True)
    comment_time = models.CharField("评论时间", max_length=64, default=None, null=True)
    data_channel = models.CharField("数据来源", max_length=32, default="猫眼")
    box_office_create_time = models.DateTimeField("采集时间", auto_now=True, auto_now_add=False)


class douban_data(models.Model):
    """
    豆瓣电影数据
    """
    video_name = models.CharField("影片名称", max_length=64, default=None)
    rate = models.CharField("评分", max_length=16, default=None, null=True)
    director = models.CharField("导演", max_length=256, default=None)
    casts = models.CharField("演员", max_length=256, default=None)
    connection_url = models.CharField("豆瓣连接", max_length=128, default=None)
    data_channel = models.CharField("数据来源 `", max_length=32, default="艺恩")
    box_office_create_time = models.DateTimeField("采集时间", auto_now=True, auto_now_add=False)