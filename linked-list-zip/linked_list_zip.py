
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


class Linked_List_Zip:
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

    def zip_lists(self, list1, list2):
        """
        Searches in the linked list for a node with the given index.       

        Args:
            k: The index to searched in linked list.

        Returns:
            A value of node was found in the linked list using index.
        """
        temp1 = list1.head
        temp2 = list2.head

        length = 0

        print(temp1)

        # while (temp):
        #     length += 1  # Calculate the length of the linked list
        #     temp = temp.next

        # current = self.head  # Initialise temp
        # count = length-1  # Index of last node

        # while (current):
        #     if (k < 0 or k >= length):
        #         return "Exception"
        #     elif (count == k):
        #         return current.value
        #     elif (count > k):
        #         count -= 1
        #         current = current.next
        #         continue


if __name__ == '__main__':

    list1 = Linked_List_Zip()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = Linked_List_Zip()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    print(list1.zip_lists(list2))