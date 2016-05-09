#! /usr/bin/python
# File name: entertainment_center.py
# Author: Fabio
# Date created: 05.05.2016
# Date modified: 10.05.2016

"""
In this file we create various instances of the 'Movie' class, we store all of
these objects in the 'movies' list and then call the 'open_movies_page' function
defined in the 'fresh_tomatoes.py' file. 
"""

import media
import fresh_tomatoes

close_up = media.Movie("Close-Up",
						"1990",
						"Abbas Kiarostami",
						"""This fiction-documentary hybrid uses a sensational
						real life event, the arrest of a young man on charges 
						that he fraudently impersonates a well-known filmmaker.""",
						"http://zardoz.a.ltrbxd.com/resized/sm/upload/os/ty/w9/kk/close-up-0-230-0-345-crop.jpg?k=5c095d09ef",  # noqa 
						"https://www.youtube.com/watch?v=Z_tGkf_jnCk")

victoria = media.Movie("Victoria",
						"2015",
						"Sebastian Schipper",
						"""A young Spanish woman who has newly moved to Berlin
						finds her flirtation with a local guy turn potentially
						deadly as their night out with his friends reveals a 
						dangerous secret.""",
						"http://skyfall.a.ltrbxd.com/resized/sm/upload/p7/5b/rd/8f/t66eAg7xBLGoSSoA8JtJtX3NKs1-0-230-0-345-crop.jpg?k=9e9016b0f6",  # noqa 
						"https://www.youtube.com/watch?v=wPpyx5aIWgQ")

blue = media.Movie("La vie d'Adele",
					"2013",
					"Abdellatif Kechiche",
					"""Adele's life is changed when she meets Emma, a young woman
					with blue hair, who will allow her to discover desire, to 
					assert herself as a woman and as an adult. In front of 
					others, Adele grows, seeks, finds herself.""",
					"http://skyfall.a.ltrbxd.com/resized/film-poster/1/1/4/5/7/6/114576-blue-is-the-warmest-color-0-230-0-345-crop.jpg?k=efefa14e31",  # noqa 
					"https://www.youtube.com/watch?v=Y2OLRrocn3s")

spring_breakers = media.Movie("Spring Breakers",
							    "2012",
								"Harmony Korine",
								"""Brit, Candy, Cotty, and Faith have been best
								friends since grade school. They have to save 
								enough money for spring break to get 
								their shot at having some fun.""",
								"http://primer.a.ltrbxd.com/resized/film-poster/9/6/1/0/9/96109-spring-breakers-0-230-0-345-crop.jpg?k=2524e6a1e7",  # noqa 
								"https://www.youtube.com/watch?v=oaeVPdsVkyA")

fedele_alla_linea = media.Movie("Fedele alla Linea",
								'2013',
								'Germano Maccioni',
								"""Un film dialogo con Giovanni Lindo Ferretti, 
								cantautore e scrittore, anima delle band di 
								culto CCCP Fedeli alla linea, C.S.I. e PGR.""",
								"http://oblivion.a.ltrbxd.com/resized/film-poster/1/4/3/6/0/3/143603-fedele-alla-linea-giovanni-lindo-ferretti-0-230-0-345-crop.jpg?k=736931677a",  # noqa 
								"https://www.youtube.com/watch?v=e09MKHWGmj0")

synechdoche = media.Movie("Synecdoche, New York",
						 '2008',
						 'Charlie Kaufman',
						  """A theater director struggles with his work, and the
						  women in his life, as he attempts to create a life 
						  size replica of New York inside a warehouse as part
						  of his new play.""",
						  "http://oblivion.a.ltrbxd.com/resized/sm/upload/z9/j9/kx/ve/l3r5MgeN0UUySPbf6aWeUyKGdb2-0-230-0-345-crop.jpg?k=a100939294",  # noqa 
						  "https://www.youtube.com/watch?v=XIizh6nYnTU")

taxi = media.Movie("Taxi Driver",
					'1976',
					'Martin Scorsese',
					"""Robert De Niro stars as Travis Bickle in this
					oppressive psychodrama about a Vietnam veteran 
					who rebels against the decadence and immorality
					of big city life in New York while working the 
					nightshift as a taxi driver.""",
					"http://oblivion.a.ltrbxd.com/resized/sm/upload/et/vw/of/37/94GCaf7SzNWdQLhZ63AaGjNXcK3-0-230-0-345-crop.jpg?k=b0d2e03e01",  # noqa 
					"https://www.youtube.com/watch?v=cujiHDeqnHY")

tree_of_life = media.Movie("The Tree of Life",
							'2011',
							'Terrence Malick',
							"""The impressionistic story of a Texas family in the 1950s. 
							The film follows the life journey of the eldest son
							, Jack who finds himself a lost soul in the modern 
							world, seeking answers to the origins and meaning 
							of life.""",
							"http://zardoz.a.ltrbxd.com/resized/film-poster/4/7/4/6/8/47468-the-tree-of-life-0-230-0-345-crop.jpg?k=d5204d763a",  # noqa 
							"https://www.youtube.com/watch?v=RrAz1YLh8nY")

before_sunset = media.Movie("Before Sunset",
							'2004',
							'Richard Linklater',
							"""Nine years ago two strangers met by chance and 
							spent a night in Vienna that ended before sunrise. 
							They are about to meet for the first time since. 
							Now they have one afternoon to find out if they 
							belong together.""",
							"http://skyfall.a.ltrbxd.com/resized/film-poster/5/1/9/7/0/51970-before-sunset-0-230-0-345-crop.jpg?k=78f7cfe2ab",  # noqa 
							"https://www.youtube.com/watch?v=oI3UuneLcyU")

caro_diario = media.Movie("Caro Diario",
							'1993',
							'Nanni Moretti',
							"""Writer, director, actor Nanni Moretti offers a 
							three part film diary which takes a sharply satiric 
							look at Italian life. Dear Diary is a 
							semi-autobiographical film in the style of a 
							documentary.""",
							"http://oblivion.a.ltrbxd.com/resized/film-poster/3/6/0/9/1/36091-dear-diary-0-230-0-345-crop.jpg?k=d0f1f1173d",  # noqa 
							"https://www.youtube.com/watch?v=zIv_vdVXjpo")

non_pensarci = media.Movie("Non Pensarci",
							'2007',
							'Gianni Zanasi',
							"""The film follows Stefano Nardini a post-punk 
							guitarist stuck in a strange career limbo. During
							that time he decides to go back home, to his family.""",
							"http://mr.comingsoon.it/imgdb/locandine/big/1587.jpg",  # noqa 
							"https://www.youtube.com/watch?v=U6RfizWCrYU")

there_will_be_blood = media.Movie("There Will Be Blood",
								'2007',
								'Paul Thomas Anderson',
								"""When Daniel Plainview learns of oil-rich 
								land in California that can be bought cheaply, 
								he moves his operation there and begins 
								manipulating and exploiting the local 
								landowners into selling him their property.""",
								"http://primer.a.ltrbxd.com/resized/sm/upload/xl/fv/04/dn/p1GnnweLwSe82eMp55VEDio2Rcr-0-230-0-345-crop.jpg?k=0e2715133d",  # noqa 
								"https://www.youtube.com/watch?v=OjZ1rUQQKxY")

movies=[before_sunset,
		blue,
		caro_diario, 
		close_up, 
		fedele_alla_linea, 
		non_pensarci,
		spring_breakers, 
		synechdoche, 
		taxi, 
		tree_of_life, 
		there_will_be_blood,
		victoria]

fresh_tomatoes.open_movies_page(movies)