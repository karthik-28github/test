#create a tuple with numbers and print one item

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
        y=int(input("enter the index to print the value"))
        print(c[y])




d=Demo()
d.create()