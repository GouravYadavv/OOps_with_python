# It is a type of inheritance in which one child class have 2 parent clas.

class phone:
    def __init__(self,company,price,model) -> None:
        self.company=company
        self.price=price
        self.model=model
    def buy(self):
        print("Buying a phone")

class smartphone:
    def feature(self):
        print("It has more features than an oridinary phone")
    def brought(self):
        print("Brought a smartphone")

"""
----------------*** IMPORTANT NOTE***------------
MRO method resolution order, it is the order which defines the priority of the class if we are provided with the multiple parent class
so in the order we write them, is also the order they will have priority from high to lower as we move from left to right.
"""

class product(phone,smartphone): # Here i have inherited 2 class to the product class. We can also inherite more than 2 classes also by same method.
    pass

p=product("Apple",120000,12)
p.brought()
print(p.company)
p.buy()