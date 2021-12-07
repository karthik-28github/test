#largest number of list

class Demo:
    def __init__(self):
        self.largest=0
    def lar(self,a):
        self.largest = a[0]
        for i in a:

            if i>self.largest:
                self.largest=i
        print("the largest number among the list is ",self.largest)

d=Demo()

a=[]
a1=int(input("how many values for a "))
for i in range(0,a1):
    a2=int(input("enter the list values for a "))
    a.append(a2)

d.lar(a)


