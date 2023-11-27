"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Playlist {self.name}>'



class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Song {self.title} by {self.artist}>'


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    # Adding relationships to access playlist and song objects
    playlist = db.relationship('Playlist', backref=db.backref('playlist_songs', cascade='all, delete'))
    song = db.relationship('Song', backref=db.backref('playlist_songs', cascade='all,delete'))

    def __repr__(self):
        return f'<PlaylistSong playlist_id={self.playlist_id} song_id={self.song_id}>'




# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
