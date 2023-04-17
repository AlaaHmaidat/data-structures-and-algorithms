# Binary Search 
Given an list contain from integer numbers and given a key to search in list if its contain this key or not

input : list , key (integer number)

output :  if key exist return the index of it ,if not return -1

## Whiteboard Process

![Whiteboard](../img/whiteboard%20Binary%20search.jpg)

## Approach & Efficiency

Approach:

1. create a function
2. pass the list and the key to binary search fun
3. create two variable rear=last index in the list , front = first index in the list
4. create while loop (if front less than or equal rear) go implement the code inside it
5. create  value equal midIndex
6. create if statement if key equal the value of midIndex return the index it self
7. else if key less than the value of midIndex decrement the rear  -1
8. else if key greater than the value of midIndex increment front +1
9. countenu looping until become false
10. if the key not in the list return -1

Efficiency:

Time complexity -->O(log n) where n is the number of elements in the input list. This is because with each iteration of the while loop, the size of the remaining search space is halved. Therefore, the number of iterations required to find the key is proportional to the logarithm of the size of the input list.
Space complexity -->O(1) because it does not use any additional data structures

## Solution

[CODE](./array-binary-search.py)

## Stretch Goal
What would you need to change if the array contained objects (sorted on a given property), and you were searching for certain property value? Write out the pseudocode.

```python
Function binary_search_obj(list, obj_key,value):

    front equal 0
    rear equal length(list)-1

    while front less than or equal rear:

        midIndex equal math.floor((front+rear) / 2)
        mid_value equal list[midIndex][obj_key]

        if mid_value equal value:
            return midIndex

        else if mid_value less than value:
            rear equal midIndex-1

        else if mid_value grater than value:
            front equal midIndex+1

    return -1
```
