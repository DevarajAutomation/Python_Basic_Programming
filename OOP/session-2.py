import random


class Person:
    gender = 'male'

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def display(self):
        print("{}".format(self.name))
        print("{}".format(self.age))

    def details(self):
        print("Hello my name is {}".format(self.name))


class Employee(Person):
    employee_id = 0
    employee_id += random.randint(1000, 10000)

    def __init__(self, role, salary, name, age, id):
        super().__init__(name, id, age)

        self.role = role
        self.salary = salary

    def display_name(self):
        print("The employee name is {}".format(self.name))
        print("The employee ID {}".format(self.employee_id))
        print("The age of employee is {}".format(self.age))
        print("The role of employee is {}".format(self.role))
    def display(self):
        super().display()






employee = Employee('SW', 45000, 'ravi', 34, 100)

employee.display_name()
print(employee.gender)
employee.display()
