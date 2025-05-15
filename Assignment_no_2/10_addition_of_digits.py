def sum_of_digits(n):
    n = abs(n)  
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total

def main():
    num = int(input("Enter a number: "))
    result = sum_of_digits(num)
    print(f"Sum of digits in {num} is: {result}")

if __name__ == "__main__":
    main()