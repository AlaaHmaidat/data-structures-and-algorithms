# Challenge Title
### **Hash Table**

A hash table in Python is a data structure that allows you to store and retrieve values using key-value pairs. It provides efficient lookup, insertion, and deletion operations. Python's built-in dictionary type serves as a hash table. It uses a hashing function to convert keys into unique hash codes, ensuring quick access to values. Hash tables are commonly used for data storage and retrieval in Python due to their speed and versatility.

## Whiteboard Process
![Whiteboard](../img/Hash%20Table.jpg)

## Approach & Efficiency
The provided code implements a Hashtable class using separate chaining to handle collisions. Here's a breakdown of the approach used:

1. The `Node` class represents a node in a linked list. Each node stores a data value and a reference to the next node.

2. The `LinkedList` class represents a linked list and provides methods to add nodes at the end of the list and convert the list to a string representation.

3. The `Hashtable` class has the following attributes:
   - `size`: The size of the hashtable (number of buckets).
   - `arr`: An array representing the buckets of the hashtable.
   - `ckeys`: A list to keep track of all the keys in the hashtable.

4. The `set` method takes a key and a value as arguments. It hashes the key using the `hash` method to determine the bucket index. If the bucket is empty, a new linked list is created, and the key-value pair is added to the linked list. If the bucket already contains a linked list, the key-value pair is added to the existing list. If there is a collision and the bucket already contains a key-value pair, the existing pair is moved to the linked list, and the new pair is added. The key is also added to the `ckeys` list.

5. The `get` method takes a key as an argument and returns the value associated with that key. It hashes the key to determine the bucket index. If the bucket is empty, it returns None. If the bucket contains a linked list, it traverses the list to find the matching key and returns the associated value.

6. The `has` method takes a key as an argument and returns a boolean in the hashtable. It hashes the key to determine the bucket index. If the bucket is empty, it returns False. If the bucket contains a linked list, it traverses the list to find the matching key and returns True if found.

7. The `keys` method returns the collection of keys stored in the hashtable by returning the `ckeys` list.

8. The `hash` method takes a key as an argument and calculates the hash value by summing the ASCII values of the characters in the key and taking the modulus of the hashtable size. This determines the bucket index where the key-value pair will be stored.

Overall, this implementation uses separate chaining to handle collisions by storing linked lists in the hashtable's buckets. The `set`, `get`, `has`, and `keys` methods utilize the hash function to determine the bucket index for the given key.


- Time complexity:

Average case: O(1) for set(), get(), and has() operations. This assumes a uniform distribution of keys and minimal collisions.
Worst case: O(n) for set(), get(), and has() operations. This occurs when there are many collisions, and the linked list at each bucket becomes long.
- Space complexity:

O(n), where n is the number of elements stored in the hashtable. This is because the space usage grows linearly with the number of elements.

## Solution

Click [here](./hashtable.py) to see the code 
Click [here](./test_hashtable.py) to see the test 