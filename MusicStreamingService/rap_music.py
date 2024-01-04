from songs import Song
from playlists import Playlist


class Rap(Song):
    def play_song(self):
        duration = self.length
        while duration > 0:
            print(f"Now playing {self.artist}"f's song called {self.title}...')
            duration -= 20

    def add_to_playlist(self, playlist: 'Playlist') -> None:
        playlist.playlist_songs.append(self)
