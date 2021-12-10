from abc import ABC,abstractmethod
# import math

class Lstsummul:
    @abstractmethod
    def calculate(self,lst):
        pass

class Sumlst:
    def calculate(self,lst):
        print(f'sum of all numbers in lists is :{sum(lst)}')

class Sumlstsquare:
    def calculate(self,lst):
        print(f'square of sum of all numbers in lists is :{sum(lst)*sum(lst)}')

num=int(input("enter number of items:"))
lst=[]
for i in range(num):
    l1=int(input("enter number:"))
    lst.append(l1)

print(lst)

s1=Sumlst()
s1.calculate(lst)
s2=Sumlstsquare()
s2.calculate(lst)
