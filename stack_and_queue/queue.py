from node import Node

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        new_node = Node(value)
        if self.front == None:
            self.front = new_node
            self.rear = new_node
            
        else:
            self.rear.next = new_node
            self.rear = new_node # ...
        return "successfully push onto a stack"

    def dequeue(self):
        if self.front == None:
            raise Exception(
                    "Sorry, This queue is empty")
        elif self.front == self.rear:
             self.rear = None
        
        temp = self.front
        self.front = self.front.next # Change the pointer for front to be point in the node after the front
        temp.next = None

        return temp.value
        
    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise Exception(
                    "Sorry, This queue is empty")
        
    def is_empty(self):
        return self.front == None and self.rear == None
            

if __name__=="__main__":
    queue1 = queue()

    queue1.enqueue(1)
    queue1.enqueue(2)
    
    print(queue1.peek())
    print(queue1.is_empty())

    print(queue1.dequeue()) # 1
    print(queue1.dequeue()) # 2
    print(queue1.dequeue()) # This queue is empty
    print(queue1.is_empty())


        

           
        