import webbrowser

class Movie():
	"""
	This class provides a way to store movie related information
	"""
	#All caps because this variable doesn't change
	VALID_STRINGS=["G", "PG", "PG-13", "R"]
	def __init__(self, movie_title, movie_year, movie_director, movie_storyline, poster_image, trailer_youtube):
		"""
		Whenever we create a new instance of the 'Movie' class, this '__init__'
		method is going to be called. While 'self' represents the instance of
		the object itself, the other four arguments are all attributes
		that relate to the object we've created.
		"""
		self.title = movie_title
		self.year = movie_year
		self.director = movie_director
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		"""
		The 'webbrowser' standard library that's available in Python allows
		us to open any web links in the browser. In this case we want to open
		the links to the trailer of a movie, as defined by the '__init__' function.
		"""
		webbrowser.open(self.trailer_youtube_url)