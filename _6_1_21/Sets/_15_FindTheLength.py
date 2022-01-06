#Find the length of a set

class Demo:
    def __init__(self):
        pass
    def create(self):
        a=set()
        a1=int(input("how many values"))
        for i in range(a1):
            b1=int(input("enter the elementss"))
            a.add(b1)
        print(a)
        print("the length of the set is",len(a))
d=Demo()
d.create()