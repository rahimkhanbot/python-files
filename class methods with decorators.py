
import datetime as dt

class Employees:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employees.num_of_emps += 1


    def fullname(self):
        return '{} {}' .format(self.first, self.last)

    def set_raise(self):
        self.pay = int(self.pay + self.raise_amt)

    def __repr__(self):
        return "Employees('{}', '{}', '{}')" .format(self.first, self.last, self.pay)

    def __str__(self):
        return  '{} - {}' .format(self.fullname(), self.email)

    @classmethod
    def high_raise(cls, amount):
        cls.raise_amt = amount

    # alternative constructor to split names  from '-' to normal main class format
    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return  cls(first, last, pay)

    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True



# creating subclass for main class Employees
class Developer(Employees):
    num_of_dev = 0
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employees):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.fullname())




dev_1 = Developer('daryl', 'muffer', 50000, 'python')
dev_2 = Developer('corey', 'shcafer', 70000, 'java')

mgr_1 = Manager('arvind', 'kumar', 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.rem_emp(dev_1)

mgr_1.print_emp()

print(dev_1.email)
print(dev_2.prog_lang)



my_date = dt.date(2019, 4, 7)
print(Employees.is_working(my_date))

emp_1 = Employees('ameer', 'khan', 50000)
emp_2 = Employees('haroon', 'khan', 60000)

emp_str_1 = 'babu-ji-40000'
emp_str_2 = 'mahesh-chetah-60000'
emp_str_3 = 'ashish-kumar-80000'

# create a variable for the string employees
new_emp1 = Employees.from_str(emp_str_1)
new_emp2 = Employees.from_str(emp_str_2)

print(new_emp1.email)
print(Employees.fullname(new_emp1))

print(emp_1.fullname())
print(Employees.fullname(emp_2))
print(emp_2.raise_amt)
Employees.high_raise(1.06)

print(emp_1.fullname(), emp_1.raise_amt)
print(Employees.num_of_emps)

print(repr(emp_1))
print(str(emp_2))