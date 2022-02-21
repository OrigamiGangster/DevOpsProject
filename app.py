from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class SongInfo(FlaskForm):
    artist = StringField('Artist')
    title = StringField('Track Title')
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])

@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = SongInfo()

    if request.method == 'POST':
        artist = form.artist.data
        title = form.title.data

        if len(artist) == 0 or len(title) == 0:
            message = "Please supply both artist and title"
        else:
            message = f'Wow, {title} by {artist} is a Banger'

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=False, host='0.0.0.0')
 