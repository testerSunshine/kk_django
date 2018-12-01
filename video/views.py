# coding=utf-8
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView

from video.models import library
from video.serializers import videoSerializer


class videoLibraryListView(ListCreateAPIView):
    """
    视频获取,每次十条
    """
    def get_queryset(self):
        query_set = library.objects.order_by("-id")[:10]
        print(query_set)
        return query_set

    serializer_class = videoSerializer
