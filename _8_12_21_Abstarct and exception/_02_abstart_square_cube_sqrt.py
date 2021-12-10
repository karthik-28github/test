from abc import ABC,abstractmethod
import math
class Myclass:
    @abstractmethod
    def calculate(self,x):
        pass

class sub1:
    def calculate(self,x):
        print(f'Square of a number{x} is {x*x}')

class sub2:
    def calculate(self,x):
        print(f'Cube of a number{x} is {x*x*x}')

class sub3:
    def calculate(self,x):
        print(f'Square root of number{x} is {math.sqrt(x)}')


a1=sub1()
a1.calculate(9)
a2=sub2()
a2.calculate(9)
a3=sub3()
a3.calculate(9)