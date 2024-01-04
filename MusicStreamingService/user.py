import typing
from playlists import Playlist
from songs import Song


class User:
    def __init__(self, nickname: str):
        self.nickname = nickname
        self.playlists = []
        self.listening_history = []

    def create_playlist(self, name: str) -> 'Playlist':
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def listen_to_song(self, song_title: str) -> None:
        Song.songs_library[song_title].play_song()
        self.listening_history.append(song_title)
