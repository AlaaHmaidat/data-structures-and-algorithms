class Node:
    """
    Node class represents a node in a linked list.
    Each node contains a value and a reference to the next node.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the Node class.

        Arguments:
        - value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

    def __str__(self):
        """
        Returns a string representation of the node.

        Returns:
        - The string representation of the node.
        """
        return str(self.value)


class Queue:
    """
    Queue class represents a queue data structure implemented using linked list.
    It maintains references to the front and rear nodes of the queue.
    """

    def __init__(self):
        """
        Initializes a new instance of the Queue class.
        Creates an empty queue with front and rear set to None.
        """
        self.front = None
        self.rear = None

    def __str__(self):
        """
        Returns a string representation of the queue.

        Returns:
        - The string representation of the queue.
        """
        if self.front is None:
            return "Empty Queue"

        output = ""
        current = self.front
        while current:
            output += f"{current.value} -> "
            current = current.next

        output += "None"
        return output

    def enqueue(self, data):
        """
        Adds an element to the rear of the queue.

        Arguments:
        - data: The data to be added to the queue.
        """
        node = Node(data)

        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.

        Returns:
        - The value of the element removed from the front of the queue.
        """
        if self.is_empty():
            raise Exception("Nothing to dequeue from, the queue is empty!")

        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        """
        Returns the value of the element at the front of the queue without removing it.

        Returns:
        - The value of the element at the front of the queue.
        """
        if self.is_empty():
            raise Exception("Nothing to peek at, the queue is empty!")

        return self.front.value

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
        - True if the queue is empty, False otherwise.
        """
        return self.front is None


class TreeNode:
    """
    TreeNode class represents a node in a binary tree.
    Each node contains a value and references to its left and right child nodes.
    """

    def __init__(self, value):
        """
        Initializes a new instance of the TreeNode class.

        Arguments:
        - value: The value to be stored in the node.
        """
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        """
        Returns a string representation of the node.

        Returns:
        - The string representation of the node.
        """
        return str(self.value)


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


def breadth_first(root):
    """
    Performs breadth-first traversal on a binary tree.

    Arguments:
    - root: The root node of the binary tree to traverse.

    Returns:
    - A list of values obtained through breadth-first traversal,
      or the string 'The tree is empty!' if the tree is empty.
    """
    output = []
    queue = Queue()

    if not root:
        return 'The tree is empty!'

    queue.enqueue(root)

    while not queue.is_empty():
        dequeued = queue.dequeue()
        if dequeued:
            output.append(dequeued.value)

            if dequeued.left:
                queue.enqueue(dequeued.left)
            if dequeued.right:
                queue.enqueue(dequeued.right)

    return output


if __name__ == "__main__":
    # Create a binary tree with the given structure
    tree = binary_tree()
    node2_1 = TreeNode(2)
    node7 = TreeNode(7)
    node5_1 = TreeNode(5)
    node2_2 = TreeNode(2)
    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node5_2 = TreeNode(5)
    node11 = TreeNode(11)
    node4 = TreeNode(4)

    node2_1.left = node7
    node2_1.right = node5_1
    node7.left = node2_2
    node7.right = node6
    node5_1.right = node9
    node6.right = node5_2
    node9.right = node11
    node11.left = node4

    tree.root = node2_1

    print("Breadth-first traversal:", breadth_first(tree.root))