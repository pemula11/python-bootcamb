import pprint, os
from bs4 import BeautifulSoup
import lxml, requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, dotenv_values

load_dotenv()
auth_manager = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    show_dialog=True,
    cache_path="token.txt",
    username="Andri Aditya"
)

sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]

URL = 'https://www.billboard.com/charts/hot-100/'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

playlist_title = []
playlist_singer = []
playlist_uri = []

date_input = input("Masukan tanggal (format: YYYY-MM-DD): ")
res = requests.get(url=URL+date_input, headers=header)

year = date_input[:4]
web_page = BeautifulSoup(res.text, 'html.parser')
data_playlist = web_page.find_all(name="div", class_="o-chart-results-list-row-container")


for song in data_playlist:
    selected = song.find(id="title-of-a-story")
    title = (selected.getText().strip())
    playlist_title.append(title)
    try:
        item = sp.search(q=f"track:{title} year={year}", type="track")
        playlist_uri.append(item['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"Musik dengan judul {title} tidak ditemukan")

print(playlist_uri)

user_id = sp.current_user()["id"]
playlist_id = sp.user_playlist_create(user_id, f"{date_input} Billboard", public=False)

print(f"Playlist dibuat: {playlist_id}")

sp.playlist_add_items(playlist_id["id"], playlist_uri)
