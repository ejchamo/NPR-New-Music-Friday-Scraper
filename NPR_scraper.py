import requests
from bs4 import BeautifulSoup


def scrape_npr_new_music_fridays():
    """Create a dictionary of albums:artists from the latest NPR New Music Fridays article."""
    site_request = requests.get("https://www.npr.org/sections/allsongs/")
    npr_site = site_request.text

    npr_site_soup = BeautifulSoup(npr_site, "html.parser")

    articles = npr_site_soup.findAll(name="a")

    latest_friday_article = ""

    for article in articles:
        if "New Music Friday:" in article.text:
            latest_friday_article = article.get("href")
            break

    # print(latest_friday_article)

    latest_friday_request = requests.get(latest_friday_article)
    latest_friday_text = latest_friday_request.text

    latest_friday_soup = BeautifulSoup(latest_friday_text, "html.parser")

    featured_albums = latest_friday_soup.find(name="ol", class_="edTag")
    # print(featured_albums)

    albums = featured_albums.findAll("em")
    # print(albums)

    albums_text = [album.text for album in albums]

    # print(albums_text)

    info = featured_albums.findAll("li")

    artists = []

    for artist in info:
        text = artist.text
        name_only = text.split("—")[0]
        artists.append(name_only)

    # print(artists)

    album_dictionary = {albums_text[i]:artists[i] for i in range(len(albums_text))}

    # print(album_dictionary)

    # for key in album_dictionary:
    #     print(key)
    #     print(album_dictionary[key])

    return album_dictionary


print(scrape_npr_new_music_fridays())
