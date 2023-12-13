def permute_a_palindrome(input):
    oddList = []
    for letter in input:
        if letter in oddList:
            oddList.remove(letter)
        else:
            oddList.append(letter)
    return len(oddList) <= 1
        
    