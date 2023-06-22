# In this python program we will see how the inheritance functions if child class has it's own constructor.

class phone:
    def __init__(self,phone,price) -> None:
        self.phone=phone
        self.price=price
    def get_price(self):
        return self.price

class smartphone(phone):
    def __init__(self,price,phone,model) -> None:
        self.phone=phone
        self.price=price
        self.model=model
        pass

a=smartphone(120000,"Iphone","12 pro") # Even if the input taken by the child class is not the format of parent class, it will still get assigned to the right one.
print(a.get_price())