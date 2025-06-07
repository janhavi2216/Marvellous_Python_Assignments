class BankAccount:
    ROI=10.5

    def __init__(self,name,amount):
        self.Name=name
        self.Amount=amount
    
    def Deposit(self):
        print("Enter an Amount that you want to Deposit :",end="")
        DAmount=int(input())
        self.Amount=self.Amount+DAmount
        print("Amount is Deposited :",DAmount)
        print("Total Amount is :",self.Amount)

    def WithDraw(self):
        print("Enter an Amount that you want to WithDrow :",end="")
        WAmount=int(input())
        if WAmount<self.Amount:
            self.Amount=self.Amount-WAmount
            print("Amount WithDraw is  :",WAmount)
            print("Remaining  Amount is :",self.Amount)     
        else:
            print("less than Total Amount")

    def CalculateIntrest(self):
        Intrest=(self.Amount*BankAccount.ROI)/100
        print("Intrest is :",Intrest)
    
    def Display(self):
        print("Name  :",self.Name)
        print("Amount :",self.Amount)
        
    

def main():
    bobj=BankAccount("XYZ",12000)
    bobj.Deposit()
    bobj.WithDraw()
    bobj.CalculateIntrest()
    bobj.Display()
if __name__=="__main__":
    main()