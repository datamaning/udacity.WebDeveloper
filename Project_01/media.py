import webbrowser
class Movie():
    """Movie in the entertainment center.

    Attributes:
        title:Movie Title
        poster_image_url:URL TO movie poster image
        trailer_youtube_url:Url to trailer on Youtube
        director:Movie director name
    """
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    def Show_trailer():
        webbrower.open(trailer_youtube_url)

