# Stack & Queue
Both the stack and queue are the linear data structure, which means that the elements are stored sequentially and accessed in a single run

## Whiteboard Process
![WhiteboardWorkflow01](../img/Whiteboard%20Linked%20List%20Kth.jpg)

## Approach & Efficiency

1. __init__(self): Initializes an empty linked list with a None value for head.

2. append(self, new_value): Inserts a new node with the given value at the end of the linked list.

    * Create a new node with the new_value.

    * If the linked list is empty (i.e., head is None), set head to the new node.
    * Otherwise, traverse the linked list until the end (temp.next is None) and set the next pointer of the last node to the new node.

3. kthFromEnd(self, k): Searches in the linked list for a node with the given index (k)
    * Create a temp which equal self.head.
    * Create a length variable which equal zero to calculate the length of the linked list

    * While temp not none increase length by 1 and make temp equal temp.next

    * Create a current which equal self.head.
    * Create a count which equal length-1 because we need start from zero.

    * While current not none
    * check if k less than 0 or grater than the length return Exception
    * Otherwise, if the count equal k return the value (current.value)
    * Otherwise, decrease the count by 1 and make current equal current.next and continue looping
    
### Big O
Big O for Stack & Queue:
The time and space complexity of the stack implementation are constant (O(1)) for all operations.


## Solution

Click [here](./stack.py) for Stack code
Click [here](./queue.py) for Queue code