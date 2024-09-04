from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout, authenticate, login
from django.conf import settings
import base64
import requests
from dotenv import load_dotenv
from API.spotify import get_spotify_client
import sys

#from django.http import HttpResponse  
# Create your views here.






# @login_required(login_url="login")
def index(request):
    return render(request, "music/index.html")


def login(request):
    if request.method == "POST":
        
        # gets username and password via POST data

        username = request.POST.get("username") 
        password = request.POST.get("password")

        # checks if user is already registered 

        user = authenticate(request, username=username, password=password)

        # if the user exists they will be logged in and redirected

        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "User not found")
            return redirect("login")
        
    else:
        return render(request, "music/login.html")

def signup(request):
    if request.method == "POST":

        #defining userdata

        username = request.POST.get("username") 
        email = request.POST.get("email") 
        password = request.POST.get("password") 
        password2 = request.POST.get("password2") 

        # check if password is the same

        if password2 == password:

            # check if the email or the username is already in the database

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect("signup")
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect("signup")
            
            # creates new user 

            else: 
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
            
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect("/")
        else: 
            messages.info(request, "Password Not Matching")
            return redirect("signup")

    else:
        return render(request, "music/signup.html")


@login_required(login_url="login")
def logout_func(request):
    auth.logout(request)
    return redirect("signup")



def logout():
    pass

def artist_top_tracks(request):
    urn = 'spotify:artist:1g8HCTiMwBtFtpRR9JXAZR'
    sp = get_spotify_client()

    # Fetch Top artist tracks

    try:
        response_top_tracks = sp.artist_top_tracks(urn)
    except Exception as e:
        
        messages.info(request, "Failed to fetch top tracks")
        
    artist_tracks = [track['name'] for track in response_top_tracks.get('tracks', [])]

    # Fetch New album releases

    try:
        response_new_releases = sp.new_releases(limit=5)
    except Exception as e:
        
        messages.info(request, "Failed to fetch album releases")

    
    albums = response_new_releases.get('albums', {}).get('items', [])
    
    if albums:
        
        albums_item = albums[0]
        artist_name = albums_item['artists'][0]['name']
        artist_uri = albums_item['artists'][0]['uri']

        for image in albums_item['images']:
                if image['height'] == 640:
                    artist_image = image['url']
                    break
    else:
        artist_name = ''

    return render(request, "music/test.html", {
        'artist_tracks': artist_tracks,
        'albums': albums,
        'artist_name': artist_name,
        'artist_uri': artist_uri,
        'artist_image': artist_image
    })







# tree = {
#     'href': 'https://api.spotify.com/v1/browse/new-releases?offset=0&limit=1',
#     'items': [
#         {
#             'album_type': 'album',
#             'artists': [
#                 {
#                     'external_urls': {'spotify': 'https://open.spotify.com/artist/6CP5wWvO8oIxedESJNCN4H'},
#                     'href': 'https://api.spotify.com/v1/artists/6CP5wWvO8oIxedESJNCN4H',
#                     'id': '6CP5wWvO8oIxedESJNCN4H',
#                     'name': 'Ski Aggu',
#                     'type': 'artist',
#                     'uri': 'spotify:artist:6CP5wWvO8oIxedESJNCN4H'
#                 }
#             ],
#             'available_markets': ['AT', 'CH', 'DE'],
#             'external_urls': {'spotify': 'https://open.spotify.com/album/1qGEpCF1NA9ToIocKI4xVK'},
#             'href': 'https://api.spotify.com/v1/albums/1qGEpCF1NA9ToIocKI4xVK',
#             'id': '1qGEpCF1NA9ToIocKI4xVK',
#             'images': [
#                 {
#                       'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02ec72528d208817b039aabfda', 'width': 300},
#                 {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851ec72528d208817b039aabfda', 'width': 64},
#                 {'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273ec72528d208817b039aabfda', 'width': 640}
#             ],
#             'name': 'Wilmersdorfs Kind',
#             'release_date': '2024-08-30',
#             'release_date_precision': 'day',
#             'total_tracks': 16,
#             'type': 'album',
#             'uri': 'spotify:album:1qGEpCF1NA9ToIocKI4xVK'
#         }
#     ],
#     'limit': 1,
#     'next': 'https://api.spotify.com/v1/browse/new-releases?offset=1&limit=1',
#     'offset': 0,
#     'previous': None,
#     'total': 100
# }

