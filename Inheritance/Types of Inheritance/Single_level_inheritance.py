class product:
    def __init__(self,model,users) -> None:
        self.model=model
        self.users=users

class phone(product):
    def __init__(self, model, users,price) -> None:
        super().__init__(model, users)
        self.price=price

p=phone("Iphone",200000,120000)
print(p.model)