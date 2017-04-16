import media
import fresh_tomatoes
       
avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a "
                     "unique mission becomes torn between following his orders "
                     "and protecting the world he feels is his home.",
                     "http://moviecultists.com/wp-content/uploads/2009/"
                     "11/avatar-poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

donnie_darko = media.Movie("Donnie Darko",
                           "A troubled teenager is plagued by visions of a "
                           "large bunny rabbit that manipulates him to commit "
                           "a series of crimes, after narrowly escaping a "
                           "bizarre accident.",
                           "https://images-na.ssl-images-amazon.com/images/I"
                           "/41z6GKy%2BGLL.jpg",
                           "https://www.youtube.com/watch?v=ZZyBaFYFySk")

pelisky = media.Movie("Pelisky",
                      "Two families, Sebkovi and Krausovi, are celebrating "
                      "christmas, but not everyone is in a good mood. Teenage "
                      "kids think their fathers are totaly stupid, fathers "
                      "are sure their children are nothing more than rebels, "
                      "hating anything they say.",
                      "http://www.najbrt.cz/files/fitwidth/1200/auto/"
                      "peliskyplakat.jpg",
                      "https://www.youtube.com/watch?v=CwQOncE8O6k")

ruby_quentin = media.Movie("Ruby & Quentin",
                           "After hiding his loot and getting thrown in jail, Ruby, "
                           "a brooding outlaw encounters Quentin, a dim-witted and "
                           "garrulous giant who befriends him.",
                           "http://cinehero.ucoz.com/_pu/0/13418011.jpg",
                           "https://www.youtube.com/watch?v=QUsLNKkc460")

back_to_the_future = media.Movie("Back to the Future",
                                 "Marty McFly, a 17-year-old high school "
                                 "student, is accidentally sent 30 years into "
                                 "the past in a time-traveling DeLorean "
                                 "invented by his close friend, the maverick "
                                 "scientist Doc Brown.",
                                 "https://images-na.ssl-images-amazon.com/"
                                 "images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1Mjg"
                                 "tOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@"
                                 "._V1_SY1000_CR0,0,643,1000_AL_.jpg",
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")

movies = [avatar, donnie_darko, pelisky, ruby_quentin, back_to_the_future]
fresh_tomatoes.open_movies_page(movies)
                      
