# Task 1
# A simple function.
# Create a simple function called favorite_movie, which takes
# a string containing the name of your favorite movie.
# The function should then print “My favorite movie is
# named {name}”.


def favorite_movie(film_name):
    print(f'My favorite movie is named "{film_name}".\n')


if __name__ == "__main__":
    film = "Best movie in the world!"
    favorite_movie(film)
