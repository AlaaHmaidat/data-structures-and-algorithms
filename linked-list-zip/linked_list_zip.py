
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
    Takes two linked lists and zips them together, alternating nodes between the two lists.

    Args:
        head1: The head of the first linked list.
        head2: The head of the second linked list.

    Returns:
        The head of the new linked list that results from zipping the two input linked lists.
    """
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    current1 = head1
    current2 = head2
    result_head = Node(None)
    result_tail = result_head

    while current1 and current2:
        temp1 = current1.next
        temp2 = current2.next

        result_tail.next = Node(current1.value)
        result_tail = result_tail.next
        result_tail.next = Node(current2.value)
        result_tail = result_tail.next

        current1 = temp1
        current2 = temp2

    if current1:
        result_tail.next = current1
    else:
        result_tail.next = current2

    return result_head.next

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
    print("list3= " ,list3.__str__())