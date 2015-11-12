
import webbrowser

class Movie():

	#contructor for creating Movie instance
	def __init__(self, movie_title,movie_released_year, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.released_year = movie_released_year
		self.story_line = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube


