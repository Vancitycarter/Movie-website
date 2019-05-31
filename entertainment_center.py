# coding=utf-8
import fresh_tomatoes
import media

detective_pikachu = media.Movie("Detective Pikachu",
"Detective Pikachu, a hilariously wise-cracking, adorable super-sleuth who is a puzzlement even to himself. Finding that they are uniquely equipped to communicate with one another, Tim and Pikachu join forces on a thrilling adventure to unravel the tangled mystery.", "https://upload.wikimedia.org/wikipedia/en/e/e5/Pokémon_Detective_Pikachu_teaser_poster.jpg",
"https://www.youtube.com/watch?v=bILE5BEyhdo")




venom = media.Movie("Venom",
"Journalist Eddie Brock body merges with the alien Venom leaving him with superhuman strength and power. ", "https://upload.wikimedia.org/wikipedia/en/1/18/Venom_%282018_film_poster%29.png",
"https://www.youtube.com/watch?v=xLCn88bfW1o")



spider_man = media.Movie("Spider-Man: Far From Home",
"Following the events of Avengers: Endgame, Spider-Man must step up to take on new threats in a world that has changed forever.", "https://upload.wikimedia.org/wikipedia/en/1/1c/Spider-Man_Far_From_Home_poster.jpeg",
"https://www.youtube.com/watch?v=Nt9L1jCKGnE")

movies = [detective_pikachu, venom, spider_man]
fresh_tomatoes.open_movies_page(movies)
