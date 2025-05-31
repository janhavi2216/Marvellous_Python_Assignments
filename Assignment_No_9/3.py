#  program creating Multiprocessing to Factorial list of number 

import multiprocessing
import multiprocessing.pool

def Factorial(Value):
     Fact=1
     while Value>0:
         Fact=Fact*Value
         Value=Value-1
     return Fact

def main():

    data=[2,4,6,8,24,26,27,9,11,25]
    Ret=[]

    P=multiprocessing.Pool()
    Ret=P.map(Factorial,data)
    
    P.close()
    P.join()
    print("Factorial is :",Ret)


if __name__=="__main__":
    main()