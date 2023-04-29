import pytest
from linked_list_kth.linked_list_kth import Linked_List_Kth

# @pytest.mark.skip()
def test_Where_k_is_greater_than_the_length_of_the_linked_list(llist):
    """
    Can successfully return Exception if k greater than the length of the linked list
    """
    llist.append("A")
    llist.append("B")

    actual = llist.kthFromEnd(4)
    expected = "Exception"
    assert actual == expected

# @pytest.mark.skip()
def test_Where_k_and_the_length_of_the_list_are_the_same(llist):
    """
    Can successfully return Exception where k and the length of the list are the same
    """
    llist.append("A")
    llist.append("B")

    actual = llist.kthFromEnd(2)
    expected = "Exception"
    assert actual == expected

# @pytest.mark.skip()
def test_Where_k_is_not_a_positive_integer(llist):
    """
    Can successfully return Exception where k is not a positive integer
    """
    llist.append("A")
    llist.append("B")
        
    actual = llist.kthFromEnd(-2)
    expected = "Exception"
    assert actual == expected

# @pytest.mark.skip()
def test_Where_the_linked_list_is_of_a_size_1(llist):
    """
    Can successfully return the value of the node where the linked list is of a size 1
    """
    llist.append("A")
        
    actual = llist.kthFromEnd(0)
    expected = "A"
    assert actual == expected

# @pytest.mark.skip()
def test_where_k_is_not_at_the_end_but_somewhere_in_the_middle_of_the_linked_list(llist):
    '''
    Can successfully return the value in the node where k is not at the end, but somewhere in the middle of the linked list
    '''
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    actual = llist.kthFromEnd(2)
    expected = "B"
    assert actual == expected

@pytest.fixture
def llist():
    llist = Linked_List_Kth()
    return llist
