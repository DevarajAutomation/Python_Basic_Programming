class Person:
    def __init__(self,name,age):
        self.name=name

        self.age=age

    def get_details(self):
        print(f'Hello {self.name} ')

class Employee(Person):


    def greet_message(self,id):

        print(f"Hello {self.name} your id is {id}")


emp1=Employee('Ravi',22)

print(emp1.name)
print(emp1.age)
emp1.get_details()
emp1.greet_message(1111)