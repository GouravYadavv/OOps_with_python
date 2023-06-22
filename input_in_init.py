class name:
    def __init__(self,gender) -> None:
        self.name=input("Please enter you name.")
        self.gender=gender
def greet(name):
    if name.gender=="male":
        print("Hello",name.name,"sir.")
    elif name.gender=="female":
        print("Hello",name.name,"ma'am.")
    else:
        print("Choose gender among male and female")
a=name("male") # We can also give function an object of our class, as at the end everything in the python is object.
greet(a)