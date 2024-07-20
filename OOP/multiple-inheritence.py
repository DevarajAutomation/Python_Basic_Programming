class Base1:
    def __init__(self):
        self.name = 'hello'
        print('This is class-1')


class Base2:
    def __init__(self):
        self.age = 45
        print("This is class-2")

        super().__init__()

class Base3(Base2, Base1):
    def __init__(self):
        Base2.__init__(self)
        Base1.__init__(self)




s1 = Base3()
print(s1.name)
print(s1.age)
