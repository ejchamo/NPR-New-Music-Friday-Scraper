**General Information**
  
  NPR-New-Music-Friday-Scraper
  Latest NPR New Music Friday article to Spotify playlist
  
**Data and file overview**

  NPR_scraper.py:  
   Method for finding the latest NPR New Music Friday article and creating an album:artist dictionary from the featured albums
  
  spotify_requests.py:
    Methods for creating a  list of album urls, creating a list of album track urls, and creating a new playlist with the Spotipy package
  
  main.py:
   runing the methods from NPR_scraper.py and spotify_requests.py

**Methodological information**

  spotify_requests.py methods use the Spotipy package and require establishing an access token with your own Spotify developer credentials
    https://spotipy.readthedocs.io/en/2.19.0/#authorization-code-flow
  
  spotify_requests.py methods are not exculsive to the NPR scraper and may be used for any given spotify album urls to create a spotify playlist
