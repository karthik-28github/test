#remove the element if element is available

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
        z=input("do you want to clear the set Y/N")
        z.lower()
        if z=="y":
            a.clear()
        print(a)
d=Demo()
d.create()