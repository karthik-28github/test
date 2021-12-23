#add an item in a tuple.

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
        a1=int(input("enter element to add to tuple"))
        b.append(a1)
        c=tuple(b)
        print(c)



d=Demo()
d.create()