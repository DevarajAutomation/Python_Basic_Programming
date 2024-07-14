class Addition:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum_of_two(self):
        print(self.a + self.b)


obj1 = Addition(2,3)
print(obj1.sum_of_two())