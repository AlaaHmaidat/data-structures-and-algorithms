
class Node:
    """
    A Node object represents a single element in a linked list.

    Args:
        value: The value stored in the node.
        next: A pointer to the next node in the sequence. Initially set to None.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List_Kth:
    """
    A Linked_List_Kth object represents a node value in linked list using index.

    Attributes:
        head: A pointer to the first node in the linked list. Initially set to None.
    """

    def __init__(self):
        """
        Initializes an empty linked list with a None value for head.
        """
        self.head = None

    def append(self, new_value):
        """
        Inserts a new node with the given value at the end of the linked list.

        Args:
            new_value: The value to be inserted into the linked list.

        Returns:
            A string indicating that the value has been successfully inserted.
        """
        node = Node(new_value)

        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        return f"insert {new_value} successfully"

    def kthFromEnd(self, k):
        """
        Searches in the linked list for a node with the given index.       

        Args:
            k: The index to searched in linked list.

        Returns:
            A value of node was found in the linked list using index.
        """
        temp = self.head
        length = 0

        while (temp):
            length += 1  # Calculate the length of the linked list
            temp = temp.next

        current = self.head  # Initialise temp
        count = length-1  # Index of last node

        while (current):
            if k < 0:
                raise Exception("Sorry, no numbers below zero")
                # return "Sorry, no numbers below zero"
            elif k >= length:
                raise Exception(
                    "Sorry, no numbers above length of linked list")
                # return "Sorry, no numbers above length of linked list"
            elif (count == k):
                return current.value
            elif (count > k):
                count -= 1
                current = current.next
                continue


if __name__ == '__main__':
    ll = Linked_List_Kth()
    ll.append(1)  # index: 3
    ll.append(3)  # index: 2
    ll.append(8)  # index: 1
    ll.append(2)  # index: 0

    print(ll.kthFromEnd(0))
