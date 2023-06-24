def Mergesort(arr):
    n = len(arr)
    if n == 0:
        return 'The list is empty'
    if n > 1:
        mid = n // 2
        left = arr[:mid]  # Slice the array from index 0 to mid (exclusive)
        right = arr[mid:]  # Slice the array from mid to the end

        # sort the left side
        Mergesort(left)
        # sort the right side
        Mergesort(right)
        # merge the sorted left and right sides together
        Merge(left, right, arr)

    return arr

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # If there are remaining elements in the right subarray
    if i == len(left):
        # Copy the remaining elements from the right subarray to the main array
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    else:
        # If there are remaining elements in the left subarray,
        # copy them to the main array (arr) starting from position k
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

# Example usage
arr = [8,4,23,42,16,15]
Mergesort(arr)
print(arr)
