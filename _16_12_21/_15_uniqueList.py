#takes a list and returns a new list with unique elements of the first list.

class Demo:
    def __init__(self):
        pass
    def Uniq(self,a):
        b=set(a)
        return b
d=Demo()
a=[10,20,30,10,50,60,80,30,50,40,20,10,0,90,20,50]
b=d.Uniq(a)
print("givin  list is ",a)
print("the Uniq list is ",b)