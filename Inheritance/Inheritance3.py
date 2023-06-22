#------------***Method Overriding in Inheritance***----------------#
# In this case of inheritance we will create 2 methods of same name in both parent and child class.
# and we will try to call that method from the child class.

class phone:
    def __init__(self,phone,price) -> None:
        self.phone=phone
        self.price=price
    def ring():
        print("Inside phone class")

class smartphone(phone): # Inheriting parent class to child class.
    def ring():
        print("Inside Smartphone class")
    pass

apple=smartphone("Apple",120000)
# Smartphone class is taking input for the constructor of the parent class.
print(apple.phone)
print(apple.price)
# Child class is properly working with the parent class constuctor.
smartphone.ring()
# But when we called the method ring which is in both parent and child class what will happen -
"""
    Every time we call a method, data member or attribute the child class first search it inside its methods and own class
    and when it does't find it so it moves to the parent class.
    But if it found the method of same name inside it's own class it overwrites the method of parent class.
    This is called as method overriding and is the concept of polymorphism.
"""