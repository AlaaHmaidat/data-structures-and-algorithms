import pytest
from tree_breadth_first.tree_breadth_first import binary_tree, TreeNode, breadth_first

def test_if_tree_empty():
    """
    Test case to check if the breadth-first traversal works correctly for an empty tree.
    """
    tree = binary_tree()
    actual = breadth_first(tree.root)
    expected = 'The tree is empty!'
    assert actual == expected

def test_if_tree_have_one_val():
    """
    Test case to check if the breadth-first traversal works correctly for a tree with a single node.
    """
    tree = binary_tree()
    node1 = TreeNode(1)
    tree.root = node1

    actual = breadth_first(tree.root)
    expected = [1]
    assert actual == expected

def test_if_tree_have_multi_val():
    """
    Test case to check if the breadth-first traversal works correctly for a tree with multiple nodes.
    """
    tree = binary_tree()
    node2_1 = TreeNode(2)
    node7 = TreeNode(7)
    node5_1 = TreeNode(5)
    node2_2 = TreeNode(2)
    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node5_2 = TreeNode(5)
    node11 = TreeNode(11)
    node4 = TreeNode(4)

    node2_1.left = node7
    node2_1.right = node5_1
    node7.left = node2_2
    node7.right = node6
    node5_1.right = node9
    node6.right = node5_2
    node9.right = node11
    node11.left = node4

    tree.root = node2_1
    
    actual = breadth_first(tree.root)
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expected

def test_if_tree_have_left_subtree_only():
    """
    Test case to check if the breadth-first traversal works correctly for a tree with only a left subtree.
    """
    tree = binary_tree()
    node2_1 = TreeNode(2)
    node7 = TreeNode(7)
    node5_1 = TreeNode(5)
    node2_2 = TreeNode(2)

    node2_1.left = node7
    node2_1.right = node5_1
    node7.left = node2_2

    tree.root = node2_1

    actual = breadth_first(tree.root)
    expected = [2, 7, 5, 2]
    assert actual == expected

def test_if_tree_have_right_subtree_only():
    """
    Test case to check if the breadth-first traversal works correctly for a tree with only a right subtree.
    """
    tree = binary_tree()
    node2_1 = TreeNode(2)
    node5_1 = TreeNode(5)
    node6 = TreeNode(6)
    node5_2 = TreeNode(5)

    node2_1.right = node5_1
    node5_1.right = node6
    node6.right = node5_2

    tree.root = node2_1

    actual = breadth_first(tree.root)
    expected = [2, 5, 6, 5]
    assert actual == expected


