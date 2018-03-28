from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = models.Music.objects.all()
    serializer_class = serializers.MusicSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
