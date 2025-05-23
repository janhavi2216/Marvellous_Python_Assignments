def palindrome(n):
    return n == n[::-1]

user_input = input("Enter a string: ")

if palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
