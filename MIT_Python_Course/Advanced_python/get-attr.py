import tableformat

class Stock:

    def __init__(self,name,shares,stock):
        self.name=name
        self.shares=shares
        self.stock=stock

    def print_data(self):

        return tableformat.print_table()


obj=Stock('GOO',100,121.33)

print(getattr(obj,'name'))
setattr(obj,'shares',90)
print(getattr(obj,'shares'))
delattr(obj,'shares')

for s in 