# In this program i will show you how you can use super function to give inputs to the constructor of the parent class.

class phone:
    def __init__(self,phone,price) -> None:
        self.phone=phone
        self.price=price
        print("inside the phone constructor")

class smartphone(phone):
    def __init__(self, phone, price,os) -> None:
        print("hum first") # This will run first and then will go to the parent's constructor.
        super().__init__(phone, price) 
        # When you use super function you don't have to redefine the variables which are already defined once in the parent class and it automatically assigns value to the parent class constructor.
        self.os=os
        print("inside the smartphone constructor")

s=smartphone("apple",120000,"ios")

print(s.os)
print(s.phone)
"""
    So this program will execute in the following manner-
    1. the code will start from the smartphone class.
    2. then it will compile till the super function comes and it will direct our compiler to the parent code.
    3. after searching for the os vlaue in the parent class, it does't get anything and will return to the smartphone class (child class).
    4. as it found the vlaue of the os it will display it and will work according to the algorithm and will search for the next value with the same apprach.
"""