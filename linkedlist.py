# This code represents a Music Player which is a singly linked list. It means that there is only one direction to travel through the playlist. 
# In the music player user can add new songs to playlist, play first and always next song and list all the songs in the playlist. 


class Song:
    def __init__(self, title):
        self.title = title  # Title of the song
        self.song_pointer = None  # Pointer to the next song in the playlist

class MusicPlayer:
    def __init__(self):
        self.first_song = None  # First song in the playlist
        self.currently_playing = None  # The song currently being played


    def add_song(self, title):
        """Add a song aka node to the end of the playlist"""
        new_song = Song(title) #create a new node

        if self.first_song is None:
            self.first_song = new_song #if there is no songs yet, the this will be the first one

        else: #if there is songs in the playlist, travel through the end of the list and add the song there
            current_song = self.first_song #start traveling from the first song in the playlist

            while current_song.song_pointer: #loop that continues as long as there is a song with a pointer to a next song 
                current_song = current_song.song_pointer #with the pointers travel to the end of the list, until reach a song which has no pointer to a next song
            current_song.song_pointer = new_song #make the pointer point to the added song 


    def play_first_song(self):
        """Start playing the first song"""
        if self.first_song: #check that there is a song in the playlist
            self.currently_playing = self.first_song #set the first song to be currently played
            print(f"Now playing: '{self.currently_playing.title}'")
        else:
            print("No songs in the playlist.")


    def play_next_song(self):
        """Play the next song"""
        if self.currently_playing and self.currently_playing.song_pointer: #check that there is a node(song) we are currently in and it has pointer to the next song 
            self.currently_playing = self.currently_playing.song_pointer #set the currently playing value to be the one that the pointer is pointing to
            print(f"Now playing: '{self.currently_playing.title}'") #play the song (it is now the next song)

        elif self.currently_playing: #condition to check that we are in current song but it does not fill the pointer requirements to next song.
            print("End of playlist reached.")

        else: #we are not in any song right now, which means that the travelling through playlist hasnt started
            print("No song is currently playing. Use 'play_first_song' to start.")


    def display_playlist(self):
        """Display all songs in the playlist"""
        current_song = self.first_song #set the current song to be the first one in the playlist
        if not current_song: #if there is no current song it means there is no songs in the playlist.
            print("Playlist is empty.")
            return
        print("Playlist:")
        while current_song: #if there is songs in the playlist it starts from the first one and travels through the whole playlist 
            print(f"- {current_song.title}")
            current_song = current_song.song_pointer  #use pointers to set new value to current song as we travel through the playlist



# Example usage
iPod = MusicPlayer()
iPod.display_playlist() #there is no song yet so prints 'playlist is empty'

iPod.add_song("Hips Don't Lie")
iPod.add_song("Highway to Hell")
iPod.add_song("Macarena")

iPod.display_playlist()  # Displays the entire playlist

iPod.play_first_song()  # Now playing: 'Hips Don't Lie'
iPod.play_next_song()    # Now playing: 'Highway to Hell'
iPod.play_next_song()    # Now playing: 'Macarena'
iPod.play_next_song()    # End of playlist reached.