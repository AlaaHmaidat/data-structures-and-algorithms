import math

def BinarySearch(list, key):
    '''
    Given a key to search in list if its contain this key or not

    Args:
        list: list of int value
        int : The key

    Returns:
        int: index or -1 
        
    Examples
        >>> BinarySearch( [4, 8, 15, 16, 23, 42, 50, 60, 80, 90, 100],8)
        1
        >>> BinarySearch( [4, 8, 15, 16, 23, 42, 50, 60, 80, 90, 100],1)
        -1
    '''
    last_index = len(list)-1
    front = 0
    rear = last_index
    while front <= rear:
        midIndex = math.floor((front+rear) / 2)
        if key == list[midIndex]:
            return midIndex
        elif key < list[midIndex]:
            rear = midIndex-1
        elif key > list[midIndex]:
            front = midIndex+1

    return -1

def binary_search_obj(list, obj_key, value):
    last_index = len(list)-1
    front = 0
    rear = last_index
    while front <= rear:
        midIndex = math.floor((front+rear) / 2)
        mid_value = list[midIndex][obj_key]
        if mid_value == value:
            return midIndex
        elif mid_value < value:
            rear = midIndex-1
        elif mid_value > value:
            front = midIndex+1

    return -1

list = [{11: 4, 22: 8, 33: 15}, {
    11: 16, 22: 23, 33: 42}, {11: 50, 22: 60, 33: 80}]
key2 = 22
v = 8
print(binary_search_obj(list, key2, v))

# list = [4, 8, 15, 16, 23, 42, 50, 60, 80, 90, 100]
# key = 8
# print(BinarySearch(list, key))
