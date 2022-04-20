'''This file is the main file for the application.'''
from flask import Flask, render_template
from data import get_data

app = Flask(__name__)

@app.route('/')
def hello():
    '''This function is the main function for the application.'''
    info = get_data()
    print(info)

    return render_template(
        'index.html',
        song_name = info[0],
        artist_names = info[1],
        album_image = info[2],
        song_preview = info[3],
        spotify_link = info[4],
        total_artists = len(info[1])
    )

if __name__ == '__main__':
    app.run(
        debug=True,
    )
