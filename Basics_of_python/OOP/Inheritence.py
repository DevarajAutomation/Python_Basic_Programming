"""Accessing all the variables and methods from another class"""




class Dog:
    info="I am a dog"

    def __init__(self,name) -> None:
        print('Dog is created')
        self.name=name

class Animal(Dog):
    #info='I am a animal called dog'
    pass

    


dog1=Animal('Pseudo')
print(Animal.info)
print(dog1.name)