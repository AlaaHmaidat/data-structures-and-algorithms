import pytest
from linked_list.linked_list import Linked_List


def test_empty_linked_list(llist):
    actual = llist.__str__()
    expected = "Empty LinkedList"
    assert actual == expected


def test_insert(llist):
    actual = llist.insert("T")
    expected = f"insert T successfully"
    assert actual == expected


def test_head_first_node(llist):
    llist.insert("T")
    actual = llist.head.value
    expected = "T"
    assert actual == expected


def test__insert_multiple_nodes(llist):
    llist.insert("Test1")
    llist.insert("Test2")
    actual = llist.__str__()
    expected = f' {{ Test2 }} -> {{ Test1 }} ->  NULL'
    assert actual == expected


def test_search_true(llist):
    llist.insert("T")
    actual = llist.includes("T")
    expected = True
    assert actual == expected


def test_search_false(llist):
    actual = llist.includes("T")
    expected = False
    assert actual == expected


def test_return(llist):
    llist.insert("T")
    actual = llist.__str__()
    expected = f' {{ T }} ->  NULL'
    assert actual == expected


@pytest.fixture
def llist():
    llist = Linked_List()
    return llist
