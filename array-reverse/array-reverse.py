
def reverseArray (list):
 
 #The [::-1] syntax is called extended slicing and allows you to select a range of elements from a sequence. In this case, it selects the entire sequence (:) but with a step of -1 (::-1), effectively reversing the order of the sequence

 respons = list[::-1] 
 # arr.reverse()
 return respons


list = [11, 22, 33, 44, 55]
print(reverseArray(list))
