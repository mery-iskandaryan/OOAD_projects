class Playlist:
    def __init__(self, name):
        self.name = name
        self.playlist_songs = []

    def view_songs(self):
        for song in self.playlist_songs:
            print(f'{song.title} - {song.artist}')

    def remove_song(self, song_title):
        for song in self.playlist_songs:
            if song.title == song_title:
                self.playlist_songs.remove(song)
                return
        raise ValueError("The song is not present in the list...")

    def play_playlist(self):
        for song in self.playlist_songs:
            song.play_song()
