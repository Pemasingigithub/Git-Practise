#Calculator 1: Using class , object , function[method] and  inheritance
class Calculator:
    def __init__(self, n1, n2):
        self.number1 = n1
        self.number2 = n2
class Add(Calculator):
    pass
    def addition(self):
       return self.number1+self.number2 #Addtion

class Sub(Add):
    pass
    def subtraction(self):
      return self.number1-self.number2  #Subtraction

class Mul(Sub):
    pass
    def multiplication(self):
      return self.number1*self.number2 #Multiplication


class Div(Mul):
    pass
    def division(self):
        try:
         return self.number1/self.number2 #Divison4
        except ZeroDivisionError:
            exit("you can not divide by zero to any number sir")

def user_input():
    n1 = int(input("Enter first number:_"))  # Input first number
    n2 = int(input("Enter the second number:_"))  # Input second number
    return n1, n2

while True:
    print("What do you want?")
    option_input=("1.Addition\n 2.Subtract\n 3.Multiply \n 4.Divide ")
    print(option_input)
    try:
     select_number=int(input("Select the above option:_"))
    except ValueError:
             exit("Give only integer value")
    if select_number == 1:
        x, y = user_input()
        a = Add(x, y)
        print("Result is:", a.addition())
    elif select_number == 2:
        x, y = user_input()
        s = Sub(x, y)
        print("The result is :", s.subtraction())
    elif select_number == 3:
        x, y = user_input()
        m = Mul(x, y)
        print("The result is:", m.multiplication())
    elif select_number == 4:
        x, y = user_input()
        d = Div(x, y)
        print("The result is:", d.division())
    else:
        print("Invalid option")
        break
def exit_method():
    yesno = input("Do you want continue[y or n]:_")
    if yesno == 'y' or yesno == 'Y':
        c.calculation()
        exit_method()  # loop
    else:
        print("Exit program")

# Calculator 2: Using class , function , object
class Cal:
    def calculation(self):
      operator_choose = input("choose operator:['+','-','*','/']_")
      self.num1 = int(input("Enter number 1:_"))
      self.num2 = int(input("Enter number 2:_"))
      if operator_choose == '+':
         return print("The sum is:",self.num1+self.num2)
      elif operator_choose == '-':
         return print("The subtract is:", self.num1 - self.num2)

      elif operator_choose == '*':
         return print("The multiplication is:", self.num1 * self.num2)

      else:
         return print("The divide is:", self.num1 / self.num2)

print("Now next other method of calculator")
c = Cal()
c.calculation()
def exit_method():
    yesno = input("Do you want continue[y or n]:_")
    if yesno == 'y' or yesno == 'Y':
        c.calculation()
        exit_method()  # loop
    else:
        print("Exit program")
exit_method()





















