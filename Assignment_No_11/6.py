Rec=1
Sum=0
def Display(no):
    global Rec
    global Sum
    if(Rec<=no):
        Sum=Sum+Rec
        Rec=Rec+1
        Display(no)
    return Sum

def main():
    print("Enter a Number :",end="")
    Value=int(input())
    Ret=Display(Value)
    print("Sum of Number :",Ret)
   
if __name__=="__main__":
    main()