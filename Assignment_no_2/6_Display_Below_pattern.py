def display_pattern(n):
    for i in range(n):
        
        print("*", end=" ")  

        for j in range(n - i):
            print("*", end=" ")
        print()

def main():
    num = int(input("Enter a number: "))
    display_pattern(num)

    print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
