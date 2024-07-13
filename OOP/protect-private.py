class Base:

    def __init__(self,a,b):
        print("This is Base Class")
        self._a=a
        self.__b=b



class Derived(Base):


    def __init__(self, a, b):
        super().__init__(a, b)
        print('This is Dervied Class')


d1=Derived(12,13)

print(d1._a)
print(d1.__b)
