numbers = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

largest = max(numbers)

print("The largest number is:", largest)
