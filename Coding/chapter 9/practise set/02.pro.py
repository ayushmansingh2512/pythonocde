import math

class Calculator:
    def __init__(self, n):  # fixed constructor
        self.n = n

    def square(self):
        print(f"The square of this number is {self.n * self.n}")
    
    def cube(self):
        print(f"The cube of this number is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The square root of this number is {math.sqrt(self.n)}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
