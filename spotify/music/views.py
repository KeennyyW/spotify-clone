from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout, authenticate, login
from django.conf import settings
import requests
from dotenv import load_dotenv
from API.spotify import get_spotify_client
import sys

#from django.http import HttpResponse  
# Create your views here.


# @login_required(login_url="login")
def index(request):
    album_data = latest_albums()
    playlist_data = spotify_playlist()
    artist_data = trending_artist()

    playlist_names = playlist_data['playlist_names']
    playlist_image = playlist_data['playlist_image']

    artist_name = artist_data['artist_names']
    artist_image = artist_data['artist_images'] 
    artist_uri = artist_data['artist_uris'] 

    context = {
        "playlist_names": playlist_names,
        "playlist_image": playlist_image,
        "artist_name": artist_name,
        "artist_image": artist_image,
        "artist_uri": artist_uri,
        **album_data,
    }

    return render(request, "music/index.html", context)




def artist_page(request, artist_link):
     sp = get_spotify_client()
     artist_data = sp.artist(artist_link)

     
     
     return render(request, "music/profile.html",)
     


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
        album_data["album_name_1"] = albums_item_1['name']

        for image in albums_item_1['images']:
                    if image['height'] == 300:
                        artist_image_1 = image['url']
                        break
                    
        album_data["artist_image_1"] = artist_image_1

    #artist 2 

        albums_item_2 = albums[1]
        album_data["artist_name_2"] = albums_item_2['artists'][0]['name']
        album_data["artist_uri_2"] = albums_item_2['artists'][0]['uri']
        album_data["album_name_2"] = albums_item_2['name']

        for image in albums_item_2['images']:
                    if image['height'] == 300:
                        artist_image_2 = image['url']
                        break
                    
        album_data["artist_image_2"] = artist_image_2

    #artist 3 

        albums_item_3 = albums[2]
        album_data["artist_name_3"] = albums_item_3['artists'][0]['name']
        album_data["artist_uri_3"] = albums_item_3['artists'][0]['uri']
        album_data["album_name_3"] = albums_item_3['name']

        for image in albums_item_3['images']:
                    if image['height'] == 300:
                        artist_image_3 = image['url']
                        break
                    
        album_data["artist_image_3"] = artist_image_3

    #artist 4

        albums_item_4 = albums[3]
        album_data["artist_name_4"] = albums_item_4['artists'][0]['name']
        album_data["artist_uri_4"] = albums_item_4['artists'][0]['uri']
        album_data["album_name_4"] = albums_item_4['name']

        for image in albums_item_4['images']:
                    if image['height'] == 300:
                        artist_image_4 = image['url']
                        break
                    
        album_data["artist_image_4"] = artist_image_4

    #artist 5

        albums_item_5 = albums[4]
        album_data["artist_name_5"] = albums_item_5['artists'][0]['name']
        album_data["artist_uri_5"] = albums_item_5['artists'][0]['uri']
        album_data["album_name_5"] = albums_item_5['name']

        for image in albums_item_5['images']:
                    if image['height'] == 300:
                        artist_image_5 = image['url']
                        break
                    
        album_data["artist_image_5"] = artist_image_5


    #artist 6

        albums_item_6 = albums[5]
        album_data["artist_name_6"] = albums_item_6['artists'][0]['name']
        album_data["artist_uri_6"] = albums_item_6['artists'][0]['uri']
        album_data["album_name_6"] = albums_item_6['name']

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



def artist_top_tracks(request):
    urn = 'spotify:artist:1g8HCTiMwBtFtpRR9JXAZR'
    sp = get_spotify_client()
    artist_tracks = {}
    # Fetch Top artist tracks

    try:
        response_top_tracks = sp.artist_top_tracks(urn)
    except Exception as e:
        
        messages.info(request, "Failed to fetch top tracks")
        
    artist_tracks['tracks'] = [track['name'] for track in response_top_tracks.get('tracks', [])]

    return artist_tracks



def trending_artist():
    sp = get_spotify_client()

    try:
        
        response_artist = sp.search(q='genre:pop', type='artist', limit=8)

        
        artists = response_artist.get('artists', {}).get('items', [])

        
        artist_names = []
        artist_images = []
        artist_uris = []

        
        for artist in artists:
            name = artist.get('name')
            images = artist.get('images', [])
            image_url = images[0].get('url') if images else None  
            artist_uri = artist.get('uri')

            
            artist_names.append(name)
            artist_images.append(image_url)
            artist_uris.append(artist_uri)

        
        artist_info_list = {
            'artist_names': artist_names,
            'artist_images': artist_images,
            'artist_uris': artist_uris,
        }

    except Exception as e:
        print(e)
        artist_info_list = {}  

    return artist_info_list




def spotify_playlist():
    sp = get_spotify_client()
    response_playlists = sp.featured_playlists(limit=14)

    playlists = response_playlists.get('playlists', {}).get('items', [])
    playlist_names = [playlist.get('name') for playlist in playlists]       
    playlist_image_data = [playlist.get('images') for playlist in playlists] 
    urls = [item[0]['url'] for item in playlist_image_data]



    playlist_data = {
        'playlist_names': playlist_names,
        'playlist_image': urls
    }

    return playlist_data

def artist(): 
     sp = get_spotify_client()
     urn = 'spotify:artist:1g8HCTiMwBtFtpRR9JXAZR'
     response_artist = sp.artist(urn) 

     return response_artist


def test(request): 
    sp = get_spotify_client()
    response_playlists = sp.featured_playlists(limit=14) 

    playlists = response_playlists.get('playlists', {}).get('items', [])
    playlist_names = [playlist.get('name') for playlist in playlists]       
    playlist_image_data = [playlist.get('images') for playlist in playlists] 
    
    
    urls = [item[0]['url'] for item in playlist_image_data]

    artist_data = artist()
    

    return render(request, "music/test.html", {
         "playlist": artist_data,
         
         
    })


