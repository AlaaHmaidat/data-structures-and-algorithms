def arrayRemoveShift(list):
    #length of list
    lengthList = len(list)
   
    midIndex = lengthList // 2 
    #number of index
    item =list[midIndex]
    list.remove(item)

    return list

list = [42, 8, 23, 42]
print(arrayRemoveShift(list))
