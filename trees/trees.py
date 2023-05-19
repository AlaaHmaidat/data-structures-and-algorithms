from Node import Node
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

    def pre_order(self,root,list1=[]):# root,left,right (the result shoud be in this ex = L T C A U S A)
        
        if root is not None:# root
            list1.append(root.value)
        if root.left is not None:# left
            self.pre_order(root.left,list1)
        if root.right is not None:# right
            self.pre_order(root.right,list1)

        return list1

    def in_order(self,root,list1=[]):# left,root,right (the result shoud be in this ex = C T A L S U A)
        if root is not None:# root
            self.in_order(root.left)
            list1.append(root.value)
            self.in_order(root.right) 
        return list1
    def post_order(self,root,list1=[]):# left,right,root (the result shoud be in this ex = C A T S A U L)
        
        if root is not None:# root
            self.post_order(root.left)
            self.post_order(root.right) 
            list1.append(root.value)
        return list1

class binary_search_tree(binary_tree):
    '''
     sub-class of the Binary Tree Class
    '''
    def __init__(self):
        binary_tree.__init__(self)

    def Add(value):
        '''
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        '''
        pass

    def Contains(self,value):
        '''
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        '''
        print(self.root.value)
        return self._contains(self.root,value)
    
    def _contains(self,root,value):# helper method
        print(root.value)
        '''
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        '''
        if root is None:# edge casses
            return False

        elif root.value == value:
            return True 
        

if __name__=='__main__':

    '''
        L
       / \
      T   U
     / \ / \
    C  A S  A

    '''

    tree1 = binary_search_tree()

    tree1.root = Node("L")
    tree1.root.left = Node("T")
    tree1.root.right = Node("U")
    tree1.root.left.left = Node("C")
    tree1.root.left.right = Node("A")
    tree1.root.right.left = Node("S")
    tree1.root.right.right = Node("A")

    print(tree1.Contains('L'))
