from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout_func, name="logout"),
    path('test', views.test, name="test"),
    path('artist/<str:artist_link>/', views.artist_page, name="artist_page"),
    path('album/<str:album_link>/', views.album_func, name="album_func"),
    path('playlist/<str:playlist_link>/', views.playlist_page, name="playlist_page"),

    
    
    
]
