def insert_sorted(sorted_list, value):
    """
    Inserts the given value into the sorted list in the correct position.

    Args:
        sorted_list (list): The sorted list.
        value: The value to be inserted into the sorted list.

    """
    i = 0
    while i < len(sorted_list) and value > sorted_list[i]:
        i += 1 
    while i < len(sorted_list):
        temp = sorted_list[i]
        sorted_list[i] = value
        value = temp
        i += 1
    sorted_list.append(value)


def insertion_sort(input_list):
    """
    Sorts the given list using the insertion sort algorithm.

    Args:
        input_list (list): The list to be sorted.

    Returns:
        list: The sorted list.

    """
    if len(input_list) == 0:
        return 'The list is empty'
    sorted_list = []
    sorted_list.append(input_list[0])

    for i in range(1, len(input_list)):
        insert_sorted(sorted_list, input_list[i])
    return sorted_list


print(insertion_sort([8,4,23,42,16,15]))