#Create set difference

#Create a union of sets

class Demo:
    def __init__(self):
        pass
    def difference1(self,a,b):
        print(a.difference(b))

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

c=input("do you want see difference ")
if c=="y":

    print("the difference  of ",a,"and ",b,"is")
    d.difference1(a,b)
