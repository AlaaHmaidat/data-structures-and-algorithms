# Reverse Array

Given an list contain from integer numbers the first number should become the last num and the 2ed num should become one before last
input : list
output : revers list

## Whiteboard Process

![WhiteboardWorkflow01](../img/whiteboard%20array-reverse.jpg)

## Approach & Efficiency

loop in to list and reverse it

1-create a function
2-creates a new variable that contains a reversed version of the input list using [::1]
whach 1 is the number of steps from tail to first to revers list
3-return the revers array and print it

Time complexity -->O(n) because in the worst-case scenario, it needs to revers all the elements in the list.
Space complexity -->O(1) because it does not use any additional data structures.

## Solution

```python 
# Define the function
def reverseArray (list):

 respons = list[::-1]
 return respons

# Example usage
list = [11, 22, 33, 44, 55] # Output: [55, 44, 33, 22, 11]
print(reverseArray(list))
```
[CODE](./array-reverse.py)