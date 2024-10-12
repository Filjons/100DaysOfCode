from get_stuff import get_stuff
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100"
credantials = get_stuff("spotify")
CLIENT_ID = credantials["id"]
CLIENT_SECRET = credantials["token"]
REDIRECT_URI = "http://example.com"

# Write your code below this line 👇

# get user input
# user_input = input("Which year do you want to travel to? (YYY-MM-DD): ")
user_input = "1988-03-19"

# send request to billboard
responese = requests.get(url=f"{URL}/{user_input}")

# parse the data into a soup using the html.parser

web_page = responese.text
soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())

# extract data (songs)
# CSS selectors to drill down in the tag tree
ranked_list = soup.select(selector="div ul li #title-of-a-story")
# print(ranked_list)

# Save data to file
file_name = f"top_100_songs_{user_input}.txt"
with open(file_name, "w", encoding="utf-8") as file:
    [file.write(f"{song.get_text().strip()}\n") for song in ranked_list]

with open(file_name, "r") as file:
    print(file.read())

# Authenticate user login credantials bla bla.

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read , playlist-modify-public"))

# Test code by fetching some sweet taylor swift stuff.
'''
results = sp.artist_albums(taylor_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
'''
