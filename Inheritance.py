class Calculator:
    def __init__(self,f, s):
        self.first = f
        self.second = s
class Add(Calculator):
    super().__init__()
    def add_number(self):
        return self.first+self.second
class Sub(Calculator):
    super().__init__()
    def sub_number(self):
        return self.first-self.second
class Mul(Calculator):
    super().__init__()
    def mul_number(self):
        return self.first*self.second
class Div(Calculator):
    super().__init__()
    def div_number(self):
       return self.first/self.second

c=Calculator(4,4)




