class student():
    def __init__(self) -> None:
        self.__name=""
    def getname(self):
        return self.__name
    def editname(self,name):
        self.__name=name

a=student()
a.editname("Ram")
b=a.getname()
print(b)