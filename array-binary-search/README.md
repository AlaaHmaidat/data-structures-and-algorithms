# Reverse Array

Given an list contain from integer numbers and given a key to search in list if its contain this key or not

input : list , key (integer number)

output :  if key exist return the index of it ,if not return -1

## Whiteboard Process

![WhiteboardWorkflow01](../img/whiteboard%20Binary%20search.jpg)

## Approach & Efficiency

1-create a function
2-pass the list and the key to binary search fun
3-create two variable rear=last index in the list , front = first index in the list
4-create while loop (if front less than or equal rear) go implement the code inside it
5-create  value equal midIndex
6-create if statement if key equal the value of midIndex return the index it self
7-else if key less than the value of midIndex decrement the rear  -1
8-else if key greater than the value of midIndex increment front +1
9-countenu looping until become false
10-if the key not in the list return -1

Time complexity -->O(log n) where n is the number of elements in the sorted list. This is because in each iteration of the while loop, the search interval is divided in half, which means that the algorithm eliminates half of the remaining elements in the search interval. 

Space complexity -->O(1) because it does not use any additional data structures

## Solution

[CODE](./array-binary-search.py)