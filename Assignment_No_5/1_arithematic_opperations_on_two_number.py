

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

def sum_result(num1,num2):
    ans1=num1+num2
    return ans1
def diffrence(num1,num2):
    ans2=num1-num2
    return ans2
def product(num1,num2):
    ans3=num1*num2
    return ans3
def division(num1,num2):
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (cannot divide by zero)"
    
print("Sum:", sum_result)
print("Difference:", diffrence)
print("Product:", product)
print("Division:",division)


