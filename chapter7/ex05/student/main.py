# Write your MoviePlayer class here

class MoviePlayer():
    def __init__(self, movies):
        self.movies = movies

    def list_movies(self, movies):
        self.movies = movies
        return movies

    def current_movie(self, movies):
        self.movies = movies
        return movies

    def firmware_version(self, movies):
        self.movies = movies
        return movies

    def update_firmware(self, version):
        self.version = version
        return version

    def play(self, movies):
        self.movies = movies
        return movies


# The code below is used to test your class
if __name__ == '__main__':
    player = MoviePlayer("Harry")
    print("Movies currently on device:", player.list_movies("Dirty"))

    player.update_firmware(2.0)
    print("Updated player firmware version to", player.firmware_version ("3.0"))

    player.play("Dirty Harry")
    #print("Currently playing", f"'{player.current_movie}'")
    cm = player.current_movie("Frozen")
    print("Currently playing", cm)