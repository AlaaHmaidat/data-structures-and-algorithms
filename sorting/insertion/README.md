## Insertion Sort
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands. 

### Pseudocode
```
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```

### Trace
Sample Array: [8,4,23,42,16,15]

### Trace
Sample Array: [8, 4, 23, 42, 16, 15]

### Pass 1:
- Initial Array: [8, 4, 23, 42, 16, 15]
- sorted: [8]
- value: 4
- i: 0

- Comparing 4 with 8: 4 < 8 (True)
- Swapping values: temp = 8, sorted[0] = 4, value = 8
- Appending value to sorted: [4, 8]
- Pass 1 Result: [4, 8]

### Pass 2:
- sorted: [4, 8]
- value: 23
- i: 0

- Comparing 23 with 4: 23 > 4 (True)
- Incrementing i: i = 1
- Comparing 23 with 8: 23 > 8 (True)
- Incrementing i: i = 2
- Since i (2) is equal to sorted.length, the while loop ends.
- Swapping values: temp = 8, sorted[2] = 23, value = 8
- Appending value to sorted: [4, 8, 23]
- Pass 2 Result: [4, 8, 23]

### Pass 3:
- sorted: [4, 8, 23]
- value: 42
- i: 0

- Comparing 42 with 4: 42 > 4 (True)
- Incrementing i: i = 1
- Comparing 42 with 8: 42 > 8 (True)
- Incrementing i: i = 2
- Comparing 42 with 23: 42 > 23 (True)
- Incrementing i: i = 3
- Since i (3) is equal to sorted.length, the while loop ends.
- Appending value to sorted: [4, 8, 23, 42]
- Pass 3 Result: [4, 8, 23, 42]

### Pass 4:
- sorted: [4, 8, 23, 42]
- value: 16
- i: 0

- Comparing 16 with 4: 16 > 4 (True)
- Incrementing i: i = 1
- Comparing 16 with 8: 16 > 8 (True)
- Incrementing i: i = 2
- Comparing 16 with 23: 16 < 23 (False)
- Swapping values: temp = 23, sorted[2] = 16, value = 23
- Incrementing i: i = 3

- Swapping values: temp = 42, sorted[3] = 23, value = 42
- Incrementing i: i = 4

- Since i (4) is equal to sorted.length, the while loop ends.
- Appending value to sorted: [4, 8, 16, 23, 42]
- Pass 4 Result: [4, 8, 16, 23, 42]

### Pass 5:
- sorted: [4, 8, 16, 23, 42]
- value: 15
- i: 0

- Comparing 15 with 4: 15 > 4 (True)
- Incrementing i: i = 1
- Comparing 15 with 8: 15 > 8 (True)
- Incrementing i: i = 2
- Comparing 15 with 16: 15 < 16 (True)
- Since i (2) is less than sorted.length, the while loop continues.
- Swapping values: temp = 16, sorted[2] = 15, value = 16
- Incrementing i: i = 3

- Swapping values: temp = 23, sorted[3] = 16, value = 23
- Incrementing i: i = 4

- Swapping values: temp = 42, sorted[4] = 23, value = 42
- Incrementing i: i = 5

- Since i (5) is equal to sorted.length, the while loop ends.
- Appending value to sorted: [4, 8, 15, 16, 23, 42]
- Pass 5 Result: [4, 8, 15, 16, 23, 42]

![](../../img/Insertion%20sort.jpg)

### Efficency

- **Time Complexity**: The time complexity of Insertion Sort is generally O(n^2), where n is the number of elements in the input list. This means that the algorithm's performance is directly proportional to the square of the input size. In the best case scenario where the input list is already sorted, the time complexity can be reduced to O(n), making it more efficient.

- **Space Complexity**: The space complexity of Insertion Sort is O(1), which means it uses a constant amount of additional space. It does not require any significant extra memory relative to the input size. The sorting is done in-place, modifying the original list without requiring additional data structures.

Click[here](./insertion.py) to see the code
Click[here](./test_insertion.py) to see the test