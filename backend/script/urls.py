from django.urls import path
from .views import song_tags

urlpatterns = [
    path('song-tags/', song_tags, name='song-tags'),
]
