import re


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
        return num_of_items

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
        if self.size == 0:
            return "This stack is empty"
        return "This stack is not empty"


class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front == None:
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node  # ...
        

    def dequeue(self):
        if self.front == None:
            # raise Exception(
            #         "Sorry, This queue is empty")
            return (
                "Sorry, This queue is empty")
        elif self.front == self.rear:
            self.rear = None

        temp = self.front
        # Change the pointer for front to be point in the node after the front
        self.front = self.front.next
        temp.next = None

        return temp.value

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise Exception(
                "Sorry, This queue is empty")

    def is_empty(self):
        if self.front == None and self.rear == None:

            return "This queue is empty"
        return "This queue is not empty"


def validate_brackets(str):  # {} # }{
    # {}(){}pop # }{)(}{ dequeue
    # ()[[Extra Characters]] # ]] ...[[)(
    '''
    validate brackets
    Arguments: string
    Return: boolean
    representing whether or not the brackets in the string are balanced
    '''
    stack_Round  = stack()
    stack_Square = stack()
    stack_Curly  = stack()

    queue_Round  = queue()
    queue_Square = queue()
    queue_Curly  = queue()

    # x = re.findall(r'\{(.*?)\}', str)
    countR1 = 0
    countR2 = 0
    countS1 = 0
    countS2 = 0
    countC1 = 0
    countC2 = 0
    for i in str:  # ()[]
        if i == '(':
            stack_Round.push('(')  # (
            countR1 +=1
        elif i == ')':
            queue_Round.enqueue(')')  # )
            countR2 +=1
        elif i == '[':
            stack_Round.push('[')  # (
            countS1 +=1
        elif i == ']':
            queue_Round.enqueue(']')  # )
            countS2 +=1
        elif i == '{':
            stack_Round.push('{')  # (
            countC1 +=1
        elif i == '}':
            queue_Round.enqueue('}')  # )
            countC2 +=1
    if countR1 == countR2 and countS1 == countS2 and countC1 == countC2 :
        top = stack_Round.pop()
        if stack_Round.index(top) != queue_Round.index(i):
                return False
    return len(stack_Round) == 0
        



    # for i in str:
    #     pop_v = stack1.pop()  # [
    #     # dequeue_v = queue1.dequeue() # )

    #     print(pop_v)

    #     if pop_v in queue1:
    #         print(True)
    #     print(False)


if __name__ == '__main__':

    validate_brackets('(({})[(]))')
