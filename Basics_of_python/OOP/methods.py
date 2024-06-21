"""Methods are functions inside the class"""

class Dog:
    info="Hey! I am mammal and loyal"

    def __init__(self,name) -> None:
        self.name=name

    def bark(self):
        print(f"Hello my name is {self.name}")


dog1=Dog('German')
dog1=Dog('Hello')
dog1.bark()