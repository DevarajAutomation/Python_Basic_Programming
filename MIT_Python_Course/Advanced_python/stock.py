class Stock:

    def __init__(self,name,shares,price):

        self.name=name
        self.shares=int(shares)
        self.price=float(price)

    def calculate_total(self):

        return self.shares * self.price
    


obj=Stock('IBM',25,22.22)

print(obj.calculate_total())


    