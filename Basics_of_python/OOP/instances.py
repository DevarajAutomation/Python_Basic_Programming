import random
class Dog:

    info = "I am mammal"

    def __init__(self) -> None:
        print('I am german shepard!')
        """The instance variables are variables which can be accessed inside an object"""
        self.number=random.randint(1,14)

#Instances of a class are called objects

dog1=Dog()
dog2=Dog()

print(dog1.info)
print(dog2.number)

