def duplicate_encode(word):
    lowerWord = word.lower()
    encodeWord = ""
    for character in lowerWord:
        if lowerWord.count(character) == 1:
            encodeWord += '('
        else:
            encodeWord += ')'
            
    return encodeWord

#2:

def duplicate_encode(word):
    listOfLetters = list(word.lower())
    encodeWord = ""
    for character in listOfLetters:
        if listOfLetters.count(character) == 1:
            encodeWord += '('
        if listOfLetters.count(character) >= 2:
            encodeWord += ')'
    return encodeWord