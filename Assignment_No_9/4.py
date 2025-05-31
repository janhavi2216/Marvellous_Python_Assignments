# program creating Normal Function,Thread And Multiprocess to Summing 1 to
#  10 million  to Calculate the time 

import threading
import multiprocessing
import multiprocessing.pool
import time


def Summing(Value):
     Sum=0
     for i in range(Value):
         Sum=Sum+i
     
     return Sum

def main():
    No=1000000

    NormalStartTime=time.time()
   # Summing(No)
    Ret =Summing(No)
    print("Normal Function Sum :",Ret)
    NormaEndTime=time.time()
    
    ThreadStartTime=time.time()
    T=threading.Thread(target=Summing,args=(No,))
    T.start()
    T.join()
    ThreadEndTime=time.time()
    
    processStartTime=time.time()
    P=multiprocessing.Pool()
    
    Ret=P.map(Summing,[No])
    P.close()
    P.join()
    print("Multiprocessing  Sum :",Ret)
    processEndTime=time.time()

    print("Normal Time :",NormaEndTime-NormalStartTime)
    print("Thread Time :",ThreadEndTime-ThreadStartTime)
    print("Process time :",processEndTime-processStartTime)

if __name__=="__main__":
    main()  