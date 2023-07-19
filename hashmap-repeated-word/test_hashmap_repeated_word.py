import pytest
from hashmap_repeated_word import repeated_word

def test_first_repeated_word():
    """
    Test case to check the first repeated word in the string.
    """
    actual = repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")[1]
    expected = 'summer'
    assert actual == expected

def test_first_repeated_word_with_single_repeated_word():
    """
    Test case to check the first repeated word in the string when there is only one repeated word.
    """
    actual = repeated_word("Once upon a time, there was a brave princess who...")[1]
    expected = 'a'
    assert actual == expected

def test_first_repeated_word_with_multiple_repeated_words():
    """
    Test case to check the first repeated word in the string when there are multiple repeated words.
    """
    actual = repeated_word("It was the best of times, it was the worst of times...")[1]
    expected = 'it'
    assert actual == expected

def test_first_repeated_word_with_empty_string():
    """
    Test case to check the first repeated word in an empty string.
    """
    actual = repeated_word("")[1]
    expected = 'The str is empty'
    assert actual == expected

def test_all_words():
    """
    Test case to check the items of the dictionary containing all words and their frequencies.
    """
    actual = set(repeated_word("Once upon a time, there was a brave princess who...")[0])
    expected = {('once', 1), ('upon', 1), ('a', 2), ('time', 1), ('there', 1), ('was', 1), ('brave', 1), ('princess', 1), ('who', 1)}
    assert actual == expected

def test_most_common_words():
    """
    Test case to check the most common words in the string.
    """
    actual = repeated_word("Once upon a time, there was a brave princess who...")[2]
    expected = ['once', 'a']
    assert actual == expected
