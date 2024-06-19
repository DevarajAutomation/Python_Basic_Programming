class Person():
    def __init__(self) -> None:
        self.fname='Dev'
        self.lname='Raj'
        self.age=30

    def __repr__(self) -> str:
        return f"<Person class - fname:{self.fname}, lname:{self.lname},age: {self.age}>"
    def __str__(self) -> str:
        return f"fname:{self.fname},lname:{self.lname},age:{self.age}"
    
cls1=Person()

print(repr(cls1))
print(str(cls1))
print(f"Formatted:",(cls1))