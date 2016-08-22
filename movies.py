import media
import fresh_tomatoes as ft
import yaml

'''
  Movies file contains a movies list needed for the open_movies_page(movies)
  method, Imported from fresh_tomatoes py file

'''

# Using PyYAML to load Story lines
with open('story_lines.yml', 'r') as f:
    story_lines = yaml.load(f)

# image_urls dictonary contains shortned links to movie poster
image_urls = {
    "independence_day":
    "https://goo.gl/AgQPbw",
    "scream":
    "https://goo.gl/nNt1CV",
    "brave_heart":
    "https://goo.gl/zzp6Cp",
    "theory_of_everything":
    "https://goo.gl/bEhncu"}

# youtube_urls dictonary contains shortned links to movie trailer
youtube_urls = {
    "independence_day":
    "https://youtu.be/B1E7h3SeMDk",
    "scream":
    "https://youtu.be/AWm_mkbdpCA",
    "brave_heart":
    "https://youtu.be/wj0I8xVTV18",
    "theory_of_everything":
    "https://youtu.be/Salz7uGp72c"
}

independence_day = media.Movie("Independence Day",
                               story_lines["independence_day"],
                               image_urls["independence_day"],
                               youtube_urls["independence_day"]
                               )
scream = media.Movie("Scream",
                     story_lines["scream"],
                     image_urls["scream"],
                     youtube_urls["scream"])

brave_heart = media.Movie("Brave Heart",
                          story_lines["brave_heart"],
                          image_urls["brave_heart"],
                          youtube_urls["brave_heart"])

theory_of_everything = media.Movie("The Theory Of Everything",
                                   story_lines["theory_of_everything"],
                                   image_urls["theory_of_everything"],
                                   youtube_urls["theory_of_everything"])

movies = [independence_day, scream, brave_heart, theory_of_everything]
ft.open_movies_page(movies)
