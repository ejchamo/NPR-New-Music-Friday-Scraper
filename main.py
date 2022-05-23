import NPR_scraper
import spotify_requests

album_dictionary = NPR_scraper.scrape_npr_new_music_fridays()

album_links = spotify_requests.get_spotify_album_links(album_dictionary)

track_links = spotify_requests.get_spotify_album_tracks(album_links)

spotify_requests.create_spotify_playlist(track_links, "New Music Fridays 5/20")