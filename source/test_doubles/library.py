from movie import Movie


class Library(object):
    def __init__(self, imdb, email):
        self.email = email
        self.imdb = imdb
        self._catalogue = []

    def donate(self, imdbId):
        imdb_info = self.imdb.fetch(imdbId)
        movie = Movie(imdbId, imdb_info["title"])
        self._catalogue.append(movie)
        self.email.send("New Movie", movie.title, "All Members")


    def get_movie(self, imdbId):
        return next(filter(lambda movie: movie.imdbId == imdbId, self._catalogue))