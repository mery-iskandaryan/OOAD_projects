import datetime


class Album:
    def __init__(self, title: str, artist: str, release_date: datetime.date, *songs):
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.songs = [song for song in songs]

