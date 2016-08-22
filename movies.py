import media
import fresh_tomatoes as ft

image_urls = {
    "independence_day":
    "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",
    "scream":
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/78/Scream_movie_poster.jpg/220px-Scream_movie_poster.jpg",
    "brave_heart":
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/55/Braveheart_imp.jpg/220px-Braveheart_imp.jpg",
    "theory_of_everything":
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Theory_of_Everything.jpg/220px-Theory_of_Everything.jpg"}

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

story_lines = {
    "independence_day":
    "Disparate groups of people who converge in the Nevada desert in the aftermath of a\
    calamitous attack by an ostensibly powerful extraterrestrial race from an unknown origin.",
    "scream":
    "High school students in the fictional town of Woodsboro, California,\
    who becomes the target of a mysterious killer known as Ghostface",
    "brave_heart":
    "William Wallace, a 13th-century Scottish warrior who led the Scots\
    in the First War of Scottish Independence against King Edward I of England",
    "theory_of_everything":
    "Jane Wilde Hawking,deals with her relationship with her ex-husband, theoretical physicist Stephen Hawking,\
    his diagnosis of motor neurone disease, and his success in physics"
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