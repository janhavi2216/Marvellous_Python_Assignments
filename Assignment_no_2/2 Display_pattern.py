def display_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="  ")  # Two spaces for better alignment
        print()  # Move to the next line

# Accept input from user
def main():
    num = int(input("Enter a number: "))
    display_pattern(num)

if __name__ == "__main__":
    main()
        