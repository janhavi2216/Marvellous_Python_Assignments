def sum_of_factors(n):
    if n <= 0:
        return "Please enter a positive integer."
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

# Accept input from user
def main():
    num = int(input("Enter a number: "))
    result = sum_of_factors(num)
    print(f"Sum of factors of {num} is: {result}")

    
if __name__ == "__main__":
    main()
