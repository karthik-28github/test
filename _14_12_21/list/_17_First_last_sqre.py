#First,Last elements whose square value is between 1 and 30,except first 5
a=[i for i in range(1,100) if i*i <30]

class Demo:
    def __init__(self):
        pass
    def pri(self,a):
        for i in a:
            if i*i < 30:
                print(i,end=" ")



d=Demo()
a=list(range(1,100))
d.pri(a)