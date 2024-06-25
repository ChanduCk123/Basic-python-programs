import sys
class customer:
    bankname="HDFC Bank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amnt):
        self.balance = self.balance+amnt
        print(f"balance after deposit: {self.balance}")
    def withdraw(self,amnt):
        if amnt > self.balance:
            print("insufficent funds.....")
            sys.exit()
        else:
            self.balance = self.balance-amnt
            print("Balance after withdraw: ",self.balance)
print("welcome to ",customer.bankname)
name=input("Enter your name: ")
c=customer(name)
while True:
    print("d-deposit\nw-withdraw\ne-exit")
    option=input("choose your option: ")
    if option=="d" or option=="D":
        amnt=float(input("Enter amount: "))
        c.deposit(amnt)
    elif option=="w" or option=="W":
        amnt=float(input("Enter amount: "))
        c.withdraw(amnt)
    elif option=="e" or option=="E":
        print("Thanks for Banking")
        sys.exit()
    else:
        print("Invalid option..pls choose valid option")
    
        