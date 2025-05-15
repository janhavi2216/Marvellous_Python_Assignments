import Arethematic
def Add(no1,no2):
    ans=no1+no2
    return ans
def Sub(no1,no2):
    ans= no1-no2
    return ans
def mult(no1,no2):
    ans=no1*no2
    return ans
def div(no1,no2):
    ans= no2 == 0 
    return ans 

def main():
    print("Enter first number: ")
    no1 = int(input())
    
    print("Enter second number: ")
    no2 = int(input())
    
    ans = Arethematic.Add(no1,no2)
    print("Addition is : ",ans)
    ans = Arethematic.Sub(no1,no2)
    print("Substraction is : ",ans)
    ans = Arethematic.Mult(no1,no2)
    print("Multiplication is : ",ans)
    ans = Arethematic.Div(no1,no2)
    print("Division is : ",ans)
    
if __name__=="__main__":
    main()


