# Merge sort
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves.

```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

### Trace
Sample Array: [8,4,23,42,16,15]

### Pass 1:

- The input array is [8, 4, 23, 42, 16, 15].
- The Mergesort function is called with the entire array.
- Since the length of the array is greater than 1, the array is divided into two halves.
- Left subarray: [8, 4, 23]
- Right subarray: [42, 16, 15]
- The Mergesort function is called recursively on both subarrays.

### Pass 2:

For the left subarray [8, 4, 23]:
- The length is greater than 1, so it is divided into two halves.
- Left subarray: [8]
- Right subarray: [4, 23]
- The Mergesort function is called recursively on both subarrays.

### Pass 3:

For the left subarray [8]:
- The length is 1, so no further recursion is needed.

For the right subarray [4, 23]:
- The length is greater than 1, so it is divided into two halves.
- Left subarray: [4]
- Right subarray: [23]
- The Mergesort function is called recursively on both subarrays.

### Pass 4:

For the left subarray [4]:
- The length is 1, so no further recursion is needed.

For the right subarray [23]:
- The length is 1, so no further recursion is needed.

### Merging Subarrays:

For the left subarray [4] and the right subarray [23]:
- Since both subarrays have only one element, we compare them and merge them into the original right subarray [4, 23].

For the left subarray [8] and the right subarray [4, 23]:
- We merge the sorted left subarray [8] with the sorted right subarray [4, 23].
- After merging, the original array becomes [4, 8, 23].

### Pass 5:

For the right subarray [42, 16, 15]:
- The length is greater than 1, so it is divided into two halves.
- Left subarray: [42]
- Right subarray: [16, 15]
- The Mergesort function is called recursively on both subarrays.

### Pass 6:

For the left subarray [42]:
- The length is 1, so no further recursion is needed.

For the right subarray [16, 15]:
- The length is greater than 1, so it is divided into two halves.
- Left subarray: [16]
- Right subarray: [15]
- The Mergesort function is called recursively on both subarrays.

### Pass 7:

For the left subarray [16]:
- The length is 1, so no further recursion is needed.

For the right subarray [15]:
- The length is 1, so no further recursion is needed.

### Merging Subarrays:

For the left subarray [16] and the right subarray [15]:
- Since both subarrays have only one element, we compare them and merge them into the original right subarray [15, 16].

For the left subarray [42] and the right subarray [15, 16]:
- We merge the sorted left subarray [42] with the sorted right subarray [15, 16].
- After merging, the original array becomes [15, 16, 42].

### Final Merge:

- The left subarray [4, 8, 23] and the right subarray [15, 16, 42] are sorted.
- We merge the sorted left subarray [4, 8, 23] with the sorted right subarray [15, 16, 42].
- After merging, the final sorted array is [4, 8, 15, 16, 23, 42].


![mergesort](../../img/Mergesort%20(1).jpg)


### Efficency

- **Time Complexity**: The time complexity of the Merge Sort algorithm is O(n log n), where 'n' represents the number of elements in the input array. This complexity arises from the recursive nature of the algorithm, as it divides the array into halves until individual elements are reached and then merges them back together. Each division takes O(log n) time, and each merge operation takes O(n) time in the worst case.

- **Space Complexity**: The space complexity of the Merge Sort algorithm is O(n) since it requires additional space to store the temporary subarrays during the merging process. In the worst case, when the algorithm is sorting the smallest subarrays (individual elements), it needs to allocate space for n/2 temporary subarrays. However, this additional space is deallocated after each merge operation, so the overall space complexity is still O(n).

Click[here](./merge.py) to see the code
Click[here](./test_merge.py) to see the test