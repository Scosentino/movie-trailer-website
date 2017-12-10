import webbrowser

class Movie():
    """This is the Movie class, it creates instances of a movie"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
         This function will open a brower to a movies trailer url
        """
        webbrowser.open(self.trailer_youtube_url)
