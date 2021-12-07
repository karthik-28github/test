#Add member(s) in a set.

class Demo:
    def __init__(self):
        self.i=0
        self.ele=0
    def addset(self,a):
        i=int(input("to which index you need to add"))
        ele=int(input("which element you need to add "))
        b=list(a)
        c=len(a)-1
        for j in a:
            if i==j:
                b[c]=b[c-1]
                b[i]=ele

        a=set(b)
        print("set after adding ",a)





d=Demo()
a=set()
a1=int(input("how many values for a "))
for i in range(0,a1):
    a2=int(input("enter the list values for a "))
    a.add(a2)
print("the set available is ",a)
b=input("do u want to add elements to the set y/n")
if b=="y":
    d.addset(a)
