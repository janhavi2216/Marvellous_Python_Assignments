from functools import reduce

def Check70To90(No):
       if (No>=70 and No<=90):
              return No
           
def Increase(No):
            return No+10
def Product(A,B):
            return A*B

def FMR(Value):
       
        print("Input data :",Value)

        FData=list(filter(Check70To90,Value))
        print("Filter Output :",FData)

        MData=list(map(Increase,FData))
        print("Map OutPut :",MData)

        RData=reduce(Product,MData)
        print("Reduce Outpur :",RData)

def main():
    print("Number of Elements :",end="")
    size=int(input())


    if size<0:
        size=-size
    Data=list()

    print("Input Elements :")
    for i in range(size):
        no=int(input())
        Data.append(no)

    FMR(Data)
  
if __name__=="__main__":
    main()