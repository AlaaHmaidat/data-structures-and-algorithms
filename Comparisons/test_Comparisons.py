import pytest

from Comparisons.Comparisons import Movie,sort_movies_by_title,sort_movies_by_year

import pytest

# Define the Movie class and sorting functions here...

# Define the test functions using pytest decorators
def test_sort_movies_by_year():
    movies = [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
        Movie("Titanic", 1997, ["Drama", "Romance"]),
        Movie("Avengers: Endgame", 2019, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Pulp Fiction", 1994, ["Crime", "Drama"]),
    ]

    sorted_movies = sort_movies_by_year(movies)
    expected_order = [2019, 2012, 1997, 1994, 2004]
    years = [movie.year for movie in sorted_movies]
    assert years == expected_order

def test_sort_movies_by_title():
    movies = [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Anchorman: The Legend of Ron Burgundy", 2004, ["Comedy"]),
        Movie("Titanic", 1997, ["Drama", "Romance"]),
        Movie("Avengers: Endgame", 2019, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Pulp Fiction", 1994, ["Crime", "Drama"]),
    ]

    sorted_movies = sort_movies_by_title(movies)
    expected_order = [
        "Avengers: Endgame",
        "The Avengers",
        "Titanic",
        "Anchorman: The Legend of Ron Burgundy",
        "Pulp Fiction",
    ]
    titles = [movie.title for movie in sorted_movies]
    assert titles == expected_order

# Execute the tests with pytest
if __name__ == "__main__":
    pytest.main()
