#check whether an element exists within a tuple

class Demo:
    def __init__(self):
        pass
    def create(self):
        b=[]
        a=int(input("how many valyes you are willing to enter"))
        for i in range(a):
            z=int(input("enter elements"))
            b.append(z)
        c=tuple(b)
        print(type(c))
        print(c)
        dict1=dict()
        a1=int(input("enter the element which you are serching "))
        for i in c:
            if i==a1:
                print(i,"found in tuple")




d=Demo()
d.create()