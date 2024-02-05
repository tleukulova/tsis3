class Account:
    def __init__(self,name,m):
        self.name=name
        self.m=m
    def Deposit(self,a):
        self.m+=a
    def Withdraw(self,a):
        if a > self.m:
           print("STOP!")
        else:
            self.m-=a
name_account=input()
m_account=float(input())
account=Account(name_account,m_account)
a_account=float(input())
account.Deposit(a_account)
a_account=float(input())
account.Withdraw(a_account)
