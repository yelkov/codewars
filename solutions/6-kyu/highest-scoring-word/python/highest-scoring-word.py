def high(x):
    import string
    alphabet = string.ascii_lowercase
    listWords = x.split()
    listValues = []
    
    for word in listWords:
        value = 0
        for character in word:
            if character in alphabet:
                value += alphabet.find(character)+1
        listValues.append(value)
        
    maxPosition = listValues.index(max(listValues))
    return listWords[maxPosition]
    
                
    