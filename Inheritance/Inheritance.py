"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
"""
class user:
    def login(self):
        print("Login")
    def register(self):
        print("Register")

class student(user): # We have here inheritated the student class to user class.
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")

# Child class can access the methods, data members and constructors of parent class but parent class can't access from chlid class. Inheritance is always in upward direction.

student1=student()
student1.login()
student1.register()
student1.enroll()
student1.review()
