class Stock:

    def __init__(self, shares, price):
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price


s1 = Stock(75,75)
print(s1.cost())
print(s1.price)

