def find_next_square(sq):
    import math
    if math.sqrt(sq) == int(math.sqrt(sq)):
        return ((math.sqrt(sq)) + 1)** 2
    else:
        return -1
