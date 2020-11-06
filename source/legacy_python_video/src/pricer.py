from src.video import Video


class Pricer(object):

    def __init__(self, movie_api):
        self.api = movie_api

    def price(self, imdbID):

        json = self.api.fetch_movie(imdbID)

        title = json["Title"]
        rating = float(json["imdbRating"])

        price = 3.95

        if rating > 7:
            price += 1.0

        if rating < 4:
            price -= 1.0

        return Video(imdbID, title, rating, price)
