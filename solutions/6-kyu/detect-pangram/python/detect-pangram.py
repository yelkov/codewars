def is_pangram(s):
    import string
    alphabet = string.ascii_lowercase   
    lowerS = s.lower()
    
    for letter in alphabet:
        if lowerS.count(letter) >= 1:
            continue
        else:
            return False
    return True
    