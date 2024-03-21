class People:
    name=input("Enter the people name:_").capitalize()
    occupation=input("Enter the people occupation name:_").capitalize()
    def output_data(self):
        self.name
        self.occupation
        print(f"My name is {self.name}".format(self.name), f'and I am {self.occupation}'
              .format(self.occupation))
m=People()
m.output_data()






class Employee:
    def input_data(self):
         self.id=int(input("Enter the employee id:_"))
         self.name=input("Enter the employee name:_").capitalize()
         self.salary=int(input("Enter the employee salary:_"))
    def display_data(self):
        print(f'Employee id is:{self.id}'.format(self.id))
        print(f"Employee name is:{self.name}".format(self.name))
        print(f"Employee salary is:{self.salary}".format(self.salary))

e=Employee()
e.input_data()
e.display_data()

class Animal:
    def __init__(self,name,eat,type):
     self.name=name
     self.eat=eat
     self.type =type

A=Animal(input("Enter the animal name:_").capitalize(),input("What eats by animal:_").capitalize(),
         input("Enter the animal type:").capitalize())

print("Animal name is:",A.name)
print("Animal eats:",A.eat)
print("Animal type is:",A.type)

class Person:
    #self can access the variable of animal class
    def __init__(self,name,age,weight,address):
       self.name=name
       self.age=age
       self.weight=weight
       self.address=address

#Inheritance example
class Student(Person):
    pass

# Here obj is Entity and name,age,weight and address are attribute
obj1=Person(input("Enter the person name:").capitalize(),
            int(input("Enter the person age:")),
            int(input("Enter the person weight:")),
            input("Enter the person address:").capitalize())

print("Person name is:",obj1.name,"Age is:",obj1.age,"Person weight is:",obj1.weight,
      "Person address is:",obj1.address)

obj2=Student(input("Enter the student name:").capitalize(),
             int(input("Enter the student age:")),
             int(input("Enter the student weight:")),
             input("Enter the student address:").capitalize())

print("Student name is:",obj2.name,"Student age is:",obj2.age,"Student weight is:",obj2.weight,
      "Student address is:",obj2.address)







