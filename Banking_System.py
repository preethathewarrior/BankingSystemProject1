print("Account Login".upper() +"\n")

class Account_Login:
    def __init__(self,user_id,password,phone_no):
        self.x=user_id
        self.y=password
        self.z=phone_no
    def user_id(self):
        x = input("Enter the user id")
        if x == self.x:
            print(self.x)
        else:
            print("user_id is wrong")

    def password(self):
        y = input("Enter the password")
        if y == self.y:
            print(self.y)
        else:
            print("password is wrong")

    def phone_no(self):
        z = int(input("Enter the Phone number"))
        if z == self.z:
            print(self.z)

        else:
            print("phone number is wrong")
            print("Your account will block after 4 invalid attempts")

A=Account_Login("preetha",'P9345',2222)
A.user_id()
A.password()
A.phone_no()

print("Amount Depositing".upper()+"\n")

class Amount_Depositing:
    def __init__(self,Savings_Account,Fixed_Deposit_Account,Recurring_Deposit_Account):
        self.a=Savings_Account
        self.b=Fixed_Deposit_Account
        self.c=Recurring_Deposit_Account
    def SB(self):
        q=int(input("Enter the amount depositing:"))
        print(q+self.a+((self.b*0.0785*10)/100))
    def FD(self):
        print(self.b)
    def RD(self):
        w=int(input("Amount Depositing per month:"))
        print(w*(1+0.049/4)**(4*1/12)+self.c)
AD=Amount_Depositing(10000,20000,1000)
AD.SB()
AD.FD()
AD.RD()

print("Amount Withdrwal".upper()+"\n")

class Amount_Withdrwal():
    def amount(self):
        d = int(input("Enter the amount:"))

        if d == 200:
            print(d)
        elif d == 500:
            print(d)
        elif d == 1000:
            print(d)
        elif d == 2000:
            print(d)
        elif d == 3000:
            print(d)
        elif d == 5000:
            print(d)
        elif 5000 < d <= 25000:
            print(d)
        else:
            print("Not Available")
            d = int(input("Enter the amount:"))
            print(d)

AW=Amount_Withdrwal()
AW.amount()















