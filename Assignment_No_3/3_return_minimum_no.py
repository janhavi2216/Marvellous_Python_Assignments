def minimum_no(n):
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}:" ))
        numbers.append(num)
    minimum = min(numbers)
    return numbers, minimum

def main():
    N = int(input("Enter number of elements? "))
    if N <= 0:
        print("Please enter a positive number.")
    else:
        nums, minimum = minimum_no(N)
        print("The entered numbers are: ",nums)
        print("Minimum element is :",minimum)

if __name__ == "__main__":
    main()