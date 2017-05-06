from flask import Flask, redirect, render_template, request
import api


app = Flask(__name__, static_url_path='/static')
spotify_api = api.SpotifyAPI()

@app.route('/')
def hello_world():
    if spotify_api.access_token:
        print(spotify_api.get_user_object())
        return 'All set up!'

    return render_template(
        'welcome.html',
        login_url=spotify_api.get_login_url()
    )

@app.route('/login')
def login_callback():
    code = request.args.get('code')
    spotify_api.get_access_token(code)
    return redirect("/", code=302)
