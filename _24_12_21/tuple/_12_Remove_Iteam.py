# remove an item from a tuple

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
        a1=int(input("enter value you want  to remove"))
        for i in b:
            if i==a1:
                b.remove(a1)

        print(tuple(b))







d=Demo()
d.create()