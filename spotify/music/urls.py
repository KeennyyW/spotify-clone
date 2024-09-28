from django.contrib import admin
from django.urls import path
from . import views
#from .views import AjaxHandler

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout_func, name="logout"),
    path('test', views.test, name="test"),
    path('artist/<str:artist_link>/', views.artist_page, name="artist_page"),
    path('album/<str:album_link>/', views.album_func, name="album_func"),
    path('playlist/<str:playlist_link>/', views.playlist_page, name="playlist_page"),
    path('get-song-data/<str:song_name>/', views.get_song, name='get_song'),
    path('play/<str:track>/<str:artist_player>', views.music_player, name='music_player'),
    path('album/<str:album_link>/ajax', views.ajax_handler, name='ajax_handler'),

    
    
    
]
