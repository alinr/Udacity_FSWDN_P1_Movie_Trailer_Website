"""
media.py

File contains the Class Movie which provides information about movies,
collected via myapifilms API (http://www.myapifilms.com/).
"""
__author__ = "Alin Radulescu"
__version__ = "1.0"


class Movie():
    """
    Provides information about movies.
    Call movieinformation via myapifilms API.
    Open a modal and play the YouTube Trailer.
    """

    def __init__(self, movie_id, movie_imdb):
        """
        Constructor for Movie class.
        Parameters:
        :param movie_id: (required) - (string) The movie's IMDb ID
        :param movie_imdb: (required) - (array) The movie's addition information
        """

        self.movie_id = movie_id
        self.movie_imdb = movie_imdb
