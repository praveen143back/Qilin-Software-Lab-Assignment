def square(num):

    return num*num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]

squares = map(square, numbers)

print(list(squares))
