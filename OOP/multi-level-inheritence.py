class A:
    def __init__(self,name):
        self.name=name
        print('This is class A')

class B:
    def __init__(self,age):
        self.age=age
        print('This is class B')

class C(A,B):
    def __init__(self):
        print('This is class C')

        A.__init__(self,'Ravi')
        B.__init__(self,22 )
        print(f"This is {self.name}")
class D(B,C):
    print('Hello')


obj1=D()

print(obj1.age)

