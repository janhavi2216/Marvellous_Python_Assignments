user_input = input("Enter list: ")
numbers = list(map(int, user_input.split()))
double = list(map(lambda x: x * 2, numbers))

print("Doubled list:", double)
