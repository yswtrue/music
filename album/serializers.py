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


class CategoryIdSerializer(serializers.PrimaryKeyRelatedField):
    queryset = models.Category.objects.all()

    class Meta:
        models = models.Category


class MusicIdSerializer(serializers.PrimaryKeyRelatedField):
    queryset = models.Music.objects.all()

    class Meta:
        models = models.Music


class AlbumSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    musics = MusicSerializer(many=True, read_only=True)

    class Meta:
        model = models.Album
        fields = ['name', 'categories', 'musics']

    def create(self, validated_data):
        category_ids = validated_data.pop('category_ids')
        music_ids = validated_data.pop('music_ids')
        categories = []
        for category_id in category_ids:
            category = models.Category.objects.get(pk=category_id)
            categories.append(category)
        album = super().create(validated_data)
        album.categories.set(categories)
        return album

    def update(self, instance, validated_data):
        category_ids = validated_data.pop('category_ids')
        music_ids = validated_data.pop('music_ids')
        categories = []
        for category_id in category_ids:
            category = models.Category.objects.get(pk=category_id)
            categories.append(category)
        album = super().update(instance, validated_data)
        album.categories.set(categories)
        return album
