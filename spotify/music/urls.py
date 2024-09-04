from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout_func, name="logout"),
    path('artist', views.artist_top_tracks, name="artist_top_tracks"),
    
    
    
]
