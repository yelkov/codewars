def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    
    squared_array1 = []
    for number in array1:
            squared_array1.append(number**2)
    if sorted(squared_array1) == sorted(array2):
            return True
    else:
        return False