def delete_nth(order,max_e):
    listOfNumbers = []
    for number in order:
        if listOfNumbers.count(number) < max_e:
            listOfNumbers.append(number)
    
    return listOfNumbers
    
#firt solution:

def delete_nth(order,max_e):
    listOfNumbers = []
    for number in order:
        if listOfNumbers.count(number) == max_e:
            continue
        else:
            listOfNumbers.append(number)
    
    return listOfNumbers