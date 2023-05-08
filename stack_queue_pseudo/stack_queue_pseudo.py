class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
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
            self.size -= 1
            return temp.value
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
        return self.size == 0


class pseudo_queue:
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()

    def enqueue(self, value):
        self.s1.push(value)

    def dequeue(self):
        if self.s1.is_empty() and self.s2.is_empty():
            return "queue is empty"

        elif self.s2.is_empty():
            while not self.s1.is_empty():
                # pop_ele=self.s1.pop()
                # self.s2.push(pop_ele)
                self.s2.push(self.s1.pop())
                
        return self.s2.pop()


if __name__ == '__main__':
    queue = pseudo_queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())  # 1
