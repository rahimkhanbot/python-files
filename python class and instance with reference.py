

class Employees:

    def __init__(self, first_name, last_name, pay):  # __init__ is a method it is known as constructor in other language
        # inside () it is arguments
        self.first_name= first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

emp_1 = Employees("Abdul", "Rahimkhan", 50000)
emp_2 = Employees("Haroon", "Rasheedkhan", 70000)

print(emp_2.fullname())
print(Employees.fullname(emp_1))
print(emp_2.email)

print("----------------------")
