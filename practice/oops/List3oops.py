#smallest number of list

class Demo:
    def __init__(self):
        self.smallest=0
    def lar(self,a):
        self.smallest = a[0]
        for i in a:
            if i<self.smallest:
                self.smallest=i
        print("the smallest number among the list is ",self.smallest)

d=Demo()

a=[]
a1=int(input("how many values for a "))
for i in range(0,a1):
    a2=int(input("enter the list values for a "))
    a.append(a2)

d.lar(a)


