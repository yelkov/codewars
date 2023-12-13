def tribonacci(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return signature[0:1]
    elif n == 2:
        return signature[:2]
    
    sequence = signature[:]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2] + sequence[-3])
        
    return sequence