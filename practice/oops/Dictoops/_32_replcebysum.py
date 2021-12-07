class Demo:
    def __init__(self):
        self.sum2=0
    def sum1(self,a):
        for i in a.values():
            self.sum2=self.sum2+i
        for j in len(a):
            dict2=dict(zip(j,self.sum2))
        print(a)





d=Demo()
a= {'a': 100, 'b': 200, 'c': 300}
d.sum1(a)