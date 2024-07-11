class A:
    def spam(self):
        print('a')

class B(A):
    def spam(self):
        print('b')
        super.spam()

class C(B):
    def spam(self):
        print('c')
        super.spam()

c=C()
print(C.__mro__)
print(c.spam())
        