Count=0
def CountZero(no):

    if no<0:
        no=-no
    global Count
    if no!=0:
        temp=no%10
        if temp==0:
            Count=Count+1
        no=no//10
        CountZero(no)
    return Count


def main():
    print("Enter a Number :",end="")
    Value=int(input())

    ret=CountZero(Value)
    print("Zero Count is :",ret)

if __name__=="__main__":
    main()