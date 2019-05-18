import os
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

#Pass keys into credentials manager for the Spotify Web API
client_credentials_manager = SpotifyClientCredentials(os.environ["SPOTIFY_CLIENT"],os.environ["SPOTIFY_SECRET"])
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
def update_credentials(my_id,secret):
	client_credentials_manager = SpotifyClientCredentials(my_id,secret)
	spotify = spotipy.Spotify(client_credentials_manager)

def get_artist_uri(artist):
    """
    get_artist_uri(artist)
    Returns the first artist uri for the artist
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
        if album.lower() in item.get("name").lower():
            break
    album_uri = album_uri.get("items")[counter]["uri"]
    return album_uri
def get_song_uri(song, album, artist):
    """
    get_song_uri(song,album,artist)
    """
    album_uri = get_album_uri(album, artist)
    song_uri = spotify.album_tracks(album_uri)
    counter = -1
    for item in song_uri.get("items"):
    	counter = counter + 1
    	if song.lower() in item.get("name").lower():
    		break
    song_uri = song_uri.get("items")[counter]["uri"]
    return song_uri
def get_song_features(song_uri):
	"""
	get_song_uri(song_uri)

	Returns the audio features for a song in JSON format given its uri.
	"""
	song_features = spotify.audio_features(song_uri)
	return song_features
def get_profile():
	"""
	get_profile()

	Returns information about your Spotify Profile
	"""
def get_playlist(playlist):
	"""
	get_playlist(playlist)

	Returns playlist information from your profile.
	"""

# artist = input("What Artist? ")
# album = input("What Album? ")
# song = input("What Song? ")

# print(get_song_features(get_song_uri(song,album, artist)))