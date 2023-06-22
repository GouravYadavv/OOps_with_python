# Static variable is a variable which remains constant for the whole class methods and is defined outside any method of a glass, or you can say it is a global variable inside a class for all the methods of that particular class.
# Let's understand this by implementing a counter in our atm machine program.

class atm():

    counter=1 # So in this program here we defined out static variable. We are going to give every costumer a serial number by this counter.

    def __init__(self) -> None:
        #self.pin=int(input("Enter you pin."))
        self.balance=1000
        self.Sno=atm.counter # It will be defined as atm.counter as it can't be accessed directly as it doesn't stored in this function.
        atm.counter+=1
        print("customer:",atm.counter) 
        #self.menu()
    def menu(self):
        user_input=int(input(''' Hello, how you would like to proceed?\n1. Press 1 to create pin.\n2. Press 2 to deposit.\n3. Press 3 to withdraw.\n4. Press 4 to check balance.\n5. Press 5 to quit.'''))
        if user_input==1:
            self.create_pin()
        elif user_input==2:
            self.deposit()
        elif user_input==3:
            self.withdraw()
        elif user_input==4:
            self.check_balance()
        elif user_input==5:
            quit()
    def create_pin(self):
            self.pin=int(input("Enter the pin"))
            print("Pin set successfully")
    def deposit(self):
            temp=int(input("Enter the pin:"))
            if temp==self.pin: 
                amount=int(input("Enter the amount to deposit:"))
                self.balance=self.balance+amount
                print("Deposit successfull.")
            else:
                print("Invalid password")
    def withdraw(self):
            temp=int(input("Enter the pin:"))
            if temp==self.pin:
                amount=int(input("Enter the amount to withdraw."))
                if amount<self.balance:
                    self.balance=self.balance-amount
                    print("Withdrawal successful. \n Your remaining balance is:",self.balance)
                else:
                    print("Insufficient balance")
            else:
                print("Invalid pin.")
    def check_balance(self):
            temp=int(input("Enter the pin:"))
            if temp==self.pin:
                print("Your balance is:",self.balance)
            else:
                print("Invalid pin.")
        
c1=atm()
c2=atm() 
c3=atm()
print(c1.Sno)
print(atm.counter)