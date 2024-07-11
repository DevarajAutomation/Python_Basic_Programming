class SimpleStock:

    def __init__(self,name,shares,price):
        self.name=name
        self.shares=shares
        self.price=price

    def cost_calculate(self):
        return self.price * self. shares
    

obj1=SimpleStock("AAA",100,21.11)
obj2=SimpleStock("AAB",90,23.12)

print(obj1.cost_calculate())
print(obj1.__dict__)
print(obj2.__dict__)
print(obj1.__class__)
print(SimpleStock.__dict__["cost_calculate"] (obj1))