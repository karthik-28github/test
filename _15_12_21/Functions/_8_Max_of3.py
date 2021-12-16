
#max of 3 numbers


class Demo:
    def __init__(self):
        self.highest=0
    def pri(self,a):
        if a[0]>a[1]and a[2]:
            self.highest=a[0]
        elif a[1]>a[2]and a[0]:
            self.highest=a[1]
        else:
            self.highest=a[2]
        print("the highest number among ",a,"is :",self.highest)



d=Demo()
a=[]
for i in range(3):
    j=int(input("enter number"))
    a.append(j)
d.pri(a)
