import requests, settings
from flask import current_app as app
from urllib.parse import quote

class SpotifyAPI:
    access_token = ''
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET

    scopes = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private user-follow-modify user-follow-read user-library-read user-library-modify user-read-private user-read-birthdate user-read-email user-top-read'
    login_base_url = 'https://accounts.spotify.com/authorize'
    redirect_uri = settings.REDIRECT_URI

    def get_login_url(self):
        redirect_uri = quote(self.redirect_uri, safe=[])
        scope_url = quote(self.scopes, safe=[])
        return "%s?client_id=%s&redirect_uri=%s&scope=%s&response_type=code" % (
            self.login_base_url,
            self.client_id,
            redirect_uri,
            scope_url
        )

    def get_access_token(self, authorization_code):
        token_endpoint = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        response  = requests.post(token_endpoint, data=data)
        self.access_token = response.json()['access_token']

    def get_user_object(self):
        base_url = 'https://api.spotify.com/v1/me'
        response  = requests.get(base_url, headers={'Authorization': 'Bearer %s' % self.access_token})
        return response.json()

def test_api():
    print(app.access_token)
