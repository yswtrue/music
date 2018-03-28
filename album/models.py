from django.db import models

# Create your models here.


class Category(models.Model):
    """专辑分类"""
    name = models.fields.CharField('分类名', max_length=50)
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT, related_name='chindren', blank=True, null=True)


class Album(models.Model):
    """音乐专辑"""
    name = models.fields.CharField('专辑名', max_length=50)
    categories = models.ManyToManyField(Category)


class Music(models.Model):
    """音乐"""
    name = models.fields.CharField('歌曲名', max_length=50)
    albums = models.ManyToManyField(
        Album, related_name='musics', blank=True, null=True)
