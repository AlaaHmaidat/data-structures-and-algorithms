
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

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            A string that lists the values of each node in the linked list, separated by '->' symbols.
            If the linked list is empty, returns the string 'Empty LinkedList'.
        """
        output = " "

        if self.head is None:
            output = "Empty LinkedList"

        else:
            temp = self.head
            while temp:
                output += f'{{ {temp.value } }} -> '
                temp = temp.next
            output += " NULL"
        return output


def zip_lists(head1, head2):
    """
    Searches in the linked list for a node with the given index.       

    Args:
        k: The index to searched in linked list.

    Returns:
        A value of node was found in the linked list using index.
    """

    # List1 is empty then return List2
    if head1 is None:
        print(head2)

    if head2 is None:
        print(head1)

    temp1 = head1
    temp1.next = head2

    temp2 = head2
    # temp2.next = head1
    # temp2 = head2
    # temp2.next =head1
    # print(head2)


if __name__ == '__main__':

    list1 = Linked_List_Zip()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = Linked_List_Zip()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    list3 = Linked_List_Zip()

    list3.head = zip_lists(list1.head, list2.head)

    print("list1= ", list1.__str__())
    print("list2= ", list2.__str__())
    print("{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL")
