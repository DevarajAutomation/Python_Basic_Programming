class DOG:
    family = 'mammal'

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def barking(self):
        return f"The {self.name} is {self.age} years old and he is barking and belongs {self.family}"


dog1 = DOG("karia", 'bidinai', age=4)
dog2 = DOG('bora','mani',9)

if isinstance(dog1, object):
    print('Yes')

print("The dog belongs {}".format(dog1.__class__.family))
print("The bora belong to {}".format(dog2.__class__.family))

print(dog1.barking())
print(dog2.barking())


