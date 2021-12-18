#Remove element from set
class Demo:
    def __init__(self):
        pass
    def create(self):
        a=set()
        a1=int(input("how many values"))
        for i in range(a1):
            b1=int(input("enter the elementss"))
            a.add(b1)
        print("before removing new element")
        print(a)
        a2=int(input("enter the element to which to be removed"))
        a.remove(a2)
        print("after removing element")
        print(a)
d=Demo()
d.create()