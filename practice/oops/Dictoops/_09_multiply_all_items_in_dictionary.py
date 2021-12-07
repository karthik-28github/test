class Muldict:
    def mul_dict(self,dict1):
        b1=1
        for num in dict1.values():
            b1 =b1*num
        print(f'mulptiply all elements in dictionaries is {b1}')

dict1={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
d1=Muldict()
d1.mul_dict(dict1)