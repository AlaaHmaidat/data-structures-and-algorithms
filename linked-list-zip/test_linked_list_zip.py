import pytest
from linked_list_zip import Linked_List_Zip,zip_lists

def test_if_list1_is_empty():
    list1 = Linked_List_Zip()
    list2 = Linked_List_Zip()
    list3 = Linked_List_Zip()    

    list2.append(5)
    list2.append(9)
    list2.append(4)

    list3.head = zip_lists(list1.head, list2.head)
    
    assert list2.__str__() == list3.__str__()

    
def test_if_list2_is_empty():
    list1 = Linked_List_Zip()
    list2 = Linked_List_Zip()
    list3 = Linked_List_Zip()    

    list1.append(5)
    list1.append(9)
    list1.append(4)

    list3.head = zip_lists(list1.head, list2.head)
    
    assert list1.__str__() == list3.__str__()


def test_if_two_lists_is_empty():
    list1 = Linked_List_Zip()
    list2 = Linked_List_Zip()
    list3 = Linked_List_Zip()    

    list3.head = zip_lists(list1.head, list2.head)
    
    actual = list3.__str__()
    expected = 'Empty LinkedList'
    assert  actual == expected

def test_if_each_test_have_one_element():
    list1 = Linked_List_Zip()
    list1.append(1)

    list2 = Linked_List_Zip()
    list2.append(2)

    list3 = Linked_List_Zip()    

    list3.head = zip_lists(list1.head, list2.head)
    
    actual = list3.__str__()
    expected = ' { 1 } -> { 2 } ->  NULL'
    assert  actual == expected

def test_if_each_test_have_multi_element():
    list1 = Linked_List_Zip()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = Linked_List_Zip()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    list3 = Linked_List_Zip()    

    list3.head = zip_lists(list1.head, list2.head)
    
    actual = list3.__str__()
    expected = ' { 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } ->  NULL'
    assert  actual == expected