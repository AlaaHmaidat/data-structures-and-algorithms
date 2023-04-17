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
        self.prev = None


class Linked_List_Insertions:
    """
    A Linked_List_Insertions object represents a linked list data structure that stores a sequence of elements.

    Attributes:
        head: A pointer to the first node in the linked list. Initially set to None.
    """
    def __init__(self):
        """
        Initializes an empty linked list with a None value for head.
        """
        self.head = None

    def append(self,new_value):
        """
        Inserts a new node with the given value at the end of the linked list.

        Args:
            value: The value to be inserted into the linked list.

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

            
    def insert_before(self,val,new_value):
        """
        Inserts a new node with the given new_value before the val.

        Args:
            value: The value to be inserted into the linked list.
        """
        node = Node(new_value)
        
        if self.head is None:
            self.head = node
        elif self.head.value== val:
            # Set the 'next' pointer of the new node to the current head of the list
            node.next = self.head
            # Update the 'head' pointer to point to the new node, making it the new head of the list
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.value == val:
                    node.next = temp.next
                    temp.next = node
                    return
                temp = temp.next
            return 'No change, method exception'

                
                
    def insert_after(self,val,new_value):
        """
        Inserts a new node with the given new_value after the val.

        Args:
            value: The value to be inserted into the linked list.
        """
        node = Node(new_value)
        
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp is not None:
                if temp.value == val:
                    node.next = temp.next
                    temp.next = node
                    return
                temp = temp.next
        return 'No change, method exception'

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
    