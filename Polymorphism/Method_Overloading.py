# Method overloading is a means by which you can call the same method in different ways, i.e. with different parameters based on the number of arguments or their different datatypes.

"""
    Example of method overloading
    A function inside a class is called as method. Using a same method for different operatinos is called as method overloading.
    In this program we are going to use a area function of gerometry class to calculate the area of rectangle as well as circle also.
"""
class geometry:
    def area(self,a,b=0):
        if b==0:
            print("Area of cricle:",3.14*a*a)
        else:
            print("Area of rectangle:",a*b)


obj=geometry()

obj.area(4)
obj.area(4,5)