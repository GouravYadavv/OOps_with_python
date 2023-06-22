# The super() function is used to give access to methods and properties of a parent or sibling class. The super() function returns an object that represents the parent class.

class phone:
    def __init__(self,brand,price) -> None:
        self.brand=brand
        self.price=price
    def buy(self):
        print("Buy a phone")

class smartphone(phone):
    print("This is a smartphone")

    def buy(self):
        print("Buy a smartphone")
        super().buy() # The super function will here call the buy method from the class phone which is the parent class for the child class smartphone.

a=smartphone("Apple",120000)
a.buy()

# If we would have not used the super function here so the output will be the buy method of the smartphone class becuase of the method overriding.