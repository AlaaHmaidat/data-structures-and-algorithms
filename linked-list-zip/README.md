# linked list zip
Zip two linked lists

## Whiteboard Process
![WhiteboardWorkflow01](../img/linked%20list%20zip.jpg)

## Approach & Efficiency
### Approach
* The function takes two linked lists as input and returns a new linked list that contains alternating nodes from the two input linked lists.
* We first check if either of the input linked lists is empty, and if so, return the other linked list.
* We then create two pointers, current1 and current2, to point to the heads of the two input linked lists.
* We also create two more pointers, result_head and result_tail, to keep track of the head and tail of the new linked list that we will be creating.
* We iterate through both input linked lists simultaneously, adding alternating nodes to the new linked list, until we reach the end of one of the input linked lists.
* If there are remaining nodes in the first linked list, we add them to the new linked list.
* If there are remaining nodes in the second linked list, we add them to the new linked list.
* Finally, we return the head of the new linked list.

### Big O
Time Complexity: The time complexity of the zip_lists function depends on the length of the input linked lists. The while loop in the function iterates through both linked lists, and it takes constant time to perform each iteration. Therefore, the time complexity of this function is O(n), where n is the length of the input linked lists.

Space Complexity: The space complexity of the function is also linear with respect to the length of the input linked lists. The function creates a new linked list to store the zipped elements, which can have at most twice the length of the longer input list. Therefore, the space complexity of this function is O(n).


## Solution

Click [here](./linked_list_zip.py)