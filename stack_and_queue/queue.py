try:
    from stack_and_queue.node import Node
except:
    from node import Node
class queue:
    def __init__(self): 
        self.front = None
        self.rear = None

    def enqueue(self,value): 
        '''
        add to the queue
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        '''
        new_node = Node(value)
        if self.front == None:
            self.front = new_node
            self.rear = new_node
            
        else:
            self.rear.next = new_node
            self.rear = new_node # ...
        return "successfully push onto a queue"

    def dequeue(self):
        '''
        delete from queue
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        '''
        if self.front == None:
            # raise Exception(
            #         "Sorry, This queue is empty")
            return (
                     "Sorry, This queue is empty")
        elif self.front == self.rear:
             self.rear = None
        
        temp = self.front
        self.front = self.front.next # Change the pointer for front to be point in the node after the front
        temp.next = None

        return f"successfully dequeue {temp.value} from the queue"
        
    def peek(self):
        '''
        peek from the queue
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        '''
        if self.front:
            return self.front.value
        else:
            raise Exception(
                    "Sorry, This queue is empty")
        
    def is_empty(self):
        '''
        check if queue is empty
        Arguments: none
        Returns: Boolean indicating whether or not the queue is empty
        '''
        if self.front == None and self.rear == None:
            
            return "This queue is empty"
        return "This queue is not empty"
            

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


        

           
        