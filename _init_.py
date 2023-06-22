class math:
    def __init__(self) -> None:
        self.a=int(input("Enter a:"))
        self.b=int(input("Enter b:"))
        self.add()
        self.sub()
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
a=math()
print(a)