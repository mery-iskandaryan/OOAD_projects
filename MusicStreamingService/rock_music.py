from songs import Song
from playlists import Playlist


class Rock(Song):
    def play_song(self):
        duration = self.length
        while duration > 0:
            print(f"Now playing {self.artist}'s song called {self.title}...")
            duration -= 20
        print("The song is over.")

    def add_to_playlist(self, playlist: 'Playlist') -> None:
        playlist.playlist_songs.append(self)
