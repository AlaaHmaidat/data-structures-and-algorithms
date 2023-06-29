import pytest

from Comparisons.Comparisons import Movie, sort_movies_by_title, sort_movies_by_year


def test_sort_movies_by_year():
    """
    Test case for sorting movies by year.
    """
    movies = [
        Movie("Movie 1", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Movie 2", 2004, ["Comedy"]),
        Movie("Movie 3", 1997, ["Drama", "Romance"]),
        Movie("Movie 4", 2019, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Movie 5", 1994, ["Crime", "Drama"]),
    ]

    sorted_movies = sort_movies_by_year(movies)
    expected_order = [2019, 2012, 2004, 1997, 1994]
    years = [movie.year for movie in sorted_movies]
    assert years == expected_order


def test_sort_movies_by_title():
    """
    Test case for sorting movies by title.
    """
    movies = [
        Movie("Movie 1", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Movie 2", 2004, ["Comedy"]),
        Movie("Movie 3", 1997, ["Drama", "Romance"]),
        Movie("Movie 4", 2019, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Movie 5", 1994, ["Crime", "Drama"]),
    ]

    sorted_movies = sort_movies_by_title(movies)
    expected_order = [
        "Movie 1",
        "Movie 2",
        "Movie 3",
        "Movie 4",
        "Movie 5",
    ]

    titles = [movie.title for movie in sorted_movies]
    assert titles == expected_order