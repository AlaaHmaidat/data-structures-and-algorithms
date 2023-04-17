import pytest
from linked_list_insertions.linked_list_insertions import Linked_List_Insertions

# @pytest.mark.skip()
def test_empty_linked_list(llist):
    """
    Can successfully instantiate an empty linked list
    """
    actual = llist.__str__()
    expected = "Empty LinkedList"
    assert actual == expected

# @pytest.mark.skip()
def test_append__node_to_the_end_of_the_linked_list(llist):
    """
    Can successfully add a node to the end of the linked list
    """
    actual = llist.append("A")
    expected = f"insert A successfully"
    assert actual == expected

# @pytest.mark.skip()
def test__append_multiple_nodes(llist):
    """
    Can successfully add multiple nodes to the end of a linked list
    """
    llist.append("A")
    llist.append("B")

    actual = llist.__str__()
    expected = f' {{ A }} -> {{ B }} ->  NULL'
    assert actual == expected

# @pytest.mark.skip()
def test_append_node_before_a_node_located_in_the_middle_of_linked_list(llist):
    """
    Can successfully insert a node before a node located i the middle of a linked list
    """
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.insert_before("C","E")
    actual = llist.__str__()
    expected = f' {{ A }} -> {{ B }} -> {{ E }} -> {{ C }} -> {{ D }} ->  NULL'
    assert actual == expected

# @pytest.mark.skip()
def test_append_node_before_first_node_in_linked_list(llist):
    '''
    Can successfully insert a node before the first node of a linked list
    '''
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.insert_before("A","E")
    actual = llist.__str__()
    expected = f' {{ E }} -> {{ A }} -> {{ B }} -> {{ C }} -> {{ D }} ->  NULL'
    assert actual == expected

# @pytest.mark.skip()
def test_append_node_after_a_node_located_in_the_middle_of_linked_list(llist):
    '''
    Can successfully insert after a node in the middle of the linked list
    '''
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.insert_after("C","E")
    actual = llist.__str__()
    expected = f' {{ A }} -> {{ B }} -> {{ C }} -> {{ E }} -> {{ D }} ->  NULL'
    assert actual == expected

# @pytest.mark.skip()
def test_append_node_after_last_node_in_linked_list(llist):
    '''
    Can successfully insert a node after the last node of the linked list
    '''
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.insert_after("D","E")
    actual = llist.__str__()
    expected = f' {{ A }} -> {{ B }} -> {{ C }} -> {{ D }} -> {{ E }} ->  NULL'
    assert actual == expected

@pytest.fixture
def llist():
    llist = Linked_List_Insertions()
    return llist
