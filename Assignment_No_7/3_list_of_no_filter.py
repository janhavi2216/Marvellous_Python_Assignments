user_input = input("Enter list: ")
numbers = list(map(int, user_input.split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)
