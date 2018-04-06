import webbrowser


class Movie():
    # class Movie is made so further objects of Movie can be created
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # these four are attributes of a movie,
        # and self is needed to define the init
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        # show_trailer is defined to create a popup window with video
        webbrowser.open(self.trailer_youtube_url)
