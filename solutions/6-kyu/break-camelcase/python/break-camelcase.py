def solution(s):
    outputWord = ""
    for character in s:
        if character.isupper():
            outputWord += " " + character
        else:
            outputWord += character
        
    return outputWord

#first solution:

def solution(s):
    outputWord = ""
    for character in s:
        if character.islower():
            outputWord += character
        elif character == "":
            outputWord += character
        else:
            outputWord += " " + character
        
    return outputWord