import abc


class Song(abc.ABC):
    songs_library = {}

    def __init__(self, title: str, artist: str, length: str):
        self.title = title
        self.artist = artist
        self.length = int(length.split(':')[0]) * 60 + int(length.split(':')[1])
        Song.songs_library[self.title] = self

    @abc.abstractmethod
    def play_song(self):
        ...

    @abc.abstractmethod
    def add_to_playlist(self, playlist: 'Playlist') -> None:
        ...
