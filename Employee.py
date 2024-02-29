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


e1 = Employee('Ram', 8000)
print("Total salary for {} is Rs {}".format(e1.getName(), e1.getSalary()))

m1 = Manager("Simon", 3000, 4000)
print("Total salary for {} is Rs {}".format(m1.getName(), m1.getSalary()))
