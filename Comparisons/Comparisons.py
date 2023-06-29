class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres



def sort_movies_by_year(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
    return sorted_movies


def sort_movies_by_title(movies):
    def get_sort_key(movie):
        title = movie.title
        if title.startswith(("A ", "An ", "The ")):
            title = title[title.index(" ") + 1:]
        return title

    sorted_movies = sorted(movies, key=get_sort_key)
    return sorted_movies
