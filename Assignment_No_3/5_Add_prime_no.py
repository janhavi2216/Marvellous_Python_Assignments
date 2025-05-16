import MarvellousNum 

def listPrime(numbers):
    total = 0
    for num in numbers:
        if MarvellousNum.ChkPrime(num):
            total += num
    return total



# Example usage
def main():
    
    N = int(input("Enter number of elements: "))
    num_list = []
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        num_list.append(num)

def sum_of_primes(numbers):
    return sum(num for num in numbers if MarvellousNum.ChkPrime(num))

    result = listPrime(num_list)
    print("Sum of prime numbers:",result)
    
if __name__ == "__main__":
    main()
