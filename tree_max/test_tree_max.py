import pytest
from tree_max.tree_max import binary_search_tree

def test_if_tree_empty():
    '''
    Test to verify if the find_maximum method returns the correct result when the tree is empty.
    '''
    tree1 = binary_search_tree()

    actual = tree1.find_maximum()
    expected = 'The tree is empty'
    assert actual == expected

def test_if_tree_have_one_element():
    '''
    Test to verify if the find_maximum method returns the correct result when the tree has one element.
    '''
    tree1 = binary_search_tree()
    tree1.add(1)
    
    actual = tree1.find_maximum()
    expected = 1
    assert actual == expected

def test_if_tree_have_multi_element():
    '''
    Test to verify if the find_maximum method returns the correct result when the tree has multiple elements.
    '''
    tree1 = binary_search_tree()
    tree1.add(1)
    tree1.add(5)
    tree1.add(3)
    
    actual = tree1.find_maximum()
    expected = 5
    assert actual == expected

def test_if_tree_have_negative_element():
    '''
    Test to verify if the find_maximum method returns the correct result when the tree has negative elements.
    '''
    tree1 = binary_search_tree()
    tree1.add(-1)
    tree1.add(-5)
    tree1.add(-3)
    
    actual = tree1.find_maximum()
    expected = -1
    assert actual == expected

def test_if_tree_have_duplicate_element():
    '''
    Test to verify if the find_maximum method returns the correct result when the tree has duplicate elements.
    '''
    tree1 = binary_search_tree()
    tree1.add(2)
    tree1.add(2)
    
    actual = tree1.find_maximum()
    expected = 2
    assert actual == expected