class customer:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def intro(self):
        print("Hello my name is",self.name,"and i am",self.age)

c1=customer("Gourav",20)
c2=customer("Ram",22)
c3=customer("Sham",24)
L=[c1,c2,c3]

for i in  L:
    i.intro()