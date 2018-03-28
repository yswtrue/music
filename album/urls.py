from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('albums', views.AlbumViewSet)
router.register('musics', views.MusicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
