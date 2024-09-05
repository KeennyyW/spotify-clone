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

    album_data = latest_albums()

    return render(request, "music/index.html", album_data)


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
        response_new_releases = sp.new_releases(limit=10)
    except Exception as e:
        
        messages.info(request, "Failed to fetch album releases")

    
    albums = response_new_releases.get('albums', {}).get('items', [])
    
    if albums:
        
        #artist 1

        albums_item = albums[0]
        artist_name = albums_item['artists'][0]['name']
        artist_uri = albums_item['artists'][0]['uri']

        # image

        for image in albums_item['images']:
                if image['height'] == 300:
                    artist_image = image['url']
                    break


        #artist 2

        albums_item_1 = albums[1]
        artist_name_1 = albums_item_1['artists'][0]['name']
        artist_uri_1 = albums_item_1['artists'][0]['uri']
        
        for image in albums_item_1['images']:
                if image['height'] == 300:
                    artist_image_1 = image['url']
                    break

        #artist 3

        albums_item_2 = albums[2]
        artist_name_2 = albums_item_2['artists'][0]['name']
        artist_uri_2 = albums_item_2['artists'][0]['uri']

        # image

        for image in albums_item_2['images']:
                if image['height'] == 300:
                    artist_image_2 = image['url']
                    break


        #artist 4

        albums_item_3 = albums[3]
        artist_name_3 = albums_item_3['artists'][0]['name']
        artist_uri_3 = albums_item_3['artists'][0]['uri']
        
        for image in albums_item_3['images']:
                if image['height'] == 300:
                    artist_image_3 = image['url']
                    break

        #artist 5

        albums_item_4 = albums[4]
        artist_name_4 = albums_item_4['artists'][0]['name']
        artist_uri_1 = albums_item_4['artists'][0]['uri']
        
        for image in albums_item_4['images']:
                if image['height'] == 300:
                    artist_image_4 = image['url']
                    break

    else:
        artist_name = ''

    return render(request, "music/test.html", {
        'artist_tracks': artist_tracks,
        'albums': albums,
        'artist_name': artist_name,
        'artist_uri': artist_uri,
        'artist_image': artist_image,
        'albums_item': albums_item,
        'albums_item_1': albums_item_1, 'artist_name_1': artist_name_1, 'artist_image_1': artist_image_1,
        'albums_item_1': albums_item_2, 'artist_name_2': artist_name_2, 'artist_image_2': artist_image_2,
        'albums_item_1': albums_item_3, 'artist_name_3': artist_name_3, 'artist_image_3': artist_image_3,
        'albums_item_1': albums_item_4, 'artist_name_4': artist_name_4, 'artist_image_4': artist_image_4,
    })



def latest_albums():
    sp = get_spotify_client()
    album_data = {}


    # Fetch New album releases

    try:
        response_new_releases = sp.new_releases(limit=10)
    except Exception as e:
        pass
        #messages.info(request, "Failed to fetch album releases")

    
    albums = response_new_releases.get('albums', {}).get('items', [])


    if albums: 

    #artist 1

        albums_item_1 = albums[0]
        album_data["artist_name_1"] = albums_item_1['artists'][0]['name']
        album_data["artist_uri_1"] = albums_item_1['artists'][0]['uri']

        for image in albums_item_1['images']:
                    if image['height'] == 300:
                        artist_image_1 = image['url']
                        break
                    
        album_data["artist_image_1"] = artist_image_1

    #artist 2 

        albums_item_2 = albums[1]
        album_data["artist_name_2"] = albums_item_2['artists'][0]['name']
        album_data["artist_uri_2"] = albums_item_2['artists'][0]['uri']

        for image in albums_item_2['images']:
                    if image['height'] == 300:
                        artist_image_2 = image['url']
                        break
                    
        album_data["artist_image_2"] = artist_image_2

    #artist 3 

        albums_item_3 = albums[2]
        album_data["artist_name_3"] = albums_item_3['artists'][0]['name']
        album_data["artist_uri_3"] = albums_item_3['artists'][0]['uri']

        for image in albums_item_3['images']:
                    if image['height'] == 300:
                        artist_image_3 = image['url']
                        break
                    
        album_data["artist_image_3"] = artist_image_3

    #artist 4

        albums_item_4 = albums[3]
        album_data["artist_name_4"] = albums_item_4['artists'][0]['name']
        album_data["artist_uri_4"] = albums_item_4['artists'][0]['uri']

        for image in albums_item_4['images']:
                    if image['height'] == 300:
                        artist_image_4 = image['url']
                        break
                    
        album_data["artist_image_4"] = artist_image_4

    #artist 5

        albums_item_5 = albums[4]
        album_data["artist_name_5"] = albums_item_5['artists'][0]['name']
        album_data["artist_uri_5"] = albums_item_5['artists'][0]['uri']

        for image in albums_item_5['images']:
                    if image['height'] == 300:
                        artist_image_5 = image['url']
                        break
                    
        album_data["artist_image_5"] = artist_image_5


    #artist 6

        albums_item_6 = albums[5]
        album_data["artist_name_6"] = albums_item_6['artists'][0]['name']
        album_data["artist_uri_6"] = albums_item_6['artists'][0]['uri']

        for image in albums_item_6['images']:
                    if image['height'] == 300:
                        artist_image_6 = image['url']
                        break
                    
        album_data["artist_image_6"] = artist_image_6


        return album_data 
    
    else: 
         for i in range(6):
              album_data[f"artist_name_{i+1}"] = "No connection"
              album_data[f"artist_uri_{i+1}"] = "https://example.com/"
              album_data[f"artist_image_{i+1}"] = "No connection"

