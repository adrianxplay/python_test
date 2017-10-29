class Band:
    def __str__(self):
        return "{}".format(self.name)

    def __init__(self, name):
        self.name = name
        self.album = None

    def add_album(self, album):
        self.album = Album(album)
        return self

    def add_song(self, song_id, song):
        self.album.add_song(song, song_id)
        return self


class Album:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def set_name(self, name):
        self.name = name

    def add_song(self, song_name, song_id):
        self.songs.append(Song(song_name, song_id))


class Song:
    def __init__(self, name, song_id):
        self.name = name
        self.song_id = song_id
