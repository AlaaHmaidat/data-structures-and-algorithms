# Linked List
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.

## Approach & Efficiency
1. create 2 classes (Node,Linked_List)
2. Node class contain (value(next,prev pointer))
3. Linked_List class contain the following methods (insert,includes,to srting)
4. insert
    1. Arguments: value
    2. Returns: nothing
    3. Adds a new node with that value to the head of the list with an O(1) Time performance.

5. includes
    1. Arguments: value
    2. Returns: a string representing all the values in the Linked List, formatted as:"{ a } -> { b } -> { c } -> NULL"

6. Write tests to prove the following functionality:
    1. Can successfully instantiate an empty linked list
    2. Can properly insert into the linked list
    3. The head property will properly point to the first node in the linked list
    4. Can properly insert multiple nodes into the linked list
    5. Will return true when finding a value within the linked list that exists
    6. Will return false when searching for a value in the linked list that does not exist
    7. Can properly return a collection of all the values that exist in the linked list

* The time complexity of the insert method is O(1), as it simply creates a new node and updates the head pointer, regardless of the size of the list.

* The time complexity of the includes method is O(n), where n is the number of nodes in the list. This is because in the worst case scenario, the method must iterate through the entire list to find the specified value.

* The space complexity of both methods is O(1), as they do not require any additional data structures that grow in size with the size of the input.

* The time complexity of the __str__ method is O(n), where n is the number of nodes in the list. This is because the method must iterate through each node in the list to build the string representation of the list.

* The space complexity of the __str__ method is also O(n), as it creates a string that is proportional to the number of nodes in the list.



## Solution

[CODE](./linked_list.py)