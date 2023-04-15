import math


def BinarySearch(list, key):
    last_index = len(list)-1
    front=0
    rear =last_index

    while front <= rear:
        midIndex = math.floor((front+rear) / 2)
        if key == list[midIndex]:
            return midIndex
        elif key < list[midIndex]:
            rear = midIndex-1
        elif key > list[midIndex]:
            front = midIndex+1

    return -1


list = [4, 8, 15, 16, 23, 42, 50, 60, 80, 90, 100]
key = 8

print(BinarySearch(list, key))
