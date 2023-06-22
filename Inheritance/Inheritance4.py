# Try to call implement inheritance on encapsulated variables (private variable) .
class phone:
    def __init__(self,brand,phone,price) -> None:
        self.__brand=brand
        self.phone=phone
        self.price=price
    def get_brand(self):
        print(self.__brand)

class smartphone(phone):
    #def get_brand2(self):
     #   print(self.__brand) # Invalid, because to access the use the self values of the phone class this method should be defined inside of that class only.
    pass

# Here we gave values to the parent class constructor and tried to access the encapulated variable.
a=smartphone("Apple","Iphone 12 pro",120000)
print(a.phone)
a.get_brand() # This will work as we have already defined a method in the parent class to return the  private value and child class can call that method fron parent class.
#a.get_brand2() # This will not work.


# Here we accessed and get the private variable printed which shows that
b=phone("Apple","Iphone 12 pro",120000)
b.get_brand()
# Here we can access the private variabels of the phone by using the methods defined inside of it.
# It shows that the child class can't directly access the private values of the parent class.