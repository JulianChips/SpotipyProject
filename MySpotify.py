import spotipy
import json
from api_keys import client_id, client_secret
from spotipy.oauth2 import SpotifyClientCredentials

#Pass keys into credentials manager for the Spotify Web API
client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_artist_uri(artist):
    """
    get_artist_uri(artist)
    Returns the first artist uri for the arist
    """
    artist_uri = spotify.search(artist,type='artist')
    artist_uri = artist_uri.get("artists")["items"][0]["uri"]
    return artist_uri
def get_album_uri(album, artist):
    """
    get_album_uri(album, artist)
    Returns album uri for first album that contains album name.
    Uses get_artist_uri() to get artist uri for album search.
    """
    artist_uri = get_artist_uri(artist)
    album_uri = spotify.artist_albums(artist_uri,album_type="album")
    counter = -1
    for item in album_uri.get("items"):
        counter = counter + 1
        if album in item.get("name"):
            break
    album_uri = album_uri.get("items")[counter]["uri"]
    return album_uri
def get_song_uri(song, album, artist):
    """
    get_song_uri(song,album,artist)
    """
