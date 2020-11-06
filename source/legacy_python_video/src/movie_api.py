import requests


class MovieAPI(object):
    def fetch_movie(self, imdbID):
        response = requests.get("http://www.omdbapi.com/?i=" + imdbID + "&apikey=6487ec62")
        return response.json