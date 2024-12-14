import spotipy
from spotipy.oauth2 import SpotifyOAuth

auth_manager = SpotifyOAuth(
    client_id="95dfff53926244bab426a174d30e3046",
    client_secret="1564d062949e488e98272797f3df239a",
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    show_dialog=True,
    cache_path="token.txt",
    username="Andri Aditya"
)

sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]

print(user_id)