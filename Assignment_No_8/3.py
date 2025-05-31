import threading

def EvenList(Value):
    ESum = 0
    for i in Value:
        if i % 2 == 0:
            ESum = ESum + i
    print("Even Factor Sum :",ESum)

def OddList(Value):
     OSum = 0
     for i in Value:
        if i % 2!= 0:
            OSum = OSum + i
     print("Odd Factor Sum :",OSum)
                 
        
def main():
    print("Enter a number :",end="")
    size=int(input())

    Data=[]

    for i in range(size):
        no=int(input())
        Data.append(no)

    T1=threading.Thread(target=EvenList,args=(Data,))
    T2=threading.Thread(target=OddList,args=(Data,))
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    print("Exit from Main")

if __name__=="__main__":
    main()