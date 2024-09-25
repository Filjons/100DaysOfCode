
import pprint
import spotipy
from get_stuff import get_stuff
import argparse
import logging
from spotipy.oauth2 import SpotifyOAuth

credantials = get_stuff("spotify")
CLIENT_ID = credantials["id"]
CLIENT_SECRET = credantials["token"]
REDIRECT_URI = "http://example.com"

logger = logging.getLogger('examples.add_tracks_to_playlist')
logging.basicConfig(level='DEBUG')


def create_playlist(playlist='', description=''):
    
    sp = authenticate(scope="playlist-modify-public")

    user_id = sp.me()['id']
    sp.user_playlist_create(user_id, playlist,
                            description=description)


def add_song_to_playlist(track='', playlist=''):
    
    sp = authenticate(scope="playlist-modify-public")

    sp.playlist_add_items(playlist, track)


def authenticate(scope=''):
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                     client_secret=CLIENT_SECRET,
                                                     redirect_uri=REDIRECT_URI,
                                                     scope=scope))


def main():

    create_playlist(playlist="test_playlist")
    # result = sp.search(q='Ritual', limit=5, type='track', market='SE')

    # pprint.pprint(result)


if __name__ == '__main__':
    main()

'''
taylor_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

results = sp.artist_albums(taylor_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
'''
