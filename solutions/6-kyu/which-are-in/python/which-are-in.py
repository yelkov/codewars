def in_array(array1, array2):
    r =[]
    for substring in array1:
        for string in array2:
            if substring in string and substring not in r:
                r.append(substring)
                    
    return sorted(r)


#first solution:

def in_array(array1, array2):
    r =[]
    for substring in array1:
        for string in array2:
            if substring in string:
                if r.count(substring) < 1:
                    r.append(substring)
                    
    return sorted(r)