import fresh_tomatoes
import media

# objects of Class Movie 
# Sombra : Title, short description, poster image, and youtube link
sombra_short = media.Movie("Sombra - Infiltration",
                           "Sombra is introduced to the Overwatch Universe",
                           "sombra_art.jpg",
                           "https://www.youtube.com/watch?v=tU7jskA1zWI")
# Doomfist : Title, short description, poster image, and youtube link
doomfist_short = media.Movie("Doomfist - Animated Short",
                             "Doomfist destroys the heroes of Overwatch",
                             "doomfist_art.jpg",
                             "https://www.youtube.com/watch?v=vaZfZFNuOpI")
# Moira : Title, short description, poster image, and youtube link
moira_short = media.Movie("Moira - Origin Story",
                          "Moira talks about why she joined Blackwatch",
                          "moira_art.png",
                          "https://www.youtube.com/watch?v=6ETybQd4uRE")
# Mei : Title, short description, poster image, and youtube link
mei_short = media.Movie("Mei - Rise and Shine",
                        "Mei's path from scientist to Overwatch member",
                        "mei_art.jpg",
                        "https://www.youtube.com/watch?v=8tjcm_kI0n0")
# Winston : Title, short description, poster image, and youtube link
winston_short = media.Movie("Winston - Recall",
                            "Winston has a huge decision to make",
                            "winston_art.jpg",
                            "https://www.youtube.com/watch?v=sB5zlHMsM7k")
# Overwatch : Title, short description, poster image, and youtube link
overwatch_short = media.Movie("Overwatch - Trailer",
                              "Overwatch debut trailer",
                              "overwatch_art.jpg",
                              "https://www.youtube.com/watch?v=K_m8fcJb5tE")
# movies creates an array and orders the objects passed to media
movies = [sombra_short, doomfist_short, moira_short,
          mei_short, winston_short, overwatch_short]
# fresh_tomatoes function open_movies_page called to display page
fresh_tomatoes.open_movies_page(movies)

