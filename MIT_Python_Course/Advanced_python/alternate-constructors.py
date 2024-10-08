class Stock:

    types=(str,int,float)

    def __init__(self,name,shares,price):
        self.name=name
        self.shares=shares
        self.price=price

    @classmethod
    def from_row(cls,row):
        values=[func(val) for func,val in zip(cls.types,row)]

        return cls(*values)
    
row=['AAA',23,21.1]
obj=Stock('AAA',23,21.1)
print(obj.from_row(row))

    
    