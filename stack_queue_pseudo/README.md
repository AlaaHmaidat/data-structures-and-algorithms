# Stack Queue Pseudo
Implement Queue using Stacks

## Whiteboard Process
![WhiteboardWorkflow01](../img/Stack%20Queue%20Pseudo.jpg)

## Approach & Efficiency
### Approach
1. Create a new class called pseudo queue.
    * PseudoQueue class will implement our standard queue interface (the two methods listed below),
    * Internally, utilize 2 Stack instances to create and manage the queue

2. Methods:
* enqueue
    * Arguments: value
    * Inserts a value into the PseudoQueue, using a first-in, first-out approach.

* dequeue
    * Arguments: none
    * Extracts a value from the PseudoQueue, using a first-in, first-out approach.

### Big O
* enqueue method:
Time complexity: O(1), as we simply push the item onto the first stack.
Space complexity: O(1), as we only allocate a single node for the item in the stack.

* dequeue method:
Time complexity: O(n), where n is the number of items in the queue. In the worst case, where the second stack is empty and we need to transfer all items from the first stack to the second stack, we pop all items from the first stack and push them onto the second stack, which takes O(n) time. However, on average, this operation takes O(1) time since we only need to transfer items occasionally.
Space complexity: O(n), as we need to allocate space for the second stack to store all items in the queue. However, we can reuse this space for subsequent operations on the queue.


## Solution

Click [here](./stack_queue_pseudo.py)