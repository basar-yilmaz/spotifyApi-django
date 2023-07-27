import requests

SPOTIFY_CLIENT_ID = 'ec4cf09689134efe8022de792f1af144'
SPOTIFY_CLIENT_SECRET = 'ac0d7c1d456a4ec3a088e1a99090202c'

def get_spotify_access_token():
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': SPOTIFY_CLIENT_ID,
        'client_secret': SPOTIFY_CLIENT_SECRET,
    }
    response = requests.post(auth_url, data=auth_data)
    data = response.json()
    return data.get('access_token')
