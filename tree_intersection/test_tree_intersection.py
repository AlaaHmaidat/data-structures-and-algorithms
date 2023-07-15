import pytest
from tree_intersection import AddToBinaryTree, tree_intersection

def test_tree_intersection():
    """
    Test case to check if common values are correctly returned from two binary trees.
    """
    tree1 = AddToBinaryTree()
    tree1.add(1)
    tree1.add(2)
    tree1.add(3)
    tree1.add(4)
    tree1.add(5)

    tree2 = AddToBinaryTree()
    tree2.add(4)
    tree2.add(5)
    tree2.add(6)
    tree2.add(7)
    tree2.add(8)

    expected_result = [4, 5]

    assert tree_intersection(tree1, tree2) == expected_result

def test_tree_intersection_empty_trees():
    """
    Test case to check if an empty list is returned when both trees are empty.
    """
    tree1 = AddToBinaryTree()
    tree2 = AddToBinaryTree()

    expected_result = []

    assert tree_intersection(tree1, tree2) == expected_result

def test_tree_intersection_no_common_values():
    """
    Test case to check if an empty list is returned when there are no common values between the trees.
    """
    tree1 = AddToBinaryTree()
    tree1.add(1)
    tree1.add(2)
    tree1.add(3)

    tree2 = AddToBinaryTree()
    tree2.add(4)
    tree2.add(5)
    tree2.add(6)

    expected_result = []

    assert tree_intersection(tree1, tree2) == expected_result
