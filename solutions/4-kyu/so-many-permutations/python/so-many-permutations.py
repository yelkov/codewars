def permutations(s):
    if len(s) <= 1:
        return list(s)
    
    result = set()
    for i,character in enumerate(s):
        remaining_character = s[:i] + s[i+1:]
        for permutation in permutations(remaining_character):
            result.add(character + permutation)
        

    return list(result)
        
        