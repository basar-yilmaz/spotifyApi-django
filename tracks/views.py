import requests
import random
from django.http import JsonResponse
from django.shortcuts import render
from .spotify_api import get_spotify_access_token
import json
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

def index(request):
    return render(request, 'index.html')




def get_random_artist(genre):
    try:
        # open the genres.json file
        with open('genres.json') as f:
            genres_data = json.load(f)

        # get the list of lower artist names for the given genre
        artists_list = genres_data.get(genre.lower(), [])
        if not artists_list:
            return None

        # pick a random artist from the list
        random_artist = random.choice(artists_list)
        return random_artist
    except FileNotFoundError:
        return None


def get_popular_tracks_by_artist(artist_name):
    # retrieve an access token from Spotify
    access_token = get_spotify_access_token()

    # Build the request URL
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'q': f'artist:"{artist_name}"',
              'type': 'track',
              'limit': 50}
    response = requests.get(
        'https://api.spotify.com/v1/search', headers=headers, params=params)

    if response.status_code == 200:
        # at this point we have a valid response
        data = response.json()

        # get the list of tracks from the response
        # if no tracks are found, return an empty list
        tracks = data.get('tracks', {}).get('items', [])

        # Sort in descending order
        # popularity is a number between 0 and 100
        # the higher the number, the more popular the track
        sorted_tracks = sorted(tracks,
                               key=lambda x: x.get('popularity', 0),
                               reverse=True)

        # Get the most popular 10 tracks from end of the list
        most_popular_tracks = sorted_tracks[:10]

        formatted_tracks = []
        for track in most_popular_tracks:
            formatted_track = {
                "artist": track['artists'][0]['name'],
                "track": track['name'],
                "popularity": track['popularity'],
                "album_image_url": track['album']['images'][0]['url'],
                "preview_url": track['preview_url'],
            }
            formatted_tracks.append(formatted_track)

        return formatted_tracks
    else:
        error_message = f"Error: {response.status_code} - {response.text}"
        return {'error': error_message}


def tracks_by_genre(request, genre):
    random_artist = get_random_artist(genre)

    if random_artist:
        popular_tracks = get_popular_tracks_by_artist(random_artist)
        return JsonResponse(popular_tracks, safe=False)
    else:
        return JsonResponse({'error': f'Genre "{genre}" not found.'}, status=404)
