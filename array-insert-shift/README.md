# Insert Shift Array

## Whiteboard Process
![WhiteboardWorkflow01](../img/whiteboard%20array-insert-shift.jpg)

## Approach & Efficiency
Approach:

1.Get the length of the input list.
2.Calculate the middle index of the list.
3.Calculate the number of indexes in the list.
4.Append the given value to the end of the list to extend the list.
5.While there are indexes after the middle index:
  1.Shift the element to the right by one position.
  2.Set the value at the middle index to the given value.
6.Return the modified list.

Efficiency:

The time complexity of this function is O(n) because in the worst-case scenario, it needs to shift all the elements after the middle index to the right by one position.
The space complexity of this function is O(1) because it does not use any additional data structures, and all modifications are done in-place in the input list.

## Solution
```
# Define the function
def insertShiftArray(list, value):
    #length of list
    lengthList = len(list)
    #ceil middel index
    midIndex = lengthList // 2 + (lengthList % 2)
    #number of index
    numderOfIndexs = lengthList - 1
    #add the value in list jest to extend the list
    list.append(value)
    #while loop for shift the value after middel index
    while numderOfIndexs >= midIndex:
        
        list[numderOfIndexs+1] = list[numderOfIndexs]
        #to stop while loop in middel
        numderOfIndexs -= 1
    #change the value in the middel    
    list[midIndex] = value

    return list

# Example usage
list = [42, 8, 15, 23, 42]
value = 16
print(insertShiftArray(list, value)) # Output: [42, 8, 15, 16, 23, 42]
```