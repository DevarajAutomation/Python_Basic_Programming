class DOG:

    family='mammal'

    def __init__(self,name,age,colour):

        self.name=name
        self.age=age
        self.colour=colour

    def bark(self):

        print(f"The dog named {self.name} is barking at the door and it belongs {self.family}")


dog1=DOG('Boli',4,'white')

print(dog1.name)
dog1.bark()