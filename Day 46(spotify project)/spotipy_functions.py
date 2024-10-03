
import pprint
import spotipy
from get_stuff import get_stuff
import argparse
import logging
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

credantials = get_stuff("spotify")
CLIENT_ID = credantials["id"]
CLIENT_SECRET = credantials["token"]
REDIRECT_URI = "http://example.com"
BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
logger = logging.getLogger('examples.add_tracks_to_playlist')
logging.basicConfig(level='DEBUG')


def create_playlist(playlist='', description=''):

    sp = authenticate(scope="playlist-modify-public")

    user_id = sp.me()['id']
    sp.user_playlist_create(user_id, playlist,
                            description=description)
    print("Created a playlist.")


def get_playslist_uri(playlist_name=""):

    scope = 'playlist-read-private'
    sp = authenticate(scope=scope)
    user_id = sp.me()['id']
    playlists = sp.user_playlists(user=user_id)
    # pprint.pprint(playlists)
    temp = playlists['items']
    for list in temp:
        if list['name'] == playlist_name:
            return list['uri']
    print("Playlist Uri Success!")


def get_song_uri(title="", year=""):

    search_str = f"track:{title} year:{year}"

    sp = authenticate(scope="playlist-modify-public")
    result = sp.search(q=search_str, limit=1, )

    song_uri = result['tracks']['items'][0]['uri']
    print("Song Uri Success!")
    return song_uri


def add_song_to_playlist(playlist='', song=[]):

    sp = authenticate(scope="playlist-modify-private")

    sp.playlist_add_items(playlist_id=playlist, items=song)
    print("Added song, Success!")


def get_songs_from_year(year=""):

    # send request to billboard
    responese = requests.get(url=f"{BILLBOARD_URL}/{year}")

    # parse the data into a soup using the html.parser

    web_page = responese.text
    soup = BeautifulSoup(web_page, "html.parser")
    # print(soup.prettify())

    # extract data (songs)
    # CSS selectors to drill down in the tag tree
    ranked_list = soup.select(selector="div ul li #title-of-a-story")
    # print(ranked_list)
    song_list = []
    # Save data to file

    [song_list.append(f"{song.get_text().strip()}") for song in ranked_list]

    # print(song_list)
    print("Song search Success!")
    return song_list


def authenticate(scope=''):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope=scope))
    print("Authentication Success!")
    return sp


    


def main():

    search_year = "1988-03-19"
    playlist = "test_playlist"
    # playlist_id = create_playlist(playlist=playlist)

    playlist_uri = get_playslist_uri(playlist_name=playlist)

    # songs = get_songs_from_year(year=)

    song_uri = get_song_uri(title="Thunderstruck", year=search_year[0:4])
    add_song_to_playlist(playlist=playlist_uri,
                         song=[song_uri])

    '''uris = ['spotify:track:2RlgNHKcydI9sayD2Df2xp']
    uri = 'spotify:playlist:68blxQX6RAnBXmYMaOm34O'
    add_song_to_playlist(playlist=uri, track=uris)'''

    #
    # result = sp.search(q='Ritual', limit=5, type='track', market='SE')

    # pprint.pprint(result)


if __name__ == '__main__':
    main()
