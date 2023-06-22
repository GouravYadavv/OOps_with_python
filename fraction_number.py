# So in this program we are going to give python language the ability to perform operations with the fraction value.
# We are going to create a class, with the help of this class python will unlock this ability.
# So for building this class we are going to use some magic methods.
class fraction:
    def __init__(self) -> None:
        self.num=int(input("Enter the value of numerator:"))
        self.den=int(input("Enter the value of denominator:")) 
    def __str__(self) -> str: # It(str) is used to call method only when print() is used with the class
        return "{}/{}".format(self.num,self.den)
    def __mul__(self,other): # __mul__ is used to input the operation to be performed when multiplication(*) is applied.
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return '{}/{}'.format(temp_num,temp_den)
    def __sub__(self,other): # __sub__ is used to input the operation to be performed when substraction(-) is applied.
        temp_num=self.num*other.den-other.num*self.den
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __add__(self,other): # __add__ is used to input the operation to be performed when addition(+) is applied.
        temp_num=self.num*other.den+other.num*self.den
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __truediv__(self,other): # __truediv__ is used to input the operation to be performed when division(/) is applied.
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        return"{}/{}",format(temp_num,temp_den)

print(fraction())

# ------------*****----- IMPORTANT NOTE -----*****---------------#
# In this program I have just shown you some basic example of magic methods, you can find a complete list of these on internet and can code some really cool program with it, so please explore rest by your own.