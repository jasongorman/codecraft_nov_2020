import unittest
from unittest.mock import MagicMock

from library import Library


class LibraryTest(unittest.TestCase):
    def test_donated_movie_added_to_catalogue(self):
        library = Library(ImdbStub("Blade Runner"), Email())
        library.donate("tt12345")
        movie = library.get_movie("tt12345")
        self.assertEqual(movie.title, "Blade Runner")

    def test_members_emailed_about_new_movie(self):
        mockEmail = Email()
        mockEmail.send = MagicMock()
        library = Library(ImdbStub("Blade Runner"), mockEmail)
        library.donate("tt12345")
        mockEmail.send.assert_called_with("New Movie", "Blade Runner", "All Members")


class ImdbStub(object):
    def __init__(self, title):
        self.title = title

    def fetch(self, imdbId):
        return {
            "title": self.title
        }


class Email(object):
    def send(self, subject, movie_title, distribution_list):
        pass


if __name__ == '__main__':
    unittest.main()
