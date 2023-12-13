def repeats(arr):
    singleOcurrencies = []
    for number in arr:
        if arr.count(number) == 1:
            singleOcurrencies.append(number)
        
    return sum(singleOcurrencies)

#2:

def repeats(arr):
    singleOcurrencies = []
    for number in arr:
        if number in singleOcurrencies:
            singleOcurrencies.remove(number)
        else:
            singleOcurrencies.append(number)
    return sum(singleOcurrencies)