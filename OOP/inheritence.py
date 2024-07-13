class Person:

    def __init__(self,name):
        self.name=name

    def is_employee(self):
        return True

class Employee(Person):

    def get_name(self):

        return self.name


emp1=Employee('Ravi')

print(emp1.name)