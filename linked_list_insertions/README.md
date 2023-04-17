
# Linked List Insertion
Inserting element in the linked list involves reassigning the pointers from the existing nodes to the newly inserted node. Depending on whether the new data element is getting inserted at the beginning or at the middle of the linked list

input : Node
output : Linked List
## Whiteboard Process
![WhiteboardWorkflow01](../img/Linked%20List%20Insertions.jpg)

## Approach & Efficiency
1. __init__(self): Initializes an empty linked list with a None value for head.
2. append(self, new_value): Inserts a new node with the given value at the end of the linked list.
    * Create a new node with the new_value.
    * If the linked list is empty (i.e., head is None), set head to the new node.
    * Otherwise, traverse the linked list until the end (temp.next is None) and set the next pointer of the last node to the new node.
3. insert_before(self, val, new_value): Inserts a new node with the new_value before the node with the value val.
    * Create a new node with the new_value.
    * If the linked list is empty (i.e., head is None), set head to the new node.
    * Otherwise, if the head node has the value val, set the next pointer of the new node to the current head of the list and update the head pointer to point to the new node.
    * Otherwise, traverse the linked list until a node with the value val is found (temp.next.value == val).
    * Set the next pointer of the new node to the node with the value val.
    * Set the next pointer of the node before the node with the value val to the new node.
4. insert_after(self, val, new_value): Inserts a new node with the new_value after the node with the value val.
    * Create a new node with the new_value.
    * If the linked list is empty (i.e., head is None), set head to the new node.
    * Otherwise, traverse the linked list until a node with the value val is found (temp.value == val).
    * Set the next pointer of the new node to the node after the node with the value val.
    * Set the next pointer of the node with the value val to the new node.
5. __str__(self): Returns a string representation of the linked list.
    * Initialize an empty string output.
    * If the linked list is empty (i.e., head is None), set output to "Empty LinkedList".
    * Otherwise, traverse the linked list and add each node's value to output followed by "->".
    * Add "NULL" to the end of output.
    * Return output.

1. __init__: O(1)
2. append: O(n), where n is the number of nodes in the linked list, because in the worst case we need to traverse the entire linked list to find the last node to append the new node.
3. insert_before: O(n), where n is the number of nodes in the linked list, because in the worst case we need to traverse the entire linked list to find the node with the value val before which we want to insert the new node.
4. insert_after: O(n), where n is the number of nodes in the linked list, because in the worst case we need to traverse the entire linked list to find the node with the value val after which we want to insert the new node.
5. __str__: O(n), where n is the number of nodes in the linked list, because we need to traverse the entire linked list to create the string representation of the linked list.

* The space complexity of this implementation is O(n), where n is the number of nodes in the linked list, because we need to store all of the nodes in memory.

## Solution

Click [here](./linked_list_insertions.py)