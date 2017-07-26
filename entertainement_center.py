import fresh_tomatoes

from media import Movies

the_girl_next_door = Movies("The girl next door", "A story of a prostitute and a nerd guy.",
                    "https://fanart.tv/detailpreview/fanart/movies/10591/movieposter/the-girl-next-door-5223587545d37.jpg",
                    "https://www.youtube.com/watch?v=nBEmRXeJ-C0")

movies = [the_girl_next_door]

fresh_tomatoes.open_movies_page(movies)
