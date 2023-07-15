class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        # if list is empty
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return '{}'.format(values)


class Hashtable():
    def __init__(self, size=3):
        self.size = size
        self.arr = [None]*size
        self.ckeys = []

    def set(self, key, value):
        '''
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        Should a given key already exist, replace its value from the value argument given to this method.
        '''
        index = self.hash(key)
        linkedList = LinkedList()

        if not self.arr[index]:# if the Bucket is empty
                new_pair = [key,value] # store the new pair 
                self.arr[index] = linkedList
                linkedList.add(new_pair)

        else: # collision happeded
            # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
            # If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
            #x = isinstance("Hello", (str, float, int, str, list, dict, tuple)) -> True
            if isinstance(self.arr[index],LinkedList):
                self.arr[index].add([key,value])

            else: # if the bucket contains pairs
                existing_pair = self.arr[index] # store the existing pair
                new_pair = [key,value] # store the new pair 
                self.arr[index] = linkedList
                linkedList.add(existing_pair)
                linkedList.add(new_pair)

        self.ckeys.append(key)


    def get(self, key):
        '''
        Arguments: key
        Returns: Value associated with that key in the table
        '''
        index = self.hash(key)
        

        llist= self.arr[index] # The llist in this index
        temp = llist.head
        while temp:
            if temp.data[0]== key:
                return temp.data[1]
            temp = temp.next 
            
        return 'This key does not exist' 

    def has(self, key):
        '''
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        '''
        index = self.hash(key)
        
        llist= self.arr[index] # The llist in this index
        temp = llist.head
        while temp:
            if temp.data[0]== key:
                return True
            temp = temp.next 
            
        return False

    def keys(self):
        '''
        Returns: Collection of keys
        '''
        return self.ckeys

    def hash(self, key):
        '''
        Arguments: key
        Returns: Index in the collection for that key
        '''
        sum = 0
        for i in key:
            char = ord(i)
            char *= 200
            sum += char

        index = sum % self.size
        return index


if __name__ == '__main__':

    hashtable = Hashtable()

    hashtable.set("A", 70)
    hashtable.set("B", 90)
    hashtable.set("C", 80)
    hashtable.set("E", 60)

    print("The value associated with that key in the table: ",hashtable.get("A"))
    print('if the key exists in the table already: ',hashtable.has("A"))
    print('if the key exists in the table already: ',hashtable.has("R"))
    print('Collection of keys: ',hashtable.keys())

    print(hashtable.arr[0])
    
