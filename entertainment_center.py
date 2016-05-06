import media
import fresh_tomatoes

close_up = media.Movie("Close-Up (1990) Directed by Abbas Kiarostami",
						"This fiction-documentary hybrid uses a sensational real life event, the arrest of a young man on charges that he fraudently impersonated the well-known filmmaker Mohsen Makhmalbaf, as the basis for a stunning, multilayered investigation into movies, identity, artistic creation, and existence, in which the real people from the case play themselves.",
						"http://zardoz.a.ltrbxd.com/resized/sm/upload/os/ty/w9/kk/close-up-0-230-0-345-crop.jpg?k=5c095d09ef",
						"https://www.youtube.com/watch?v=Z_tGkf_jnCk")

victoria = media.Movie("Victoria (2015) Directed by Sebastian Schipper",
						"A young Spanish woman who has newly moved to Berlin finds her flirtation with a local guy turn potentially deadly as their night out with his friends reveals a dangerous secret.",
						"http://skyfall.a.ltrbxd.com/resized/sm/upload/p7/5b/rd/8f/t66eAg7xBLGoSSoA8JtJtX3NKs1-0-230-0-345-crop.jpg?k=9e9016b0f6",
						"https://www.youtube.com/watch?v=wPpyx5aIWgQ")

blue = media.Movie("La vie d'Adele (2013) Directed by Abdellatif Kechiche",
					"Adele's life is changed when she meets Emma, a young woman with blue hair, who will allow her to discover desire, to assert herself as a woman and as an adult. In front of others, Adele grows, seeks herself, loses herself, finds herself.",
					"http://skyfall.a.ltrbxd.com/resized/film-poster/1/1/4/5/7/6/114576-blue-is-the-warmest-color-0-230-0-345-crop.jpg?k=efefa14e31",
					"https://www.youtube.com/watch?v=Y2OLRrocn3s")

spring_breakers = media.Movie("Spring Breakers (2012) Directed by Harmony Korine",
								"Brit, Candy, Cotty, and Faith have been best friends since grade school. They live together in a boring college dorm and are hungry for adventure. All they have to do is save enough money for spring break to get their shot at having some real fun. A serendipitous encounter with rapper Alien promises to provide the girls with all the thrill and excitement they could hope for. With the encouragement of their new friend, it soon becomes unclear how far the girls are willing to go to experience a spring break they will never forget.",
								"http://primer.a.ltrbxd.com/resized/film-poster/9/6/1/0/9/96109-spring-breakers-0-230-0-345-crop.jpg?k=2524e6a1e7",
								"https://www.youtube.com/watch?v=oaeVPdsVkyA")



movies=[blue, close_up, spring_breakers, victoria]
fresh_tomatoes.open_movies_page(movies)