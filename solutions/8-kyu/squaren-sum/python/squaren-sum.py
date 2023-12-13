def square_sum(numbers):
    squares = []
    for number in numbers:
        squares.append(number**2)
    return sum(squares)