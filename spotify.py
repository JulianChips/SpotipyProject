# pip install spotipy
import spotipy
from api_keys import client_id, client_secret
from spotipy.oauth2 import SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_song():
    pass
def get_album():
    pass
def get_artist(name):
    results = spotify.search(q='artist:' + name, type='artist')
    return results

get_artist("SZA")