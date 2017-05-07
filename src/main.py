import api
from album import Album
from user import User
from flask import Flask, redirect, render_template, request


app = Flask(__name__, static_url_path='/static')
spotify_api = api.SpotifyAPI()

def retrieve_information():
    user = spotify_api.get_user_object()
    app.user = User(user)

    app.user.set_albums(spotify_api.get_user_albums())
    print(app.user.albums)

    for a in app.user.albums:
        print(a.release_date)

@app.route('/')
def hello_world():
    if spotify_api.access_token:
        retrieve_information()

        return "All set up!"

    return render_template(
        'welcome.html',
        login_url=spotify_api.get_login_url()
    )

@app.route('/login')
def login_callback():
    code = request.args.get('code')
    spotify_api.get_access_token(code)
    return redirect("/", code=302)
