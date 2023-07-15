class Nodeh:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        """
        Add a new node with the given data to the linked list.
        """
        node = Nodeh(data)
        # If the list is empty
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return '{}'.format(values)


class Hashtable:
    def __init__(self, size=3):
        self.size = size
        self.arr = [None] * size
        self.ckeys = []

    def set(self, key, value):
        """
        Set the key and value pair in the hashtable, handling collisions as needed.
        If a given key already exists, replace its value with the provided value argument.
        """
        index = self.hash(key)
        linkedList = LinkedList()

        if not self.arr[index]:
            # If the bucket is empty
            new_pair = [key, value]
            self.arr[index] = linkedList
            linkedList.add(new_pair)
        else:
            # Collision happened
            if isinstance(self.arr[index], LinkedList):
                self.arr[index].add([key, value])
            else:
                # If the bucket contains pairs
                existing_pair = self.arr[index]
                new_pair = [key, value]
                self.arr[index] = linkedList
                linkedList.add(existing_pair)
                linkedList.add(new_pair)

        self.ckeys.append(key)

    def has(self, key):
        """
        Check if the key exists in the hashtable.

        Returns:
        - Boolean, indicating if the key exists in the table already.
        """
        index = self.hash(key)
        llist = self.arr[index]
        temp = llist.head
        while temp:
            if temp.data[0] == key:
                return True
            temp = temp.next
        return False

    def keys(self):
        """
        Return a collection of keys in the hashtable.
        """
        return self.ckeys

    def hash(self, key):
        """
        Hash the key and return the index in the hashtable.

        Returns:
        - Index in the collection for that key.
        """
        index = key % self.size
        return index


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, root):
        """
        Perform pre-order traversal on the binary tree.

        Arguments:
        - root: The root node of the binary tree.

        Returns:
        - A list of values obtained through pre-order traversal.
        """
        list1 = []
        if root is not None:
            list1.append(root.value)
            list1.extend(self.pre_order(root.left))
            list1.extend(self.pre_order(root.right))
        return list1


class AddToBinaryTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self, value):
        """
        Add a new node with the given value to the binary search tree.
        """
        if self.root is None:
            # Edge case: tree is empty
            self.root = Node(value)
        self._add(self.root, value)

    def _add(self, root, value):
        """
        Helper method to add a new node with the given value to the binary search tree.
        """
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


def tree_intersection(tree1, tree2):
    """
    Find the common values between two binary trees using a hashtable.

    Arguments:
    - tree1: The first binary tree.
    - tree2: The second binary tree.

    Returns:
    - A list of common values found in both trees.
    """
    hashmap = Hashtable()
    intersection = []

    tree1_values = tree1.pre_order(tree1.root)
    for value in tree1_values:
        hashmap.set(value, True)

    tree2_values = tree2.pre_order(tree2.root)
    for value in tree2_values:
        if hashmap.has(value):
            intersection.append(value)

    return intersection


if __name__ == '__main__':
    tree1 = AddToBinaryTree()
    tree1.add(150)
    tree1.add(100)
    tree1.add(75)
    tree1.add(160)
    tree1.add(125)
    tree1.add(175)
    tree1.add(250)
    tree1.add(200)
    tree1.add(350)
    tree1.add(300)
    tree1.add(500)

    tree2 = AddToBinaryTree()
    tree2.add(42)
    tree2.add(100)
    tree2.add(15)
    tree2.add(160)
    tree2.add(125)
    tree2.add(175)
    tree2.add(600)
    tree2.add(200)
    tree2.add(350)
    tree2.add(4)
    tree2.add(500)

    common_values = tree_intersection(tree1, tree2)
    print("Common values:", common_values)