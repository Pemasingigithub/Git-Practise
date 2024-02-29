from exit import exit_function, student_info
class Employee:
    def __init__(self, n, s):
        self.name = n
        self.salary = s

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, n, s, b):
        super().__init__(n, s)
        self.bonus = b

    def getSalary(self):
        return self.salary + self.bonus


def main_form():
    print("""Employee details
================""")
    n = input("Enter the name:_")
    s = float(input("Enter the salary:_"))
    e1 = Employee(n, s)
    name = e1.getName()
    print("Total salary for {} is Rs {}".format(name.capitalize(), e1.getSalary()))

    print("""
| Manager details |
___________________""")
    n = input("Enter the name:_")
    s = float(input("Enter the salary:_"))
    b = float(input("Enter the bonus:_"))
    m1 = Manager(n, s, b)
    name = m1.getName()
    print("Total salary for {} is Rs {}".format(name.capitalize(), m1.getSalary()))
    yesno = exit_function()
    if yesno == 'y' or yesno == 'Y':
        main_form()
name1, Id = student_info()
main_form()
