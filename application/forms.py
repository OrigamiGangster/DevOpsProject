from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SongInfo(FlaskForm):
    artist = StringField('Artist')
    title = StringField('Track Title')
    submit = SubmitField('Add Name')