# In this case of inheritance we will give output to the child class and it will store in the parent class.
class phone:
    def __init__(self,brand,price,model) -> None:
        self.brand=brand
        self.price=price
        self.model=model

class smartphone(phone):
    # Here smartphone is the child class of the parent class phone.
    # Smartphone class doesn't have any constructor but phone class have.
    pass

apple=smartphone("Apple",120000,"Iphone 12 pro")
# Now as we have given the values to the smartphone class but it doesn't have any constructor but it will still work.

print(apple.brand)
print(apple.price)
print(apple.model)
# So you can use constructor of the parent class if child class doesn't have.