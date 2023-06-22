# Aggregation is a "has a" type of relationship betweem 2 classes, as customer class has adress in the program below.
class customer:
    def __init__(self,name,number,address) -> None:
        self.name=name
        self.number=number
        self.address=address
class address:
    def __init__(self,city,pin_code,state) -> None:
        self.city=city
        self.pin_code=pin_code
        self.state=state
    def change(self,new_city,new_pin_code,new_state):
        self.city=new_city
        self.pin_code=new_pin_code
        self.state=new_state

add=address("Rewari",123401,"Haryana")
print(add.city) # Here we have given values to the class address and now we are going to use it in the customer class.

cust=customer("Gourav",1112223330,add)
print(cust.address.city) # As you can see here the customer class is useing the object of addess class.

add.change("Ambala",222211,"Haryana")
print(cust.address.city) # The change method of address class is also working with the customer class.