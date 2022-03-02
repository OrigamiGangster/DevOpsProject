from flask import render_template, request
from application import app, db
from application.models import SongInfo
from application.forms import SongInfo

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/add_song', methods=['GET', 'POST'])
def song():
    message = ""
    form = SongInfo()

    if request.method == 'POST':
        artist = form.artist.data
        title = form.title.data

        if len(artist) == 0 or len(title) == 0:
            message = "Please supply both artist and title"
        else:
            message = f'Wow, {title} by {artist} is a Banger'

    return render_template('add_song.html', form=form, message=message)
