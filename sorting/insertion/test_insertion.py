import pytest
from insertion import insert_sorted,insertion_sort

# @pytest.mark.skip
def test_we_have_reverse_sorted():

    actual = insertion_sort([20,18,12,8,5,-2]) 
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_we_have_few_uniques():

    actual = insertion_sort([5,12,7,5,5,7]) 
    expected = [5,5,5,7,7,12]
    assert actual == expected


def test_we_have_nearly_sorted():

    actual = insertion_sort([2,3,5,7,13,11]) 
    expected = [2,3,5,7,11,13]
    assert actual == expected

def test_we_have_empty():

    actual = insertion_sort([]) 
    expected = 'The list is empty'
    assert actual == expected

def test_we_have_normal_list():

    actual = insertion_sort([8,4,23,42,16,15]) 
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected