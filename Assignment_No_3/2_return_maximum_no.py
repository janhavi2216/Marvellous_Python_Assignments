def maximum_no(n):
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}:" ))
        numbers.append(num)
    maximum = max(numbers)
    return numbers, maximum

def main():
    N = int(input("Enter number of elements? "))
    if N <= 0:
        print("Please enter a positive number.")
    else:
        nums, maximum = maximum_no(N)
        print("The entered numbers are: ",nums)
        print("Maximun element is :",maximum)

if __name__ == "__main__":
    main()