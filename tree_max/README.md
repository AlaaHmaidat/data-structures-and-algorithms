# Tree Max
find maximum value

Arguments: none
Returns: number
## Whiteboard Process
![WhiteboardWorkflow01](../img/Tree%20Max.jpg)

## Approach & Efficiency
### Approach
   1. The `find_maximum` method first checks if the tree is empty (i.e., if the root is `None`). If the tree is empty, it returns `The tree is empty` since there are no values in the tree.

2. If the tree is not empty, it calls the `_find_maximum` helper method with the root node as an argument.

3. The `_find_maximum` method takes a node `root` as an argument and performs the following steps:
   - If the `root` is `None`, it means the node is empty, so it returns negative infinity (`float('-inf')`) to indicate that there are no values in this node.
   - Otherwise, it initializes the `max_value` variable with the value of the current node.
   - Then, it recursively calls `_find_maximum` on the left and right child nodes of the current node.
   - The values returned from the recursive calls are stored in `left_max` and `right_max` variables, respectively.
   - The method then compares the `left_max` and `right_max` values with the current `max_value` and updates `max_value` if necessary.
   - Finally, it returns the `max_value` as the maximum value found in the subtree rooted at the current node.

4. The `find_maximum` method returns the value returned by the `_find_maximum` method, which represents the maximum value in the entire binary tree.

In summary, the approach recursively traverses the binary tree and compares the maximum values found in the left and right subtrees with the current node's value to find the overall maximum value in the tree.
### Big O

The time complexity for both the find_maximum() method and the _find_maximum() helper method is O(N), where N is the number of nodes in the binary tree. The space complexity is O(H), where H is the height of the binary tree.
## Solution

Click [here](./tree_max.py)