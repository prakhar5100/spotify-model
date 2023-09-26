from flask import Flask, request, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

df = pd.read_csv('Song_data.csv')


client_id = 'b4d2eb5a18c94d5c9a433c484d412540'
client_secret = '84cac7ebeb2b4a62a912026341ecc05f'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    song_name = request.args.get('song_name')
    artist_name = request.args.get('artist_name')
    
    results = sp.search(q=f"track:{song_name} artist:{artist_name}", type='track')
    song_data = results['tracks']['items'][0]
    song_id = song_data['id']
    audio_features = sp.audio_features([song_id])[0]
    energy = audio_features['energy']

    recommended_songs = []
    energy_threshold = 0.1

    for index, row in df.iterrows():
        song_energy = row['Energy']
        if abs(song_energy - energy) <= energy_threshold:
            recommended_songs.append({
                'Song Name': row['Song Name'],
                'Artist': row['Artist'],
                'Energy': row['Energy']
            })

    return render_template("results.html", recommended_songs=recommended_songs)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
