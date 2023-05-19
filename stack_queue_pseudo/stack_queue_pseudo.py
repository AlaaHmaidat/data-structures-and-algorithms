class Node:
    def __init__(self, value):
        """
        Initialize a Node with a given value.
        """
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.top = None
        self.size = 0

    def push(self, value):
        """
        Pushes a value onto the top of the stack.
        """
        new_node = Node(value)

        if self.top:
            new_node.next = self.top

        self.top = new_node
        self.size += 1

    def pop(self):
        """
        Removes and returns the value at the top of the stack.
        If the stack is empty, returns a message indicating that the stack is empty.
        """
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        return "Sorry, this stack is empty"

    def peek(self):
        """
        Returns the value at the top of the stack without removing it.
        If the stack is empty, returns a message indicating that the stack is empty.
        """
        if self.top:
            return self.top.value
        else:
            return "Sorry, this stack is empty"

    def get_size(self):
        """
        Returns the size of the stack.
        """
        return self.size

    def is_empty(self):
        """
        Checks if the stack is empty.
        Returns True if the stack is empty, False otherwise.
        """
        return self.size == 0


class PseudoQueue:
    def __init__(self):
        """
        Initialize an empty pseudo queue using two stacks.
        """
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):
        """
        Adds a value to the pseudo queue.

        Args:
            value: The value to be enqueued.

        Returns:
            A message indicating the success of the enqueue operation.

        """
        self.s1.push(value)
        return 'successfully pushed into stack1'

    def dequeue(self):
        """
        Removes and returns the value at the front of the pseudo queue.
        If the pseudo queue is empty, returns a message indicating that the queue is empty.
        """
        if self.s1.is_empty() and self.s2.is_empty():
            return "Queue is empty"

        elif self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

        return self.s2.pop()


if __name__ == '__main__':
    queue = PseudoQueue()
    print(queue.enqueue(1))
    queue.enqueue(2)
    queue.enqueue(3)
    # [1, 2, 3]

    print(queue.dequeue())  # 1
    # The steps are to pop all elements from [1, 2, 3] (stack1 will be empty).
    # It will pop 3, 2, 1 and push them into stack2 [3, 2, 1].
    # Then it will pop from stack2, which is 1.

    queue.enqueue(4)
    # Push 4 to the first stack which is empty.
    # stack1: [4]

    print(queue.dequeue())  # 2
    # Pop from stack1, which is 4, then push it into stack2.
    # stack2: [4]
    # It will pop from stack2, which is 2.

    print(queue.dequeue())  # 3
    # Pop from stack2, which is 3.

    print(queue.dequeue())  # 4
    # Pop from stack2, which is 4.
