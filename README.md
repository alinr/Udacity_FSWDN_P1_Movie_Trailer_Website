# Movie Trailer Website

The Movie Trailer Website Project is the first project at the [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
It is a server-side python code to store a list of movies, including box art imagery, a movie trailer URL and further information about the movies, received via [myapifilms API](http://www.myapifilms.com).
This data will be served as a web page allowing visitors to watch the trailers of the movies.
Additional information from myapifilms.com are saved as json file in movies_data.json. Use Python v2.7.

## Table of contents

- [How to run](#how-to-run)
- [What is included](#what-is-included)
- [Creator](#creator)
- [Copyright and license](#copyright-and-license)

## How to run

The app can be executed by several ways, the most direct one is by typing "python entertainment_center.py" on system's command line. 
If you want to extend or change the movies displayed by the app, you can do this by adding new items to the array "movies_list" in file load_data.py. After that, execute "python load_data.py" on system's command line. A new movies_data.json file will be generated. Then execute again "python entertainment_center.py" on system's command line, to update the content at fresh_tomatoes.html.

## What is included

Within the download you'll find the following directories and files.
You'll see something like this:

```
Udacity_FSWDN_P1_Movie_Trailer_Website/
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── load_data.py
├── media.py
├── movies_data.json
└── README.md
```

## Creator

**Alin Radulescu**

- <http://alinr.com/>


## Copyright and license

Code and documentation copyright 2015 Alin Radulescu. Code released under the MIT license. Docs released under Creative Commons.