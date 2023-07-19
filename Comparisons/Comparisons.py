import pytest

class Movie:
    """
    Represents a movie with a title, year, and genres.
    """

    def __init__(self, title, year, genres):
        """
        Initializes a Movie object.

        Args:
            title (str): The title of the movie.
            year (int): The year the movie was released.
            genres (list): A list of genres associated with the movie.
        """
        self.title = title
        self.year = year
        self.genres = genres

    def __repr__(self):
        """
        Returns a string representation of the Movie object.

        Returns:
            str: The formatted string representation of the Movie object.
        """
        return f"<Movie: {self.title} ({self.year})>"


def sort_movies_by_year(movies):
    """
    Sorts the movies by most recent year first.

    Args:
        movies (list): A list of Movie objects.

    Returns:
        list: The sorted list of Movie objects.
    """
    sorted_movies = sorted(movies, key=lambda movie: movie.year, reverse=True)
    return sorted_movies


def sort_movies_by_title(movies):
    """
    Sorts the movies alphabetically by title, ignoring leading "A"s, "An"s, or "The"s.

    Args:
        movies (list): A list of Movie objects.

    Returns:
        list: The sorted list of Movie objects.
    """
    def get_sort_key(movie):
        title = movie.title
        if title.startswith(("A ", "An ", "The ")):
            title = title[title.index(" ") + 1:]
        return title

    sorted_movies = sorted(movies, key=get_sort_key)
    return sorted_movies
    
if __name__=='__main__':
    # Create movie objects
    movie1 = Movie("The Movie 1", 2012, ["Action", "Adventure", "Sci-Fi"])
    movie2 = Movie("The Movie 2", 2020, ["Comedy"])
    movie3 = Movie("A Movie 3", 1997, ["Drama", "Romance"])

    # Create a list of movies
    movies = [movie1, movie2, movie3]

    # Sort movies by year
    sorted_movies_by_year = sort_movies_by_year(movies)
    print('Sort movies by year: ',sorted_movies_by_year)

    # Sort movies by title
    sorted_movies_by_title = sort_movies_by_title(movies)
    print('Sort movies by title: ',sorted_movies_by_title)


    # Run the tests
    # pytest.main()