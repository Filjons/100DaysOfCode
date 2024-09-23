from get_stuff import get_stuff
import spotipy
from spotipy.oauth2 import SpotifyOAuth

credantials = get_stuff("spotify")
CLIENT_ID = credantials["id"]
CLIENT_SECRET = credantials["token"]
REDIRECT_URI = "http://example.com"

#Authenticate user login credantials bla bla.

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read"))

#Test code by fetching some sweet taylor swift stuff.

taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

results = sp.artist_albums(taylor_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
