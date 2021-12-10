from abc import ABC,abstractmethod

class Numbers:
    def numbers_are(self,lst):
        print(f'list of numbers is :{lst}')

    @abstractmethod
    def print_numbers(self,lst):
        pass

class Evennum(Numbers):
    def print_numbers(self,lst):
        print(f'even numbers are:{lst[1::2]}')

class Oddnum(Numbers):
    def print_numbers(self,lst):
        print(f'odd numbers are:{lst[0::2]}')


lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n1=Evennum()
n1.numbers_are(lst)
n1.print_numbers(lst)
n2=Oddnum()
n2.numbers_are(lst)
n2.print_numbers(lst)