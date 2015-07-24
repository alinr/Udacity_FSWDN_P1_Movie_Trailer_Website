import webbrowser
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


# Styles and HTML Header for the page
main_page_head = '''
<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Fresh Tomatoes Movie Trailers</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,100,300,700' rel='stylesheet' type='text/css'>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            font-family: 'Roboto', sans-serif;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin: 10px;
            padding: 10px;
            border-radius:3px;
            border:1px solid #eee;
            position:relative;
        }
        .movie-tile:hover {
            background-color: #EEE;
        }
        .movie-tile h2 {
            font-size:2.5rem;
            font-weight:700;
            padding:2rem 0;
            border-bottom:1px solid #ddd;
            margin:0 0 2rem;
        }
        .storyline {
            font-size:1.8rem;
            color:#777;
            padding-bottom:2rem;
            border-bottom:1px solid #ddd;
            margin:0 0 2rem;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;

        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .subheader {
            color:#fff;
            font-weight:200;
        }

        .play-trailer {
            position:absolute;
            top:30px;
            right:30px;
        }
        .navbar-brand {
            display:block;
            margin:0 0 10px;
            font-size:3rem;
            font-weight:300;
        }

        @media (min-width:768px){.masonry-item{width:335px}
        @media (min-width:992px){.masonry-item{width:285px}}
        @media (min-width:1200px){.masonry-item{width:345px}}
        .masonry-item img{width:100%;height:auto}
    </style>
</head>
<body>
'''

# The main page layout and title bar
main_page_content = '''
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
        <div class="modal-dialog">
            <div class="modal-content">
                <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                </a>
                <div class="scale-media" id="trailer-video-container"></div>
            </div>
        </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
        <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
                    <p class="subheader">A list of the best rated movies at IMDb.</p>
                </div>
            </div>
        </div>
    </div>
    <div class="container" id="masonry">
        {movie_tiles}
    </div>

'''

# Scripting and Footer for the page
main_page_footer = '''
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/masonry/3.3.1/masonry.pkgd.min.js"></script>

    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.play-trailer', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
            $('.movie-tile').hide().first().show("fast", function showNext() {
                $(this).next("div").show("fast", showNext);
            });
        });

        var $container = $('#masonry');
        $container.masonry();

        //Reinitialize masonry inside each panel after the accordion link is clicked -
        $('div[data-test=col]').each(function () {
            var $this = $(this);

            $this.on('shown.bs.collapse', function () {
                $container.masonry();
            });
            $this.on('hidden.bs.collapse', function () {
                $container.masonry();
            });
        });

    </script>
</body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile masonry-item">
    <img src="{movie_poster_image_url}" >
    <h2>{movie_title}</h2>
    <p class="storyline">{movie_storyline}</p>
    <p>Directors: {movie_directors}</p>
    <p>First aired: {movie_year}, Runtime: {movie_runtime}
    <br />Age Rating: {movie_age_rating}<br />IMDb Rating: {movie_imdb_rating}<br /></p>
    <div class="panel-group" id="accordion_{movie_id}" role="tablist" aria-multiselectable="true">
        <div class="panel panel-default">
            <div class="panel-heading" role="tab" id="headingOne">
                <h4 class="panel-title">
                <a role="button" data-toggle="collapse" data-parent="#accordion_{movie_id}"
                href="#collapseOne_{movie_id}" aria-expanded="true"
                aria-controls="collapseOne_{movie_id}">Actors</a>
                </h4>
            </div>
            <div id="collapseOne_{movie_id}" class="panel-collapse collapse"
            role="tabpanel" aria-labelledby="headingOne" data-test="col">
                <div class="panel-body">
                {movie_actors}
                </div>
            </div>
        </div>
    </div>
    <a class="btn btn-success play-trailer" data-trailer-youtube-id="{movie_trailer_youtube_id}"
    data-toggle="modal" data-target="#trailer">Play trailer</a>
</div>
'''

def create_movie_tiles_content(movies):
    """
    Create the HTML container for each movie and fill the variables with values
    :param movies: array with movie values
    :return: HTML container with movie values
    """
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.movie_imdb["movie_youtube_trailer_url"])
        youtube_id_match = youtube_id_match or \
                           re.search(r'(?<=be/)[^&#]+', movie.movie_imdb["movie_youtube_trailer_url"])
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Create the actor's list
        actors = ''
        for actor in movie.movie_imdb['actors']:
            actors += '<li><a href="' + actor['urlProfile'] + '" target="_blank">' \
                      + actor['actorName'] + '</a> as <strong>' \
                      + actor['character'] + '</strong></li>'

        # Create the director's list
        directors = ''
        for director in movie.movie_imdb['directors']:
            directors += director['name'] + ' '

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_id=movie.movie_id,
            movie_title=movie.movie_imdb["title"],
            movie_storyline=movie.movie_imdb["plot"],
            movie_poster_image_url=movie.movie_imdb["urlPoster"],
            movie_runtime=movie.movie_imdb["runtime"][0],
            movie_actors=actors,
            movie_directors=directors,
            movie_year=movie.movie_imdb["year"],
            movie_release_date=movie.movie_imdb["releaseDate"],
            movie_age_rating=movie.movie_imdb["rated"],
            movie_imdb_rating=movie.movie_imdb["rating"],
            movie_trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    """
    Create the HTML file, open the browser and show the file
    :param movies: array with movie values
    """
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content + main_page_footer)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
