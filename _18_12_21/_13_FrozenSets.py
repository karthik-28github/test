#FrozenSets Exampe

#Find the length of a set

class Demo:
    def __init__(self):
        pass
    def create(self):
        a=set()
        fa=set()
        a1=int(input("how many values"))
        for i in range(a1):
            b1=int(input("enter the elementss"))
            a.add(b1)
        print(a)
        q=input("Do you want to freez the set Y/N")
        print("once you freez the set is immutabe")
        if q=="y":
            fa=frozenset(a)
        print(fa)
d=Demo()
d.create()