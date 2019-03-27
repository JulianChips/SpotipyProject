#Install package for Spotipy wrapper
# pip install spotipy

#import dependencies
import spotipy
import json
from api_keys import client_id, client_secret
from spotipy.oauth2 import SpotifyClientCredentials

#Pass keys into credentials manager for the Spotify Web API
client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
#Generate Instance of the spotipy.Spotify class
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#Get search results for Kendrick Lamar
results = spotify.search('Kendrick Lamar',type='artist')

#Get top result of search
top_result = results.get("artists")["items][0]

#Get albums given artist uri from search
kendrick_albums = spotify.artist_albums(top_result["items"][0]["uri"],album_type="album")

#print albums by Kendrick Lamar
print(json.dumps(kendrick_albums,indent=4))
                                    
#Get the album To Pimp A Butterfly
TPAB = kendrick_albums.get("items")[10]

#Get list of tracks on the tpab album
tpab_tracks = spotify.album_tracks(TPAB.get("uri"))["items"]
                                    
#Get the features inherent in the sound of the song For Free? - Interlude
For_Free_features = spotify.audio_features(tpab_tracks[1]["uri"])

#Print these features
print(json.dumps(For_Free_features,indent=4))