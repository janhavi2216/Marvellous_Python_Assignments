from functools import reduce
user_input = input("Enter list: ")
numbers = list(map(int, user_input.split()))

product = reduce(lambda x, y: x * y, numbers)

print("Product:", product)
