'''
def insertShiftArray(list, value):

    lengthList = len(list)

    list1 = []
    list2 = []

    length1 = (lengthList//2)+(lengthList % 2)+1
    length2 = lengthList-length1+1

    for item in range(0, length1-1):
        list1.append(list[item])
    list1.append(value)
    index = list1.index(value)

    for item in range(length2):
        list2.append(list[index+item])

    newList = list1+list2
    return newList
'''


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


list = [42, 8, 15, 23, 42]
value = 16
print(insertShiftArray(list, value))
