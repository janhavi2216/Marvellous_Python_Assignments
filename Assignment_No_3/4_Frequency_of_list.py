def get_numbers(n):
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    return numbers

def find_frequency(numbers, target):
    return numbers.count(target)

def main():
    N = int(input("Enter number of elements ? "))
    if N <= 0:
        print("Please enter a positive number.")
    else:
        num_list = get_numbers(N)
        target = int(input("Enter the number to find its frequency: "))
        freq = find_frequency(num_list, target)
        print("The entered numbers are:",num_list)
        print("The frequency  is: ",freq)

if __name__ == "__main__":
    main()
