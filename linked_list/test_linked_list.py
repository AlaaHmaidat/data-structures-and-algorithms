# import pytest
# from linked_list.linked_list import Linked_List


# def test_empty_linked_list(llist):
#     """
#     Can successfully instantiate an empty linked list
#     """
#     actual = llist.__str__()
#     expected = "Empty LinkedList"
#     assert actual == expected


# def test_insert(llist):
#     """
#     Can properly insert into the linked list
#     """
#     actual = llist.insert("T")
#     expected = f"insert T successfully"
#     assert actual == expected


# def test_head_first_node(llist):
#     """
#     The head property will properly point to the first node in the linked list
#     """
#     llist.insert("T")
#     actual = llist.head.value
#     expected = "T"
#     assert actual == expected


# def test__insert_multiple_nodes(llist):
#     """
#     Can properly insert multiple nodes into the linked list
#     """
#     llist.insert("Test1")
#     llist.insert("Test2")
#     actual = llist.__str__()
#     expected = f' {{ Test2 }} -> {{ Test1 }} ->  NULL'
#     assert actual == expected


# def test_search_true(llist):
#     """
#     Will return true when finding a value within the linked list that exists
#     """
#     llist.insert("T")
#     actual = llist.includes("T")
#     expected = True
#     assert actual == expected


# def test_search_false(llist):
#     """
#     Will return false when searching for a value in the linked list that does not exist
#     """
#     actual = llist.includes("T")
#     expected = False
#     assert actual == expected


# def test_return(llist):
#     """
#     Can properly return a collection of all the values that exist in the linked list
#     """
#     llist.insert("T")
#     actual = llist.__str__()
#     expected = f' {{ T }} ->  NULL'
#     assert actual == expected


# @pytest.fixture
# def llist():
#     llist = Linked_List()
#     return llist
