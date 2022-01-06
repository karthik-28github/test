#Shallow Copy of sets

#FrozenSets Exampe

#Find the length of a set

class Demo:
    def __init__(self):
        pass
    def create(self):
        a=set()
        b=set()
        a1=int(input("how many values"))
        for i in range(a1):
            b1=int(input("enter the elementss"))
            a.add(b1)
        print(a)
        b=a.copy()
        print("after adding 10  20 and 30 to the set B")
        b.add(10)
        b.add(20)
        b.add(30)
        print(a)
        print(b)

d=Demo()
d.create()