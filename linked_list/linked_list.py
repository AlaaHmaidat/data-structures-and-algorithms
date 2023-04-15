'''
head -->|A|next|-->|B|next|-->None

--insert in the first of linked list:
head -->|C|next|-->|A|next|-->|B|next|-->None
   
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Linked_List:

    def __init__(self):
        self.head = None

    def insert(self, value):
        # for v in value: def insert(self, *value):

            # Create a new node with the given value
            node = Node(value)

            # Set the 'next' pointer of the new node to the current head of the list
            node.next = self.head

            # Update the 'head' pointer to point to the new node, making it the new head of the list
            self.head = node

            return f"insert {value} successfully"

    def includes(self, value):
        temp = self.head

        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def __str__(self):

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
    

class Doubly_Linked_List:

    def __init__(self):
        self.head = None

    def insert(self, value):
        # for v in value:

            # Create a new node with the given value
            node = Node(value)

            # Set the 'next' pointer of the new node to the current head of the list
            node.next = self.head

            if self.head is not None:
                node.prev = node

            # Update the 'head' pointer to point to the new node, making it the new head of the list
            self.head = node

            return f"insert {value} successfully"

    # def includes(self, value):
    #     values = []
    #     temp = self.head

    #     while temp:
    #         values.append(temp.value)
    #         temp = temp.next

    #     for value in values:
    #         return True
    #     return False

    def includes(self, value):
        temp = self.head

        while temp is not None:
            if temp.value == value:
                return True
            temp = temp.next
        return False
    
    def to_string(self):

        output = " "

        if self.head is None:
            output = "Empty LinkedList"

        else:
            temp = self.head
            while temp:
                output += f'{{ {temp.value} }} <-> '
                temp = temp.next
            output += " NULL"
        return output


    # delete the first matched node (key) in linkelist

    def delete_node(self, key):

        temp = self.head

        # 1. Empty linked list
        if (temp is None):
            return False

        # 2. If the target is the first node
        if (temp is not None):
            if (temp.value == key):
                self.head = temp.next
                temp = None
                return

        # search for the key and delete the target node
        while (temp is not None):
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

        # 3. The key does not Exists
        if (temp is None):
            return False

        # unlinke the target node from the linkedlist
        prev.next = temp.next
        temp = None
        return True
