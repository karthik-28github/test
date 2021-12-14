#Check a list contains sublist

class Demo:
    def __init__(self):
        self.stq=""
    def prr(self,a):
        for i in a:
            if type(i) is list:
                self.stq=("we have a sublist")
        print(self.stq)


d=Demo()
a=[0,4,7,1,6,8,13,179,49,4,16,218,[1,2,3,4,6],3189,217,117,329,127,67,31,94,5]
d.prr(a)