import pytest
from trees.trees import binary_search_tree

def test_can_successfully_instantiate_an_empty_tree():
    """
    Test if an empty tree can be instantiated successfully.
    """
    tree1 = binary_search_tree()
    actual = tree1.pre_order(tree1.root)
    expected = []
    assert actual == expected

def test_can_successfully_instantiate_tree_with_single_root_node():
    """
    Test if a tree with a single root node can be instantiated successfully.
    """
    tree1 = binary_search_tree()
    tree1.Add("L")
    actual = tree1.in_order(tree1.root)
    expected = ["L"]
    assert actual == expected

def test_for_Binary_Search_Tree_can_successfully_add_left_child_and_right_child_properly_to_a_node():
    """
    Test if a binary search tree can successfully add left and right children to a node.
    Expected tree:
        L
       / \
      C   T
    """
    tree1 = binary_search_tree()
    tree1.Add("L")
    tree1.Add("T")
    tree1.Add("C")
    actual = tree1.in_order(tree1.root)
    # we can check that from in order method it should return [T,L,C]
    expected = ['C', 'L', 'T']
    assert actual == expected

def test_can_successfully_return_collection_from_preorder_traversal():
    """
    Test if the preorder traversal returns the correct collection of values.
    """
    tree1 = binary_search_tree()
    tree1.Add("L")
    tree1.Add("T")
    tree1.Add("U")
    tree1.Add("C")
    tree1.Add("A")
    tree1.Add("S") 
    actual = tree1.pre_order(tree1.root)
    expected = ['L', 'C', 'A', 'T', 'S', 'U']
    assert actual == expected

def test_can_successfully_return_collection_from_inorder_traversal():
    """
    Test if the inorder traversal returns the correct collection of values.
    """
    tree1 = binary_search_tree()
    tree1.Add("L")
    tree1.Add("T")
    tree1.Add("U")
    tree1.Add("C")
    tree1.Add("A")
    tree1.Add("S") 
    actual = tree1.in_order(tree1.root)
    expected = ['A', 'C', 'L', 'S', 'T', 'U']
    assert actual == expected

def test_can_successfully_return_collection_from_postorder_traversal():
    """
    Test if the postorder traversal returns the correct collection of values.
    """
    tree1 = binary_search_tree()
    tree1.Add("L")
    tree1.Add("T")
    tree1.Add("U")
    tree1.Add("C")
    tree1.Add("A")
    tree1.Add("S") 
    actual = tree1.post_order(tree1.root)
    expected = ['A', 'C', 'S', 'U', 'T', 'L']
    assert actual == expected