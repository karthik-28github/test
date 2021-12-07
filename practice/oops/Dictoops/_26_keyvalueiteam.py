class Demo:
    def __init__(self):
        pass
    def print1(self,a):
        for i,j in a.items():
            print(i)
            print(j)
            print(a.items())



d=Demo()
a={1:"one",2:"two",3:"three",4:"one",5:"two",6:"three"}
d.print1(a)