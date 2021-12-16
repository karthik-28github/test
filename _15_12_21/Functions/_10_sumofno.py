#sum of all the numbers in a list


class Demo:
    def __init__(self):
        self.sum1=0
    def sum(self,a):
        for i in a:
            self.sum1=self.sum1+i
        print(self.sum1)



d=Demo()
a=range(100)
d.sum(a)