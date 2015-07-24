#!/usr/bin/python
"""
load_data.py

Python script to load JSON Data from myapifilms-API and
save in movies_data.json.
"""
__author__ = "Alin Radulescu"
__version__ = "1.0"


import urllib
import json
import os


# Movies list, contains IMDb-Movie-ID & YouTube official trailer URL for each movie
movies_list = [
    ["tt0111161", "https://www.youtube.com/watch?v=NmzuHjWmXOc"],
    ["tt0068646", "https://www.youtube.com/watch?v=sY1S34973zA"],
    ["tt0071562", "https://www.youtube.com/watch?v=qJr92K_hKl0"],
    ["tt0468569", "https://www.youtube.com/watch?v=EXeTwQWrcwY"],
    ["tt0110912", "https://www.youtube.com/watch?v=tGpTpVyI_OQ"],
    ["tt0050083", "https://www.youtube.com/watch?v=fSG38tk6TpI"],
    ["tt0060196", "https://www.youtube.com/watch?v=WCN5JJY_wiA"],
    ["tt0167260", "https://www.youtube.com/watch?v=r5X-hFf6Bwo"],
    ["tt0137523", "https://www.youtube.com/watch?v=SUXWAEX2jlg"],
    ["tt0120737", "https://www.youtube.com/watch?v=V75dMMIW2B4"],
    ["tt0080684", "https://www.youtube.com/watch?v=JNwNXF9Y6kY"],
    ["tt0109830", "https://www.youtube.com/watch?v=eYSnxZKTZzU"],
    ["tt1375666", "https://www.youtube.com/watch?v=YoHD9XEInc0"],
    ["tt0073486", "https://www.youtube.com/watch?v=OXrcDonY-B8"],
    ["tt0167261", "https://www.youtube.com/watch?v=LbfMDwc4azU"],
    ["tt0099685", "https://www.youtube.com/watch?v=h3QpxNI-PtE"],
    ["tt0133093", "https://www.youtube.com/watch?v=vKQi3bBA1y8"],
    ["tt0076759", "https://www.youtube.com/watch?v=oypug4vFD1E"],
    ["tt0047478", "https://www.youtube.com/watch?v=rwIHcNyC_Rw"],
    ["tt0317248", "https://www.youtube.com/watch?v=ldVlSKByUtg"],
    ["tt0114369", "https://www.youtube.com/watch?v=znmZoVkCjpI"],
    ["tt0102926", "https://www.youtube.com/watch?v=RuX2MQeb8UM"],
    ["tt0114814", "https://www.youtube.com/watch?v=Q0eCiCinc4E"],
    ["tt0038650", "https://www.youtube.com/watch?v=KZ_OZpb0wIA"],
    ["tt0118799", "https://www.youtube.com/watch?v=16RZHqCIy9M"]
]


def call_api(movie_id):
    """
    :param movie_id: IMDb Movie ID
    :return: array with myapifilms-API Movie values
    """
    # Call additional movieinformation from the myapifilms API
    imdb_information = urllib.urlopen(
        "http://www.myapifilms.com/imdb?idIMDB=" + movie_id +
        "&format=JSON&aka=0&business=0&seasons=0&seasonYear=1&technical=1&"
        "lang=en-us&actors=S&biography=0&trailer=0&uniqueName=0&filmography=0&"
        "bornDied=0&starSign=0&actorActress=1&actorTrivia=0&movieTrivia=0&"
        "awards=0&moviePhotos=N&movieVideos=N&similarMovies=0")
    # Load API Response and transform to JSON
    data_imdb = json.loads(imdb_information.read().decode('utf-8'))

    # Return IMDb data of the movie
    return data_imdb


# Create or overwrite the output file
file = open('movies_data.json', 'w')
# Begin writing JSON Array
file.write("[")
for movie in movies_list:
    # Call function to receive JSON Data from the API
    data = call_api(movie[0])
    # Add movie youtube trailer information to JSON
    data['movie_youtube_trailer_url'] = movie[1]
    # Write JSON to data file
    json.dump(data, file)
    # Add separator
    file.write(",")
# Remove the last , to obtain a correct JSON file
file.seek(-1, os.SEEK_END)
file.truncate()
file.write("]")
