import sys

from src.movie_api import MovieAPI
from src.pricer import Pricer
from src.rental import Rental


class MovieStub(object):
    def fetch_movie(self, imdbId):
        return {"Title": "Blade Runner", "imdbRating": 7.1}


def main():
    customer = sys.argv[1]
    imdbID = sys.argv[2]

    rental = Rental(customer, imdbID, Pricer(MovieStub()))

    print(rental)


if __name__ == "__main__": main()


    #
    # Example movies:
    #
    # tt0096754 - high rated
    # tt0060666 - low rated
    # tt0317303 - medium rated