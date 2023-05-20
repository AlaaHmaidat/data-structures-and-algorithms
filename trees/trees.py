class Node:
    '''
    Node class that has properties for the value stored in the node, the left child node, and the right child node
    '''
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class binary_tree:
    '''
    Binary Tree class

    Define a method for each of the depth first traversals:
    pre order
    in order
    post order

    Each depth first traversal method should return an array of values, ordered appropriately.
    '''
    def __init__(self):
        self.root = None

    def pre_order(self,root):# root,left,right 
        '''
        Perform pre-order traversal on the binary tree.

        Arguments:
        - root: The root node of the binary tree.

        Returns:
        - A list of values obtained through pre-order traversal.
        '''
        list1=[]
        if root is not None:# root
            list1.append(root.value)
            list1.extend(self.pre_order(root.left)) # used to append the elements returned by the recursive calls to the traversal methods
            list1.extend(self.pre_order(root.right))

        return list1

    def in_order(self,root):# left,root,right 
        '''
        Perform in-order traversal on the binary tree.

        Arguments:
        - root: The root node of the binary tree.

        Returns:
        - A list of values obtained through in-order traversal.
        '''
        list1=[]
        if root is not None:# root
            list1.extend(self.in_order(root.left))
            list1.append(root.value)
            list1.extend(self.in_order(root.right)) 
        return list1
    def post_order(self,root):# left,right,root 
        '''
        Perform post-order traversal on the binary tree.

        Arguments:
        - root: The root node of the binary tree.

        Returns:
        - A list of values obtained through post-order traversal.
        '''
        list1=[]
        if root is not None:# root
            list1.extend(self.post_order(root.left))
            list1.extend(self.post_order(root.right)) 
            list1.append(root.value)
        return list1

class binary_search_tree(binary_tree):
    '''
     sub-class of the Binary Tree Class
    '''
    def __init__(self):
        binary_tree.__init__(self)

    def Add(self,value):
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
               

    def Contains(self,value):
        '''
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        '''
        return self._contains(self.root,value)
    
    def _contains(self,root,value):# helper method
        '''
        helper method
        Argument: value,root
        Returns: boolean indicating whether or not the value is in the tree at least once.
        '''
        if root is None:# edge cases
            return False
        elif root.value == value:
            return True
        
        # if type(value) == str:
            # if ord(root.value) < ord(value):
        
        if value <  root.value:
            if root.left is not None:
                if root.left.value == value:
                        return True
                else:
                        if self._contains(root.left,value):
                            return True
                    
        if value >  root.value:
            if root.right is not None:
                    if root.right.value == value:
                        return True
                    else:
                        if self._contains(root.right,value):
                            return True

        return False        
                    

if __name__=='__main__':

    '''
        L
       / \
      C   T
     /   / \
    A   S   U

    '''
    tree1 = binary_search_tree()
    tree1.Add("L")
    tree1.Add("T")
    tree1.Add("U")
    tree1.Add("C")
    tree1.Add("A")
    tree1.Add("S") 
    
    print("Pre-order traversal:", tree1.pre_order(tree1.root)) # ['L', 'C', 'A', 'T', 'S', 'U']
    print("In-order traversal:", tree1.in_order(tree1.root)) # ['A', 'C', 'L', 'S', 'T', 'U']
    print("Post-order traversal:", tree1.post_order(tree1.root)) # ['A', 'C', 'S', 'U', 'T', 'L']

    print(tree1.Contains('C'))