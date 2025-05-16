def get_numbers_and_sum(n):
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    total = sum(numbers)
    return numbers, total

def main():
    N = int(input("Enter number of elements? "))
    if N <= 0:
        print("Please enter a positive number.")
    else:
        nums, total = get_numbers_and_sum(N)
        print("The entered numbers are: ", nums)
        print("Sum of all elements:",total)

if __name__ == "__main__":
    main()