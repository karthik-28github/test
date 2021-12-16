#multiplay of all the numbers in a list


class Demo:
    def __init__(self):
        self.mul1=1
    def multi(self,a):
        for i in a:
            self.mul1=self.mul1+i
        print(self.mul1)



d=Demo()
a=range(1,100)
d.multi(a)