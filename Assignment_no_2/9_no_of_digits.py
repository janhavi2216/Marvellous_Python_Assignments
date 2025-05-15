def count_digits(n):
    return len(str(abs(n)))  

def main():
    num = int(input("Enter a number: "))
    result = count_digits(num)
    print(f"Number of digits in {num} is: {result}")

if __name__ == "__main__":
    main()
