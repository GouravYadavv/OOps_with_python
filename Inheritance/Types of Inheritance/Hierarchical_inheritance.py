# It is a type of inheritance in which 2 child classes have one parent class.
# Or in other words in this type of inheritance 2 classes inherites from a single class.

class product():
    def __init__(self,model,sales) -> None:
        self.model=model
        self.sales=sales
    def sale(self):
        print("This is sales",self.sales)

class iphone(product):
    def __init__(self, model, sales,feature) -> None:
        super().__init__(model, sales)
        self.feature=feature
        self.feature()
    def feature(self):
        print("It has the following feature:",self.feature)

class android(product):
    def __init__(self, model, sales,feature) -> None:
        super().__init__(model, sales)
        self.feature=feature
        self.feature()
    def feature(self):
        print("It has the following feature:",self.feature)

