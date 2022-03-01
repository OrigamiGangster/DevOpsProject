from application import db


class SongInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String)
    title = db.Column(db.String)

