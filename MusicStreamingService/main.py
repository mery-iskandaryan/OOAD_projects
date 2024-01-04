from rock_music import Rock
from rap_music import Rap
from playlists import Playlist
from user import User


def main():
    # creating songs
    song1 = Rock('Comfortably Numb', 'Pink Floyd', '3:55')
    song2 = Rock('Bohemian Rhapsody', 'Queen', '4:15')
    song3 = Rap('Mockingbird', 'Eminem', '3:45')

    # creating a user
    user1 = User('someone')

    # listen to a song
    user1.listen_to_song('Mockingbird')
    user1.listen_to_song('Comfortably Numb')

    # looking ar user1's listening history
    print(user1.listening_history)

    # creating a playlist and adding songs to it
    playlist1 = user1.create_playlist('some playlist')
    song1.add_to_playlist(playlist1)
    song2.add_to_playlist(playlist1)
    song3.add_to_playlist(playlist1)

    # listen to playlist
    playlist1.play_playlist()

    # removing a song from playlist
    playlist1.remove_song('Mockingbird')




if __name__ == '__main__':
    main()
