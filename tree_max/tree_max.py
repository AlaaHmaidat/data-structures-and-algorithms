class Node:
    '''
    Node class that has properties for the value stored in the node, the left child node, and the right child node
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binary_tree_max:
    '''
    Binary Tree class

    Define a method for each of the depth-first traversals:
    - pre-order
    - in-order
    - post-order

    Each depth-first traversal method should return an array of values, ordered appropriately.
    '''
    def __init__(self):
        self.root = None

    def find_maximum(self):
        '''
        Find the maximum value stored in the tree.

        Returns:
        - The maximum value stored in the tree (numeric).
        '''
        if self.root is None:
            return 'The tree is empty'

        return self._find_maximum(self.root)

    def _find_maximum(self, root):
        '''
        Helper method to find the maximum value stored in the tree.

        Arguments:
        - root: The root node of the binary tree.

        Returns:
        - The maximum value stored in the tree (numeric).
        '''
        if root is None:
            return float('-inf')  # Return negative infinity for an empty node

        max_value = root.value
        left_max = self._find_maximum(root.left)
        right_max = self._find_maximum(root.right)

        if left_max > max_value:
            max_value = left_max
        if right_max > max_value:
            max_value = right_max

        return max_value


class binary_search_tree(binary_tree_max):
    '''
    Sub-class of the Binary Tree Class
    '''
    def __init__(self):
        binary_tree_max.__init__(self)

    def add(self,value):
        '''
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        '''
        if self.root is None:# edge cases
             self.root = Node(value)
             
        self._add(self.root,value)
    
    def _add(self,root,value):# helper method
        '''
        helper method
        Arguments: value,root
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        '''
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self._add(root.left, value)
        elif value > root.value:
            if root.right is None:
                root.right = Node(value)
            else:
                self._add(root.right, value)

if __name__ == '__main__':

    tree1 = binary_search_tree()
    tree1.add(2)
    tree1.add(7)
    tree1.add(2)
    tree1.add(6)
    tree1.add(5)
    tree1.add(11)
    tree1.add(5)
    tree1.add(9)
    tree1.add(4)

    # Find the maximum value
    max_value = tree1.find_maximum()
    print("Maximum value:", max_value)