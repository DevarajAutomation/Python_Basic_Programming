class A:

    def __init__(self,c,d):
        self.c=c
        self.__d=d

        print('This is class A')


class B(A):
    def __init__(self, e, c, d):
        super().__init__(c, d)
        print('This is class B')
        self.e=e






b1=B(10,12,13)

print(b1.c)
print(b1.d)