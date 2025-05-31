import threading
import os

def Small(Value): 
    print("PID Small is ",os.getpid())
    for C in Value:
        if C>='a' and C<='z':
            print("Inside Small :",C)
     
def Capital(Value):
    print("PID Capital is ",os.getpid())
    for i in Value:
        if i>='A'and i<='Z':
            print("Inside Capital :",Cnt)

def Digit(Value):
    print("PID Digitis is :",os.getpid())
    for i in Value:
        if i>='0' and i<='9':
            print("Inside Digit :",i)
            
def main():
    print("PID main is ",os.getppid())
    print("Enter a String :",end="")
    String=input()


    T1=threading.Thread(target=Small,args=(String,))
    T2=threading.Thread(target=Capital,args=(String,))
    T3=threading.Thread(target=Digit,args=(String,))
    T1.start()
    T2.start()
    T3.start()
    T1.join()
    T2.join()
    T3.join()
    
if __name__=="__main__":
    main()