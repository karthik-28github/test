class Demo:
    def __init__(self):
        pass
    def palandrome(self,a):
        pass

class Demo1(Demo):
    def palandrome(self,a):
        y=len(a)
        palandrome=False
        for i in a-1:
            while i!=a[y]:
                if i==a[y]:
                    i+=1
                    y-=1
                    palandrome=True
        if palandrome==True:
            print(a,"is palandrome")





d=Demo1()
a=input("enter the palandrome String")
d.palandrome(a)