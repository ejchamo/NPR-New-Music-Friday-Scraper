from credentials import my_client_id, my_client_secret
from NPR_scraper import scrape_npr_new_music_fridays
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=my_client_id,
        client_secret=my_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
# print(user_id)

# album_dictionary = scrape_npr_new_music_fridays()


def get_spotify_album_links(album_dictionary):
    """Request album url from the Spotify API.

    Keyword arguments:
    album_dictionary -- albums you want spotify links for, format as album:artist dictionary
    """

    album_links = []

    for album in album_dictionary:
        result = sp.search(f"album:{album} artist:{album_dictionary[album]}", type="album")
        if result["albums"]["items"][0]:
            album_link = result["albums"]["items"][0]["external_urls"]["spotify"]
            # print(album_link)
            album_links.append(album_link)
        else:
            print(f"album: {album} could not be found")

    # print(album_links)
    return album_links


# album_links = get_spotify_album_links()


def get_spotify_album_tracks(album_links):
    """Request song url for given albums from the Spotify API.

    Keyword arguments:
    album_links -- albums you want each spotify song link for, format as list of spotify album urls
    """
    album_info = []

    for album in album_links:
        info = sp.album_tracks(album_id=album)
        tracks = info["items"]
        album_info.append(tracks)

    # print(album_info[0][0]["external_urls"]["spotify"])

    track_links = []

    for album in album_info:
        for track in album:
            url = track["external_urls"]["spotify"]
            track_links.append(url)

    # print(track_links)

    return track_links


# track_links = get_spotify_album_tracks()


def create_spotify_playlist(track_links, playlist_name):
    """Create a new spotify playlist from given tracks

    Keyword arguments:
    track_links -- tracks you want to put into a playlist, format as list of spotify song urls
    playlist_name -- what you want the playlist name to be, format as string
    """
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    # print(playlist)
    print(playlist["external_urls"]["spotify"])
    sp.playlist_add_items(playlist_id=playlist["id"], items=track_links)

