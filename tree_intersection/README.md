# Challenge Title
### **Tree Intersection**
Find the common values between two binary trees using a hashtable.

## Whiteboard Process
![Whiteboard](../img/common%20values%20in%202%20binary%20trees.jpg)

## Approach & Efficiency

1. Create an empty hashtable (HashMap) to store the values from the first tree.
2. Perform a pre-order traversal on the first tree and add each value to the hashtable using the `set` method.
3. Initialize an empty list called `intersection` to store the common values.
4. Perform a pre-order traversal on the second tree.
5. For each value encountered during the traversal, check if it exists in the hashtable using the `has` method.
6. If the value exists in the hashtable, it is a common value, so append it to the `intersection` list.
7. Return the `intersection` list containing the common values found in both trees.


The time complexity is O(N), where N is the total number of nodes in the trees, and the space complexity is O(M), where M is the number of unique values in the first tree.

## Solution

Click [here](./tree_intersection.py) to see the code

Click [here](./test_tree_intersection.py) to see the test