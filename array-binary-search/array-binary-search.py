import math


def BinarySearch(list, key):
    lengthList = len(list)-1

    midIndex = math.ceil(lengthList / 2)
    # print(midIndex)
    if key == list[midIndex]:
        return list[midIndex]
    elif key >= list[midIndex]:
        for i in range(midIndex, lengthList):
            midIndex = math.ceil((lengthList+midIndex)/2)
            # print(midIndex)
            if key == list[midIndex]:
                return list[midIndex]
            elif key >= list[midIndex]:
                continue
    elif key <= list[midIndex]:
        for i in range(0, midIndex):
            midIndex = math.ceil(midIndex/2)
            # print(midIndex)
            if key == list[midIndex]:
                return list[midIndex]
            elif key <= list[midIndex] and midIndex!=1:
                continue
            elif key <= list[midIndex] and midIndex==1:
                return list[0]


list = [4, 8, 15, 16, 23, 42, 44, 45, 46]
val = 16

print(BinarySearch(list, val))
