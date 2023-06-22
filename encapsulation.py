''' 
Encapsulation is a way to restrict the direct access to some components of an object, so users cannot access state values for all of the variables of a particular object. Encapsulation can be used to hide both data members and data functions or methods associated with an instantiated class or object.

------------*****-----IMPORTANT NOTE-----*****-----------------

In python you can't set any data or function completely private, if they are set private they can still be accessed by specific syntax which we are going to cover in this program.

'''
# Let's create a class for ATM
# In ATM class you will be able to change the pin of your account.
class atm():
    def __init__(self) -> None:
        self.__pin="1001"
        self.__balance=1000
        #self.menu()
        self.get_pin()
    def get_pin(self):
        print(self.__pin)
    def menu(self):
        user_input=int(input("""Choose among the following
                                \n 1. 1 to create pin
                                \n 2. 2 to quit
                                \n 3. 3 to check balance."""))
        if user_input==1:
            self.create()
        elif user_input==2:
            quit()
        elif user_input==3:
            self.check()
        else:
            print("Invalid Input.")
    def create(self):
        temp=int(input("Enter the current Pin"))
        if temp==self.__pin:
            new_pin=input("Enter the new Pin")
            self.__pin=new_pin
        else:
            print("Invalid Pin")
    def check(self):
        temp=int(input("Enter the current Pin"))
        if temp==self.__pin:
            print(self.__balance)
        else:
            print("Invalid Pin.")

sbi=atm()
atm.get_pin()