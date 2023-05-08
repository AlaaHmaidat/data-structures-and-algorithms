try:
    from stack_and_queue.node import Node
except:
    from node import Node

class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)

        if self.top:
            # The pointer of the new_node point at the same point that the top point at
            new_node.next = self.top

        self.top = new_node  # Change the pointer for the top to be in the new_node
        self.size += 1  # increment the size
        num_of_items = self.size
        return f"successfully push {num_of_items} item onto a stack"

    def pop(self):
        
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -=1
            return f"successfully pop {temp.value} from the stack"
        # raise Exception("Sorry, This stack is empty")
        return ("Sorry, This stack is empty")
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            # raise Exception(
            #         "Sorry, This stack is empty")
            return ("Sorry, This stack is empty")
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        if self.size == 0:
            return "This stack is empty"
        return "This stack is not empty"
        
    
