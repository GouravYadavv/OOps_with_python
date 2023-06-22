# Multi level inheritance is the type of inheritance in which one class is the child class to a parent class and the child class
# itself is a parent class to another class. This can be between 3 or more classes.   
class product:
    def review(self):
        print("Reviewing, product class.")
class phone(product): # phone class is the child class of the parent class product.
    def __init__(self,model,price):
        print("Inside phone constructor.")
        self.model=model
        self.price=price
        self.end()
    def buy(self):
        print("buying a phone")
    def repair(self):
        print("repairing a phone")
    def end(self):
        print("phone class completely scanned")
class smartphone(phone): # smartphone class is the child class of the parent class phone.
    pass

s=smartphone("Apple",120000)

s.review()
print(s.price)
s.buy()

"""
    How this code is going to execute-
    Class smartphone doesn't have any direct access to the class product, so if we
    will call the method of the class product from the class smartphone , first it will 
    search for that method in class it is inherited to and that is phone class, If it doesn't 
    get the method it is searching for then the phone class will search in the product class
    to which it is inherited and return the result to the smartphone class. 
"""