def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

user_input = input("Enter list: ")
numbers = list(map(int, user_input.split()))

prime_numbers = list(filter(prime, numbers))

print("Prime numbers:", prime_numbers)
