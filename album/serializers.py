from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    musics = MusicSerializer(many=True, read_only=True)
    category_ids = serializers.ListField(write_only=True, default=[])
    music_ids = serializers.ListField(write_only=True, default=[])

    class Meta:
        model = models.Album
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        category_ids = validated_data.pop('category_ids')
        music_ids = validated_data.pop('music_ids')
        categories = models.Category.objects.filter(pk__in=category_ids)
        musics = models.Music.objects.filter(pk__in=music_ids)
        album = super().create(validated_data)
        album.categories.set(categories)
        album.musics.set(musics)
        return album

    def update(self, instance, validated_data):
        category_ids = validated_data.pop('category_ids')
        music_ids = validated_data.pop('music_ids')
        categories = models.Category.objects.filter(pk__in=category_ids)
        musics = models.Music.objects.filter(pk__in=music_ids)
        album = super().update(instance, validated_data)
        album.categories.set(categories)
        album.musics.set(musics)
        return album
