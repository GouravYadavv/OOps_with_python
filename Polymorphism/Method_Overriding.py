#  Method Overriding is redefining a parent class method in the derived class. Overriding requires inheritance for implementation.
# Inheritance is required for method overriding.

class product():
    def review(self):
        print("This is the review of product class.")
    def rewind(self):
        print("This is the rewind method of the product class.")

class smartphone(product):
    def rewind(self):
        print("This is the rewind method of the smartphone class.")

# As we can see we have defined two methods by the same name in both the parent and chlid class,
# So the method of child class will override the method of parent class.
# This states that whenever we call a method from child class it first searches for the method in own class then if doesn't 
# found then moves to the parent class.

a=smartphone()
a.review() # This will return the method from the product class which is the parent class for the smartphone class.
a.rewind() # But this will return the method from it's own class, as method is present in this class.