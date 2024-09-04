import spotipy
from django.conf import settings
from spotipy.oauth2 import SpotifyClientCredentials


#handle auth


def get_spotify_client():
    auth_manager = SpotifyClientCredentials(
        client_id=settings.SPOTIFY_CLIENT_ID, 
        client_secret=settings.SPOTIFY_CLIENT_SECRET
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp


sp = get_spotify_client()



