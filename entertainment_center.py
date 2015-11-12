import media
import fresh_tomatoes

#create instances of Movie class
fight_club = media.Movie("Fight Club",
						 1999,
					     "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more...",
						 "http://alikamran.com/wp-content/uploads/2012/08/fightclub-poster2.jpeg",
						 "https://www.youtube.com/watch?v=NjkWLP24LkU")

certified_copy = media.Movie("Certified Copy",
							 2010,
			   				 "In Tuscany to promote his latest book, a middle-aged British writer meets a French woman who leads him to the village of Lucignano. While there, a chance question reveals something deeper.",
			   				 "https://upload.wikimedia.org/wikipedia/en/3/31/Copie-conforme-poster.png",
			   				 "https://www.youtube.com/watch?v=nM_8TPLMCOU")

saving_private_ryan = media.Movie("Saving Private Ryan",
								  "1998",
			   					  "Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.",
			   					  "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
			  					  "https://www.youtube.com/watch?v=vwAxi4A2YcY")

the_matrix = media.Movie("The Matrix",
						 1999,
			   			 "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
			   			 "http://t0.gstatic.com/images?q=tbn:ANd9GcQq3pIz-aKgkmYX1dJ-EL-AlHSPcOO7wdqRIJ5gJy9qNinXpmle",
			  			 "https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_dark_knight = media.Movie("The Dark Knight",
							  2008,
							  "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
							  "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v7_aa.jpg",
							  "https://www.youtube.com/watch?v=EXeTwQWrcwY")

jarhead = media.Movie("Jarhead",
					  2005,
					  "Based on former Marine Anthony Swofford about his pre-Desert Storm experiences in Saudi Arabia and about his experiences fighting in Kuwait.",
					  "http://static.rogerebert.com/uploads/movie/movie_poster/jarhead-2005/large_kmbyO0XUHRHcMyxVSZAWDdrpxIu.jpg",
					  "https://www.youtube.com/watch?v=-aBP-c28_1M")

#create a list to store instances of Movie class
movies = [jarhead, the_matrix, saving_private_ryan, fight_club, certified_copy, the_dark_knight]

#pass a list to open_movies_page method 
fresh_tomatoes.open_movies_page(movies)