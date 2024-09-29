import os
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.conf import settings
import requests
from dotenv import load_dotenv
from API.spotify import get_spotify_client
# from API.rapidapi import artist_data
import sys
from random import randint, random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from random import randint
from django.views.generic import TemplateView
from django.views import View

rapid_key = settings.RAPID_API_KEY


# from .models import Song

# from django.http import HttpResponse
# Create your views here.


# @login_required(login_url="login")
def index(request):
    album_data = latest_albums()
    playlist_data = spotify_playlist()
    artist_data = trending_artist()

    playlist_names = playlist_data['playlist_names']
    playlist_image = playlist_data['playlist_image']
    playlist_id = playlist_data['playlist_id']

    artist_name = artist_data['artist_names']
    artist_image = artist_data['artist_images']
    artist_uri = artist_data['artist_uris']

    sp = get_spotify_client()
    response_playlists = sp.featured_playlists(limit=14)

    context = {
        "playlist_names": playlist_names,
        "playlist_image": playlist_image,
        "playlist_id": playlist_id,
        "artist_name": artist_name,
        "artist_image": artist_image,
        "artist_uri": artist_uri,
        "test": response_playlists,
        **album_data,
    }

    return render(request, "music/index.html", context)


def artist_page(request, artist_link):
    sp = get_spotify_client()
    artist_data_spotipy = sp.artist(artist_link)

    artist_data_name = artist_data_spotipy['name']

    artist_image = next((image['url'] for image in artist_data_spotipy['images'] if image['height'] == 640), None)

    top_tracks = artist_top_tracks(artist_link)["tracks"]
    song_image = artist_top_tracks(artist_link)["image"]

    top_tracks_image = artist_top_tracks(artist_link)

    rapid_response = artist_data_rapid(artist_link)
    banner = rapid_response[0][1]
    if banner is None:
        banner = 'https://placehold.co/600x400?text=RAPID+IS+ASS'


    return render(request, "music/profile.html", context={
        "artist_name": artist_data_name,
        "artist_banner": banner,
        "artist_image": artist_image,
        "top_tracks": top_tracks,
        "song_image": song_image

    })


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

        # defining userdata

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
        # messages.info(request, "Failed to fetch album releases")

    albums = response_new_releases.get('albums', {}).get('items', [])

    if albums:

        # artist 1

        albums_item_1 = albums[0]
        album_data["artist_name_1"] = albums_item_1['artists'][0]['name']
        # album_data["artist_uri_1"] = albums_item_1['artists'][0]['uri']
        album_data["album_name_1"] = albums_item_1['name']
        album_data["album_uri_1"] = albums_item_1["id"]

        for image in albums_item_1['images']:
            if image['height'] == 300:
                artist_image_1 = image['url']
                break

        album_data["artist_image_1"] = artist_image_1

        # artist 2

        albums_item_2 = albums[1]
        album_data["artist_name_2"] = albums_item_2['artists'][0]['name']
        # album_data["artist_uri_2"] = albums_item_2['artists'][0]['uri']
        album_data["album_name_2"] = albums_item_2['name']
        album_data["album_uri_2"] = albums_item_2["id"]

        for image in albums_item_2['images']:
            if image['height'] == 300:
                artist_image_2 = image['url']
                break

        album_data["artist_image_2"] = artist_image_2

        # artist 3

        albums_item_3 = albums[2]
        album_data["artist_name_3"] = albums_item_3['artists'][0]['name']
        # album_data["artist_uri_3"] = albums_item_3['artists'][0]['uri']
        album_data["album_name_3"] = albums_item_3['name']
        album_data["album_uri_3"] = albums_item_3["id"]

        for image in albums_item_3['images']:
            if image['height'] == 300:
                artist_image_3 = image['url']
                break

        album_data["artist_image_3"] = artist_image_3

        # artist 4

        albums_item_4 = albums[3]
        album_data["artist_name_4"] = albums_item_4['artists'][0]['name']
        # album_data["artist_uri_4"] = albums_item_4['artists'][0]['uri']
        album_data["album_name_4"] = albums_item_4['name']
        album_data["album_uri_4"] = albums_item_4["id"]

        for image in albums_item_4['images']:
            if image['height'] == 300:
                artist_image_4 = image['url']
                break

        album_data["artist_image_4"] = artist_image_4

        # artist 5

        albums_item_5 = albums[4]
        album_data["artist_name_5"] = albums_item_5['artists'][0]['name']
        # album_data["artist_uri_5"] = albums_item_5['artists'][0]['uri']
        album_data["album_name_5"] = albums_item_5['name']
        album_data["album_uri_5"] = albums_item_5["id"]

        for image in albums_item_5['images']:
            if image['height'] == 300:
                artist_image_5 = image['url']
                break

        album_data["artist_image_5"] = artist_image_5

        # artist 6

        albums_item_6 = albums[5]
        album_data["artist_name_6"] = albums_item_6['artists'][0]['name']
        # album_data["artist_uri_6"] = albums_item_6['artists'][0]['uri']
        album_data["album_name_6"] = albums_item_6['name']
        album_data["album_uri_6"] = albums_item_6["id"]

        for image in albums_item_6['images']:
            if image['height'] == 300:
                artist_image_6 = image['url']
                break

        album_data["artist_image_6"] = artist_image_6

        return album_data

    else:
        for i in range(6):
            album_data[f"artist_name_{i + 1}"] = "No connection"
            album_data[f"artist_uri_{i + 1}"] = "https://example.com/"
            album_data[f"artist_image_{i + 1}"] = "No connection"


def artist_top_tracks(data):
    urn = data
    sp = get_spotify_client()
    artist_tracks = {}
    # Fetch Top artist tracks

    try:
        response_top_tracks = sp.artist_top_tracks(urn)
    except Exception as e:

        messages.info(request, "Failed to fetch top tracks")

    artist_tracks['tracks'] = [track['name'] for track in response_top_tracks.get('tracks', [])]
    artist_tracks['uri'] = [track['uri'] for track in response_top_tracks.get('tracks', [])]
    artist_tracks['image'] = [
        next((image['url'] for image in track['album']['images'] if image['width'] == 300), None)
        for track in response_top_tracks.get('tracks', [])
    ]
    return artist_tracks


def trending_artist():
    sp = get_spotify_client()

    try:
        random_handler = randint(0, 4)
        if random_handler == 0:
            response_artist = sp.search(q='genre:pop', type='artist', limit=8)
        elif random_handler == 1:
            response_artist = sp.search(q='genre:alt-rock', type='artist', limit=8)
        elif random_handler == 2:
            response_artist = sp.search(q='genre:dance', type='artist', limit=8)
        elif random_handler == 3:
            response_artist = sp.search(q='genre:idm', type='artist', limit=8)
        elif random_handler == 4:
            response_artist = sp.search(q='genre:trip-hop', type='artist', limit=8)
        else:
            pass

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
    playlist_id = [playlist.get('id') for playlist in playlists]

    playlist_data = {
        'playlist_names': playlist_names,
        'playlist_image': urls,
        "playlist_id": playlist_id
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


def artist_data_rapid(data):
    url = "https://spotify-scraper.p.rapidapi.com/v1/artist/overview"

    formatted_data = data.removeprefix("spotify:artist:")

    querystring = {"artistId": formatted_data}

    headers = {
        "x-rapidapi-key": rapid_key,
        "x-rapidapi-host": "spotify-scraper.p.rapidapi.com"
    }

    response_api = requests.get(url, headers=headers, params=querystring)

    response_data = response_api.json()

    artist_info = []

    biography = response_data.get('biography')
    banner = response_data.get('visuals', {}).get('header', [{}])[0].get('url')

    artist_info.append((biography, banner))

    return artist_info


def album_func(request, album_link):
    sp = get_spotify_client()

    response_album_tracks = sp.album_tracks(album_link)
    response_album = sp.album(album_link)

    album_image = response_album.get('images', [])[0].get('url', {})
    album_name = response_album.get('name', {})
    album_artist = response_album.get('artists', [])[0].get('name', {})
    album_release = response_album.get('release_date', {})
    audio = f"{settings.MEDIA_URL}songs/Coat%20I%20Would%20Buy.mp3"
    track_names = []

    for item in response_album_tracks.get('items', []):
        track_name = item.get('name', 'Unknown Track Name')
        track_names.append(track_name)

    # handle song data
    song_arg = track_name + " " + album_artist
    song = get_song(song_arg)

    return render(request, "music/album.html", context={
        "image": album_image,
        "response": response_album,
        "name": album_name,
        "artist": album_artist,
        "track_names": track_names,
        "release_date": album_release,
        "song_data": song,
        "audio": audio,
    })


def playlist_page(request, playlist_link):
    sp = get_spotify_client()
    playlist_response = sp.playlist(playlist_link)

    playlist_name = playlist_response.get('name')
    playlist_description = playlist_response.get('description')
    # playlist_data.append([playlist_response.get('name') for item in items])

    song_names = []
    for item in playlist_response.get('items', []):
        song_name = item.get('name', 'not found')
        song_names.append(song_name)

    Songs = []

    # playlist_data.append((playlist_name, playlist_description))

    return render(request, "music/playlist.html", context={
        "playlist_name": playlist_name,
        "playlist_description": playlist_description,
        "playlist_data": playlist_response,
        "song_names": song_names

    })


def get_song(song_name):
    url = "https://spotify-scraper.p.rapidapi.com/v1/track/download"

    querystring = {"track":song_name}

    headers = {
        "x-rapidapi-key": rapid_key,
        "x-rapidapi-host": "spotify-scraper.p.rapidapi.com"
    }

    response_1 = requests.get(url, headers=headers, params=querystring)
    data = response_1.json()


    if data.get(
            'message') == "You have exceeded the MONTHLY quota for Requests on your current plan, BASIC. Upgrade your plan at https://rapidapi.com/DataFanatic/api/spotify-scraper":
        song_url = os.path.join(settings.MEDIA_ROOT, 'music', 'Coat I Would Buy.mp3')
    else:

        song_url = data.get('youtubeVideo', {}).get('audio', [])[1].get('url')



    return song_url



def music_player(track, artist_player):
    pass


def ajax_handler(request, album_link):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get('title')
        artist = data.get('artist')



        song_data = title + artist

        try:
            song = get_song(song_data)
            return JsonResponse({'success': True, 'song_url': song})
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Song not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})





# def ajax_post_handler(request):
#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         if request.method == 'POST':
#             response = json.loads(request)
#             data = response.get('payload')
#
#
#

