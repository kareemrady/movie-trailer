class Movie():
    '''
    Movie class that represents a movie with a title
    , story line, poster image url and youtube trailer url
    '''
    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
