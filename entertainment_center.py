#!/usr/bin/python
"""
entertainment_center.py

Simple python script to create an array of instances of the class
media.Movie and call the fresh_tomatoes.py script to create a static
HTML file which will display movies with their information & trailer.
"""
__author__ = "Alin Radulescu"
__version__ = "1.0"


import fresh_tomatoes
import media
import json


# Open JSON-file which contains movie information, received from myapifilms
with open('movies_data.json') as data_file:
    # Read and load IMDb-API Response
    data = json.load(data_file)

    movies_array = []
    for movie in data:
        # Create array with instances of the class movie
        movies_array.append(media.Movie(movie["idIMDB"], movie))

# Call fresh_tomatoes.py to create static HTML file which will display the movies
fresh_tomatoes.open_movies_page(movies_array)


