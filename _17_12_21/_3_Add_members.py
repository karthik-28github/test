#Add member(s) in a set.
class Demo:
    def __init__(self):
        pass
    def create(self):
        a=set()
        a1=int(input("how many values"))
        for i in range(a1):
            b1=int(input("enter the elementss"))
            a.add(b1)
        print("before adding new element")
        print(a)
        a2=int(input("enter the new element"))
        a.add(a2)
        print("after adding new element")
        print(a)
d=Demo()
d.create()