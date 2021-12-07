#Create a union of sets

class Demo:
    def __init__(self):
        pass
    def union1(self,a,b):
        print(a.union(b))

d=Demo()
a=set()
a1=int(input("how many values for a "))
for i in range(0,a1):
    a2=int(input("enter the list values for a "))
    a.add(a2)
print("the set available is ",a)

b=set()
b1=int(input("how many values for b "))
for i in range(0,b1):
    b2=int(input("enter the list values for b "))
    b.add(b2)
print("the set available is ",b)

c=input("do you want to do union")
if c=="y":

    print("the union of ",a,"and ",b,"is")
    d.union1(a,b)
