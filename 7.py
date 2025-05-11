def is_divisible_by_5(number):
    return number % 5 == 0

# Get input from the user
try:
    user_input = int(input("Enter a number: "))
    result = is_divisible_by_5(user_input)
    print("Divisible by 5:", result)
except ValueError:
    print("Please enter a valid integer.")

