# coding=utf-8
from time import timezone

from rest_framework import serializers
from video.models import library


class videoSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        """
        视频连接转化
        :param instance:
        :return:
        """
        ret = super(videoSerializer, self).to_representation(instance)
        ret["video_path"] = "/media" + ret["video_path"]
        return ret

    class Meta:
        model = library
        fields = ("video_length",
                  "video_title",
                  "video_path",
                  "video_author",
                  "video_author_id",
                  "video_author_v_id",
                  "video_channel",
                  "id",)

