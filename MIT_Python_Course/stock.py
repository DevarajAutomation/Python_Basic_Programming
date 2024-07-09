import csv

class Stock:

    def __init__(self,name,shares,price):
        self.name=name
        self.shares=shares
        self.price=price

    def read_portfolio(self,filepath):

        file=open(filepath,'r')
        csv_reader=csv.reader(file)
        header=next(csv_reader)

        for row in csv_reader:
            print(row)

    def sell_shares(self,nshares):

        sell= self.shares - nshares
        self.shares=self.shares - sell
        return self.shares
    
    def print_data(self,filepath):
        file=open(filepath,'r')
        csv_reader=csv.reader(file)
        header=next(csv_reader)

        for row in csv_reader:
            print('%10s %10d %10.2f' % (self.name,self.shares,self.price))


obj=Stock('GOOG', 100, 490.1)

obj.print_data("/workspaces/Python_Basic_Programming/Data/portfolio.csv")
obj.read_portfolio("/workspaces/Python_Basic_Programming/Data/portfolio.csv")
obj.sell_shares(45)
        