def solution(number):
    multiples = []
    
    if number < 0:
        return 0
    while number > 0:
        if (number - 1) % 3 == 0 or (number - 1) % 5 == 0:
            multiples.append(number - 1)
        number = number - 1
        
    return sum(multiples)
    
        
        