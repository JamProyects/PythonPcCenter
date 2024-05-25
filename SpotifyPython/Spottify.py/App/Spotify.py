from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint 
from Client.ClientsSecurity import CLIENT_ID1, CLIENT_SECRET2

client_id = CLIENT_ID1
client_secret = CLIENT_SECRET2



author = 'RadioHead'
song = 'bad guy'.upper()
flag = 0

if len(sys.argv) > 1:
    search_str = sys.argv[1]
else:
    search_str = "RadioHead"


sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
result = sp.search(author)






