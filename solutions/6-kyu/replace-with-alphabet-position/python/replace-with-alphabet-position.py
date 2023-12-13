def alphabet_position(text):
    import string
    alphabet = string.ascii_lowercase
    lowerText = text.lower()
    position = []
    
    for character in lowerText:
        if character in alphabet:
            position.append(str(alphabet.index(character)+1))
    return ' '.join(position)